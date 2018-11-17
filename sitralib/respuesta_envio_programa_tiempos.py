# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_funcion import *
from sitralib.byte_lamparas import *
from sitralib.byte_status import *
from sitralib.helpers.byte import *
from sitralib.helpers.fecha import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaEnvioProgramaTiempos(object):
  """
  Trama de respuesta de envío de programa de tiempos desde EC hacia CC
  xD5
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bytSta = ByteStatus()
    self.bitStaI = BitsStatusI()
    self.bitStaII = BitsStatusII()
    self.bitStaIII = BitsStatusIII()
    self.bitAla = BitsAlarma()
    self.validateBcc = Bcc()
    self.bytLamp = ByteLamparas()
    self.fecha = Fecha()
    self.bytFun = ByteFuncion()

  def get(self, trm):
    if (self.validateBcc.isValidBcc(trm, 12, 81)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])
      })
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update(
        {'numero_programa': self.helpers.hexToDec(trm[20])})
      res.update(
        {'duracion_ciclo': self.__get_duracion_ciclo(trm)})
      res.update(
        {'tiempo_suplementario': self.__get_tiempo_suplementario(trm)})
      res.update(
        {'desfasaje': self.__get_desfasaje(trm)})
      res.update(
        {'tiempos_intervalo': self.__get_tiempos_intervalo(trm)})
      res.update({'object': 'respuestaEnvioProgramaTiempos'})

      return res
    else:
      return []

  def __get_tiempos_intervalo(self, trm):
    """
    Obtiene los intervalos de tiempo
    :param self:
    :param trm: Trama D5
    :return: listado de tiempos
    """
    t = [self.helpers.hexToDec(trm[i]) for i in range(21, 57)]
    return t

  def __get_duracion_ciclo(self, trm):
    """
    Retorna la duracion del ciclo
    :param self:
    :param trm: Trama
    :return: numero decimal
    """
    msb = trm[57]
    lsb = trm[58]
    valor = msb + lsb
    return self.helpers.hexToDec(valor)

  def __get_tiempo_suplementario(self, trm):
    """
    Retorna la duracion del ciclo
    :param self:
    :param trm: Trama
    :return: numero decimal
    """
    msb = trm[59]
    lsb = trm[60]
    valor = msb + lsb
    return self.helpers.hexToDec(valor)

  def __get_desfasaje(self, trm):
    """
    Retorna la duracion del ciclo
    :param self:
    :param trm: Trama
    :return: numero decimal
    """
    msb = trm[61]
    lsb = trm[62]
    valor = msb + lsb
    return self.helpers.hexToDec(valor)


if __name__ == "__main__":
  help_text = """
  obj = RespuestaEnvioProgramaTiempos()
  retorno = obj.respuestaEnvioProgramaTiempos({5: 'FF', 6: '00', 8: ... })
  """
  print(help_text)

  trama = {5: 'FF', 6: '00', 7: '00', 8: '1E', 9: 'D5', 10: '00', 11: '4D',
       12: '79', 13: '06', 14: '4A', 15: '01', 16: '94', 17: '00',
       18: '00', 19: '00', 20: '00', 21: '14', 22: '17', 23: '03',
       24: '02', 25: '0A', 26: '0F', 27: '03', 28: '02', 29: '02',
       30: '00', 31: '00', 32: '00', 33: '00', 34: '00', 35: '00',
       36: '00', 37: '00', 38: '00', 39: '00', 40: '00', 41: '00',
       42: '00', 43: '00', 44: '00', 45: '00', 46: '00', 47: '00',
       48: '00', 49: '00', 50: '00', 51: '00', 52: '00', 53: '00',
       54: '00', 55: '05', 56: '05', 57: '00', 58: '50', 59: '00',
       60: 'A0', 61: '00', 62: '1E', 63: '7F', 64: 'FF', 65: '7F',
       66: 'FF', 67: '7F', 68: 'FF', 69: '7F', 70: 'FF', 71: '7F',
       72: 'FF', 73: '7F', 74: 'FF', 75: '7F', 76: 'FF', 77: '7F',
       78: 'FF', 79: '7F', 80: '00', 81: '35', 82: '00', 83: '00',
       84: '00', 85: '00', 86: 'FF', 87: '00', 88: '00', 89: '1E',
       90: 'C9', 91: '00', 92: '10', 93: '38', 94: '06', 95: '4A',
       96: '01', 97: '94', 98: '00', 99: '00', 100: '00', 101: 'E1'}
  obj = RespuestaEnvioProgramaTiempos()
  retorno = obj.respuestaEnvioProgramaTiempos(trama)
  #
  import pprint

  pp = pprint
  pp.pprint(retorno)
