# -*- coding: UTF-8 -*-
import socket
import time
import json
import sitralib.referencias as ref
from sitralib.validators.bcc import *
from sitralib.helpers.ordenar_trama import *
from pymongo import MongoClient
from bson.json_util import dumps, loads
from termcolor import colored

class Captura:
  def __init__(self, **kwargs):
    self.ordenar_trama = OrdenarTrama()
    self.configs = kwargs
    self.validator = Bcc()

    # Conexión MongoDB
    mongo_connect = MongoClient(
        self.configs['databases']["monitor"]["HOST"],
        self.configs['databases']["monitor"]["PORT"]
    )
    self.mongo_db = mongo_connect.sitra
    self.mongo_db.proceso.remove({})

    if self.configs.get('sitra_debug'):
      print(
            colored("ARGS", 'cyan', attrs=["reverse", "bold"]),
            self.configs
        )


  def get(self):
    """
    Ejecuta la captura de datos
    """
    data = list()
    counter = 0

    for trama in self.configs['tramas']:

      counter_while = 0
      while True:
        """
        Envia la trama 'n' candidad de veces intentado concretar la
        comunicacion; si no lo logra, muere mostrando un error.
        """

        # Retiene el ejecución por el período seteado en timeout.
        time.sleep(self.configs['timeout'])

        if self.configs.get('sitra_debug'):
          print(
              colored(
                  "INTENTO {0}".format(counter_while), 
                  'blue', attrs=["reverse", "bold"]
              )
          )

        # código trama de envio
        codigo_trama_envio = self.ordenar_trama.get_codigo_trama(trama)
        # print('codigo_trama_envio', codigo_trama_envio)
        # código trama de respuesta
        codigo_trama_verificacion = ref.CONSULTA_RESPUESTA[
          codigo_trama_envio]
        # print('codigo_trama_verificacion', codigo_trama_verificacion)
        trama_respuesta = self.__send_lan(trama)

        ## código trama respuesta
        try:
          codigo_trama_respuesta = self.ordenar_trama.get_codigo_trama(
              trama_respuesta['trama_obtenida']
          )
        except KeyError:
          codigo_trama_respuesta = '00'

        # Validación
        if codigo_trama_respuesta != codigo_trama_verificacion and \
                counter_while <= self.configs['reintentos']:
          # La trama esta formada correctamente pero, no es el
          # código que corresponde a la consulta
          counter_while += 1
          continue
        elif trama_respuesta['success'] == 1:
          # La trama de respuesta es correcta. Corta la ejecución.
          break
        elif counter_while >= self.configs['reintentos']:
          # Se superó la cantidad de reintentos
          message_error = {
            'status': 4,
            'uuid' : self.configs['uuid'],
            'description': ref.MENSAJES[8]['mensaje'].format(
              self.configs['reintentos']
            ),
            'success': 0,
          }
          return message_error

        counter_while += 1

      # Si hay error finalizo la ejecución
      if trama_respuesta['success'] == 0:
        return trama_respuesta

      # Si no hubiera error collecciono las tramas
      data.append(trama_respuesta['trama_obtenida'])

      codigo = self.ordenar_trama.get_codigo_trama(trama)
      self.__archivoJson(
        crsid=self.configs['crs_id'],
        num=counter,
        cod=codigo,
        total=len(self.configs['tramas'])
      )

      counter += 1

    self.__proceso_finalizado()

    # Retronr una lista con las tramas
    return {'data': data, 'success': 1,'uuid':self.configs['uuid']}


  def __send_lan(self, tgm):
    """Conexión LAN
    """
    try:
      trama = []
      address = (
        str(self.configs['crs_ip']),
        int(self.configs['prt_puerto'])
      )
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(self.configs['timeout'])
      sock.connect(address)
      hex_string = tgm

      if self.configs.get('sitra_debug'):
        print(
            colored("ENVIA", 'cyan', attrs=["reverse", "bold"]),
            hex_string
        )

      for num in hex_string.split(): sock.sendall(bytearray.fromhex(num))

      time.sleep(self.configs.get('espera'))

      for x in sock.recv(2048): trama.append(hex(x))

      # sock.settimeout(None)
      sock.close()

      if self.configs.get('sitra_debug'):
        print(
            colored("RESPUESTA TRAMA BRUTA", 'cyan',
                    attrs=["reverse", "bold"]),
            trama
        )

      tramaProcesada = self.ordenar_trama.ordenarTrama(trama)

      # Debug
      if self.configs.get('sitra_debug'):
        print(
            colored(
                "RESPUESTA TRAMA PROCESADA",
                "cyan", attrs=["reverse", "bold"]
            ),
            tramaProcesada
        )
        print(
            colored(
                "VALIDA BCC", "cyan", attrs=["reverse", "bold"]
            ),
            self.validator.isValidBcc(tramaProcesada)
        )
        print("\n\n\n")


      if not self.validator.isValidBcc(tramaProcesada):
        return {
            'status'         : 5,
            'uuid'           : self.configs['uuid'],
            'description'    : ref.MENSAJES[9]['mensaje'],
            'trama_obtenida' : tramaProcesada,
            'success'        : 0
        }

      return {
          'uuid'             : self.configs['uuid'],
          'description'      : ref.MENSAJES[10]['mensaje'],
          'success'          : 1,
          'status'           : 1,
          'trama_obtenida'   : tramaProcesada,
      }

    except socket.timeout:
      if self.configs.get('sitra_debug'):
        print(
            colored(
                "TIMEOUT", "yellow", attrs=["reverse", "bold"]
            )
        )

      message = {
          'status'           : 2,
          'uuid'             : self.configs['uuid'],
          'description'      : ref.MENSAJES[1]['mensaje'],
          'success'          : 0,
      }
      return message

    except socket.error:
      if self.configs.get('sitra_debug'):
        print(
            colored(
                "ERROR DE CONEXION", "red", attrs=["reverse", "bold"]
            )
        )

      message = {
          'status'           : 3,
          'uuid'             : self.configs['uuid'],
          'description'      : ref.MENSAJES[11]['mensaje'],
          'success'          : 0,
      }
      return message


  def __proceso_finalizado(self):
    """Crea un archivo *.json con el porcentaje vacio
    """
    EMPTY_PROCESS = {
        'uuid'     : self.configs['uuid'],
        'per'      : 0,
        'crsid'    : self.configs['crs_id'],
        'cod'      : '0',
        'nombre'   : '',
        'datetime' : time.strftime('%Y-%m-%dT%H:%M:%S'),
    }
    self.__procentaje_proceso(EMPTY_PROCESS)


  def __procentaje_proceso(self, data):
    # Si el usuario no está logueado hace un redirect.
    try:
      self.mongo_db.proceso.update_one(
          {"_id": 1}, {"$set": {'data':data}}, upsert=True
      )
    except:
      print('problemas grabando en mongo')


  def __archivoJson(self, **kwargs):
    """Crea un archivo *.json con el porcentaje creado
    """
    porcentaje = round((kwargs['num'] * 100) / kwargs['total'])
    if not kwargs['cod']:
      cod = kwargs['cod']
    else:
      cod = '00'

    percent = {
        'uuid'     : self.configs['uuid'],
        'datetime' : time.strftime('%Y-%m-%dT%H:%M:%S'),
        'crsid'    : self.configs['crs_id'],
        'accion'   : 'captura',
        'per'      : porcentaje,
        'cod'      : kwargs['cod'],
        'nombre'   : ref.CODE_REFERENCES[kwargs['cod']]['humanize']
    }
    self.__procentaje_proceso(percent)


class TramaInvalida(Exception):
  pass


if __name__ == '__main__':
  from sitralib.generador_tramas_captura import *

  crs = {
    'crs_id': 17,
    'crs_numero': 3000,
    'crs_ip': '192.168.11.3',
    'prt_puerto': 1000,
    'grp_id_num': 1,
    'timeout': .4,
    'reintentos': 5,
    'porcentaje': '/Applications/MAMP/htdocs/bitbucket/sitra/sitra/estructura/static/estructura/data/porcentaje.json',
  }

  o = GeneradorTramasCaptura(**crs)
  tramas = o.create()

  # Ejecuta el capturador
  c = Captura(tramas=tramas, **crs)
  e = c.get()

  print(e)
