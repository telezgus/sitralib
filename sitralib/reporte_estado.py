# -*- coding: utf-8 -*-
import sys


class ReporteEstado:
  def validar(self, trama):

    if not trama: return dict()
    t = dict()

    byteDeStatus     = self.__obtenerByteStatus(trama)
    bitsDeStatusI    = self.__obtenerBitsStatusI(trama)
    bitsDeAlarmas    = self.__obtenerBitsAlarmas(trama)
    bitsDeAlarmasII  = self.__obtenerBitsAlarmasII(trama)
    byteFalta        = self.__obtenerByteFalta(trama)
    byteConflicto    = self.__obtenerByteConflicto(trama)
    byteFaltaFusible = self.__obtenerByteFaltaFusible(trama)
    numeroDeCruce    = self.__obtenerNumeroCruce(trama)

    if trama:
      t['numero_cruce'] = numeroDeCruce
      t['bits_status_i'] = bitsDeStatusI
      t['byte_status'] = self.__obtenerByteStatus(trama)
      t['est'] = self.__estadoIndicador({'estado': bitsDeStatusI})
      t['vtr'] = self.__vector(bitsDeStatusI)

      # Agrupo las alertas
      alertas = dict()
      alertas.update({
        'byte_status': self.__setAlertasByteDeStatus(byteDeStatus)
      })

      alertas.update({
        'bits_status_i': self.__setAlertasBitsDeStatusI(bitsDeStatusI)
      })

      alertas.update({
        'bits_alarma': self.__setAlertasBitsDeAlarmas(bitsDeAlarmas)
      })

      alertas.update({
        'bits_alarma_ii': self.__setAlertasBitsDeAlarmasII(bitsDeAlarmasII)
      })


      alertas.update({
        'byte_falta': byteFalta
      })

      alertas.update({
        'byte_conflicto': byteConflicto
      })

      alertas.update({
        'byte_falta_fusible': byteFaltaFusible
      })

      # Incluyo las alertas en el diccionario de retorno
      t['alertas'] = alertas
            
      # Si la trama contempla propiedades de evaluación del
      # estado extendido
      if 'byte_lamparas' in trama:
        t.update(self.__prepararTrama(trama))
      return t

    return dict()


  def __data_validator(self, key, trama):
    return trama.get(key, dict()).get("est", dict()).get("val")


  def __vector(self, bitsDeStatusI):
    """Retorna el estado/color con el que se debe representar el vector
    en la pantalla de monitoreo.


    Arguments:
      bitsDeStatusI {dict} -- Respuesta de bitsDeStatusI

    Returns:
      [int] -- Número/codigo del color a utilizar
    """
    if bitsDeStatusI['AP']['est']['val'] == None or int(
        bitsDeStatusI['TIT']['est']['val']) == 1:
      vector = 12 # Apagado/inactivo

    # Si el cruce esta apagado
    elif int(bitsDeStatusI['AP']['est']['val']) == 1:

      # Si no es titilante.
      if int(bitsDeStatusI['TIT']['est']['val']) == 0:
        vector = self.__estadoVector({
          'estado'  : bitsDeStatusI,
          'normal'  : 10, # Verde oscuro
          'apagado' : 11  # Rojo oscuro
        })
      else:
        vector = 12 # Apagado/inactivo

    else:
      vector = self.__estadoVector({
        'estado'  : bitsDeStatusI,
        'normal'  : 8, # verde activo
        'apagado' : 9  # Rojo activo
      })
    return vector


  def __estadoVector(self, opt):
    est     = opt.get('estado')
    normal  = opt.get('normal')
    apagado = opt.get('apagado')

    if int(est['VP']['est']['val']) == 1:
      t = normal
    elif int(est['VP']['est']['val']) == 0:
      t = apagado

    return t


  def __prepararTrama(self, trama):
    """
    Remueve los indices innecesarios para mostrar el estado
    :return:
    """
    remove_list = [
        # 'byte_status_a',
        'byte_status_b',
        'byte_status_c',
        'bits_status_ii',
        'bits_status_iii',
        'object',
        'bits_alarma'
        
        'byte_falta_fusible',
        'byte_conflicto',
        'byte_falta',
        'byte_detector'
    ]

    for i in remove_list:
      trama.pop(i, None)

    return trama


  def __obtenerAlarmas(self, data):
    sys.exit(0)


  def __obtenerBitsStatusI(self, trama):
    return trama.get('bits_status_i', dict())


  def __setAlertasBitsDeStatusI(self, trama):

    new_trama = dict()

    if trama['PFL']['est']['val'] != 0:
      new_trama['PFL'] = trama['PFL']

    if trama['CP']['est']['val'] != 0:
      new_trama['CP'] = trama['CP']

    if trama['LP']['est']['val'] == 0:
      new_trama['LP'] = trama['LP']

    if trama['AP']['est']['val'] != 0:
      new_trama['AP'] = trama['AP']

    if trama['TIT']['est']['val'] != 0:
      new_trama['TIT'] = trama['TIT']

    return new_trama


  def __obtenerByteStatus(self, trama):
    return trama.get('byte_status_a', dict())


  def __obtenerByteFalta(self, trama):
    return trama.get('byte_falta', dict())


  def __obtenerByteConflicto(self, trama):
    return trama.get('byte_conflicto', dict())


  def __obtenerByteFaltaFusible(self, trama):
    return trama.get('byte_falta_fusible', dict())


  def __setAlertasByteDeStatus(self, trama):
    if 'SIPLA' in trama:
      return dict()

    return trama


  def __obtenerNumeroCruce(self, trama):
    return trama.get('numero_cruce', dict())


  def __obtenerBitsAlarmasII(self, trama):
    return trama.get('bits_alarma_ii', dict())


  def __obtenerBitsAlarmas(self, trama):
    return trama.get('bits_alarma', dict())


  def __setAlertasBitsDeAlarmas(self, trama):
    """Remuevo los indices que no evalúo
    """

    if self.__data_validator("TSUP", trama) == 0:
      trama.pop('TSUP', None)

    if self.__data_validator("FR", trama) == 0:
      trama.pop('FR', None)

    if self.__data_validator("CV", trama) == 0:
      trama.pop('CV', None)

    if self.__data_validator("FV", trama) == 0:
      trama.pop('FV', None)

    if self.__data_validator("GPS", trama) == 0:
      trama.pop('GPS', None)

    if self.__data_validator("PA", trama) == 0:
      trama.pop('PA', None)

    if self.__data_validator("BTT", trama) == 0:
      trama.pop('BTT', None)

    if self.__data_validator("BTT", trama)== 1:
      trama.pop('BTT', None)

    elif self.__data_validator("BTA", trama) == 0:
      trama.pop('BTA', None)

    return trama



  def __setAlertasBitsDeAlarmasII(self, trama):
    """
    Remuevo los indices que no evalúo

    'bits_alarma_ii': {'CLAG': {'des': 'Cambio Local Agendas',
                             'est': {'des': 'Normal', 'val': 0}},
                    'CLCO': {'des': 'Cambio Local Configuracion',
                             'est': {'des': 'Normal', 'val': 0}},
                    'CLPR': {'des': 'Cambio Local Programas',
                             'est': {'des': 'Normal', 'val': 0}},
                    'ERTC': {'des': 'Error Seg RTC',
                             'est': {'des': 'Normal', 'val': 0}},
                    'MEEX': {'des': 'Modo Emergencia Externo',
                             'est': {'des': 'Normal', 'val': 0}},
                    'MMEX': {'des': 'Modo Manual Externo',
                             'est': {'des': 'Normal', 'val': 0}},
                    'PMMX': {'des': 'Pulso del Modo Manual Externo',
                             'est': {'des': 'Normal', 'val': 0}},
                    'PPPC': {'des': 'Programacion por PC',
                             'est': {'des': 'Normal', 'val': 0}}},
    """


    if self.__data_validator("CLAG", trama) == 0:
      trama.pop('CLAG', None)

    if self.__data_validator("CLCO", trama) == 0:
      trama.pop('CLCO', None)

    if self.__data_validator("CLPR", trama) == 0:
      trama.pop('CLPR', None)

    if self.__data_validator("ERTC", trama) == 0:
      trama.pop('ERTC', None)

    if self.__data_validator("MEEX", trama) == 0:
      trama.pop('MEEX', None)

    if self.__data_validator("MMEX", trama) == 0:
      trama.pop('MMEX', None)

    if self.__data_validator("PMMX", trama) == 0:
      trama.pop('PMMX', None)

    if self.__data_validator("PMMX", trama)== 1:
      trama.pop('PMMX', None)

    elif self.__data_validator("PPPC", trama) == 0:
      trama.pop('PPPC', None)

    return trama




  def __estadoIndicador(self, data):
    if len(data) > 0:

      if 'estado' in data:
        est = data['estado']
      else:
        est = False

      if self.__data_validator("AP", data) == 1:
        est = 7  # Negro / apagado
      elif self.__data_validator("TIT", data) == 1:
        est = 4  # Amarillo / titilante
      elif self.__data_validator("C", data) == 1:
        est = 6  # Azul / Comunicado
      elif self.__data_validator("C", data) == 0:
        est = 13  # Azul con raya / Local
      else:
        est = 5  # local / Color naranja

      return est

    return False



if __name__ == "__main__":
  import pprint as pp
  from sitralib.respuesta import *
  resp = Respuesta()

  trama = "FF 17 00 00 C9 00 10 31 05 0C 00 D0 00 00 00 E8"
  trama1 = "00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 14 00 00 00 EE EE EE EE EE EE 1E 00 19 07 10 12 50 11 04 00 00 00 08 01 00 00 00 05 00 29 00 00 00 2D 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 95"
  trama2 = """FF 00 00 01 C5 00 56 6D 0B BD 00 14 00 20 00 11 00 00 00 00 00 00 00
          21 11 23 08 36 00 03 00 00 00 02 0F 00 00 00 48 00 3D 00 00 00 78 00
          00 00 2B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
          00 00 00 00 00 00 00 20 1E 00 00 00 00 00 00 00 C5"""
  t = resp.obtenerRespuesta(trama2)

  reporte_estado = ReporteEstado()
  reporte_validado = reporte_estado.validar(t)
  pp.pprint(reporte_validado)
