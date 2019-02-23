# -*- coding: utf-8 -*-
import sys


class ReporteEstado(object):
  def validar(self, trama):

    if not trama: return {}
    t = dict()

    byteDeStatus  = self.__obtenerByteStatus(trama)
    bitsDeStatusI = self.__obtenerBitsStatusI(trama)
    bitsDeAlarmas = self.__obtenerBitsAlarmas(trama)
    numeroDeCruce = self.__obtenerNumeroCruce(trama)

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

      # Incluyo las alertas en el diccionario de retorno
      t['alertas'] = alertas

      # Si la trama contempla propiedades de evaluación del
      # estado extendido
      if 'byte_lamparas' in trama:
        t.update(self.__prepararTrama(trama))
      return t

    return {}

  def __vector(self, bitsDeStatusI):
    if bitsDeStatusI['AP']['est']['val'] == None or int(
        bitsDeStatusI['TIT']['est']['val']) == 1:
      vector = 12

    elif int(bitsDeStatusI['AP']['est']['val']) == 1:

      if int(bitsDeStatusI['TIT']['est']['val']) == 0:
        vector = self.__estadoVector({
          'estado': bitsDeStatusI,
          'normal': 10,
          'apagado': 11
        })
      else:
        vector = 12

    else:
      vector = self.__estadoVector({
        'estado': bitsDeStatusI,
        'normal': 8,
        'apagado': 9
      })
    return vector

  def __prepararTrama(self, trama):
    """
    Remueve los indices innecesarios para mostrar el estado
    :return:
    """
    # trama.pop('byteDeStatus_a')
    trama.pop('byte_status_b')
    trama.pop('byte_status_c')
    trama.pop('bits_status_ii')
    trama.pop('bits_status_iii')
    trama.pop('object')
    trama.pop('bits_alarma')

    return trama

  def __obtenerAlarmas(self, data):
    '''
    Retorna los indices que reportan alarmas en bitsDeStatusI
    '''
    sys.exit(0)

  def __obtenerBitsStatusI(self, trama):
    '''
    Evalua la trama C8 ó C9 y obtiene la colección de datos para
    los bitsDeStatusI
    '''
    if 'bits_status_i' in trama:
      return trama['bits_status_i']

    return {}

  def __setAlertasBitsDeStatusI(self, trama):
    # Remuevo los indices que no evalúo
    new_trama = dict()
    if trama['PFL']['est']['val'] != 0:
      new_trama['PFL'] = trama['PFL']

    if trama['CP']['est']['val'] != 0:
      new_trama['CP'] = trama['CP']

    if trama['LP']['est']['val'] == 0:
      new_trama['LP'] = trama['LP']

    if trama['AP']['est']['val'] != 0:
      new_trama['AP'] = trama['AP']

    return new_trama

  def __obtenerByteStatus(self, trama):
    if 'byte_status_a' in trama:
      return trama['byte_status_a']

    return {}

  def __setAlertasByteDeStatus(self, trama):
    # Remuevo los indices que no evalúo
    if 'SIPLA' in trama:
      return {}

    return trama

  def __obtenerNumeroCruce(self, trama):
    '''
    Evalua la trama C8 ó C9 y obtiene el numero de cruce
    los bitsDeStatusI
    'numeroDeCruce': ['0B', 'B8'],
    '''
    if 'numero_cruce' in trama:
      return trama['numero_cruce']

    return {}

  def __obtenerBitsAlarmas(self, trama):
    '''
    Evalua la trama C8 ó C9 y obtiene la colección de datos para
    los bits de alarmas
    '''
    if 'bits_alarma' in trama:
      return trama['bits_alarma']

    return {}

  def __setAlertasBitsDeAlarmas(self, trama):
    # Remuevo los indices que no evalúo
    # trama.pop('TSUP', None)
    # trama.pop('BT', None)

    if trama['TSUP']['est']['val'] == 0:
      trama.pop('TSUP', None)

    if trama['BT']['est']['val'] == 0:
      trama.pop('BT', None)

    if trama['FR']['est']['val'] == 0:
      trama.pop('FR', None)

    if trama['CV']['est']['val'] == 0:
      trama.pop('CV', None)

    if trama['FV']['est']['val'] == 0:
      trama.pop('FV', None)

    if trama['GPS']['est']['val'] == 0:
      trama.pop('GPS', None)

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
        est = 5  # local

      return est

    return False

  def __estadoVector(self, opt):

    if len(opt) > 0:

      if 'estado' in opt:
        est = opt['estado']
      else:
        est = False

      if 'normal' in opt:
        normal = opt['normal']
      else:
        normal = False

      if 'apagado' in opt:
        apagado = opt['apagado']
      else:
        apagado = False

      if int(est['VP']['est']['val']) == 1:
        t = normal
      elif int(est['VP']['est']['val']) == 0:
        t = apagado

      return t


if __name__ == "__main__":
  pass
  # trama = {}
  # obj = ReporteEstado()
  # r = obj.validar(trama2)
  # import pprint
  #
  # pp = pprint
  # pp.pprint(r)
