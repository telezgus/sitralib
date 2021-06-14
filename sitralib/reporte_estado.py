# -*- coding: utf-8 -*-
import sys


class ReporteEstado:
  def validar(self, trama):

    if not trama: return dict()
    t = dict()

    byteDeStatus     = self.__obtenerByteStatus(trama)
    bitsDeStatusI    = self.__obtenerBitsStatusI(trama)
    bitsDeAlarmas    = self.__obtenerBitsAlarmas(trama)
    byteFalta        = self.__obtenerByteFalta(trama)
    byteConflicto    = self.__obtenerByteConflicto(trama)
    byteFaltaFusible = self.__obtenerByteFaltaFusible(trama)
    numeroDeCruce    = self.__obtenerNumeroCruce(trama)

    if trama:
      t['numero_cruce'] = numeroDeCruce
      t['bits_status_i'] = bitsDeStatusI
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


  def __obtenerBitsAlarmas(self, trama):
    return trama.get('bits_alarma', dict())


  def __setAlertasBitsDeAlarmas(self, trama):
    # Remuevo los indices que no evalúo

    if trama['TSUP']['est']['val'] == 0:
      trama.pop('TSUP', None)

    if trama['FR']['est']['val'] == 0:
      trama.pop('FR', None)

    if trama['CV']['est']['val'] == 0:
      trama.pop('CV', None)

    if trama['FV']['est']['val'] == 0:
      trama.pop('FV', None)

    if trama['GPS']['est']['val'] == 0:
      trama.pop('GPS', None)

    if trama['PA']['est']['val'] == 0:
      trama.pop('PA', None)

    if trama['BTT']['est']['val'] == 0:
      trama.pop('BTT', None)

    if trama['BTA']['est']['val'] == 1:
      trama.pop('BTT', None)
    elif trama['BTA']['est']['val'] == 0:
      trama.pop('BTA', None)

    return trama


  def __estadoIndicador(self, data):
    if len(data) > 0:

      if 'estado' in data:
        est = data['estado']
      else:
        est = False

      if int(est['AP']['est']['val']) == 1:
        est = 7  # apagado
      elif int(est['TIT']['est']['val']) == 1:
        est = 4  # titilante
      elif int(est['C']['est']['val']) == 1:
        est = 6  # centralizado
      else:
        est = 5  # local / Color naranja

      return est

    return False




if __name__ == "__main__":
  import pprint as pp
  from sitralib.respuesta import *
  resp = Respuesta()
  
  trama = """FF 00 00 01 C5 00 60 5B 0B B4 F2 94 00 20 00 14 11 00 00 DD DD DD DD
21 06 01 17 49 28 02 00 04 F2 00 1E 00 00 F2 2B 00 1E 00 00 00 78 00
00 00 2B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 89"""
  
  t = resp.obtenerRespuesta(trama)

  reporte_estado = ReporteEstado()
  reporte_validado = reporte_estado.validar(t)
  pp.pprint(reporte_validado)
