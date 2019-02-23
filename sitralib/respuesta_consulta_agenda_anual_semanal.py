# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
# from sitralib.helpers.byte import *
# from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaConsultaAgendaAnualSemanal(object):
  """
  Trama de respuesta de consulta de agenda anual semanal desde EC hacia CC
  xD9
  """

  def __init__(self):
    self.helpers     = Helpers()
    self.bytSta      = ByteStatus()
    self.bitStaI     = BitsStatusI()
    self.bitStaII    = BitsStatusII()
    self.bitStaIII   = BitsStatusIII()
    self.bitAla      = BitsAlarma()
    self.validateBcc = Bcc()

  def get(self, trm):
    if (self.validateBcc.isValidBcc(trm, 12, 140)):

      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update(
        {'cambio': self.__set_agendas_anuales(trm)})
      res.update(
        {'agenda_diaria': self.__set_agendas_semanales(trm)})
      res.update({'object': 'respuestaConsultaAgendaAnualSemanal'})

      return res
    else:
      return []

  def __set_agendas_semanales(self, trm):
    """
    :param trm:
    :return:
    """

    contador = 1
    index = 0
    iter = list()

    for i in range(56, 140):
      if contador == 1:
        iter.append(dict())
        iter[index].update({'indice': index})
        iter[index].update({
          'domingo': self.helpers.hexToDec(trm[i])
        })
      if contador == 2:
        iter[index].update({
          'lunes': self.helpers.hexToDec(trm[i])
        })
      if contador == 3:
        iter[index].update({
          'martes': self.helpers.hexToDec(trm[i])
        })
      if contador == 4:
        iter[index].update({
          'miercoles': self.helpers.hexToDec(trm[i])
        })
      if contador == 5:
        iter[index].update({
          'jueves': self.helpers.hexToDec(trm[i])
        })
      if contador == 6:
        iter[index].update({
          'viernes': self.helpers.hexToDec(trm[i])
        })
      if contador == 7:
        iter[index].update({
          'sabado': self.helpers.hexToDec(trm[i])
        })
        # Reset counters
        contador = 0
        index += 1

      contador += 1

    return iter

  def __set_agendas_anuales(self, trm):

    contador = 1
    index = 0
    iter = list()

    for i in range(20, 44):
      if contador == 1:
        iter.append(dict())
        iter[index].update({'indice': index})
        iter[index].update({
          'dia': trm[i] if self.helpers.validateBetween(
            min=1, max=31, number=self.helpers.hexToDec(trm[i]))
          else False
        })

      if contador == 2:
        iter[index].update({
          'mes': trm[i] if self.helpers.validateBetween(
            min=1, max=12, number=self.helpers.hexToDec(trm[i]))
          else False
        })
        # Reset counters
        contador = 0
        index += 1

      contador += 1

    return iter


if __name__ == "__main__":
  help_text = """
  obj = RespuestaConsultaAgendaAnualSemanal()
  retorno = obj.respuestaConsultaAgendaAnualSemanal({5: 'FF', 6: '00', 8: ... })
  """
  print(help_text)

  trama = {5: 'FF', 6: '00', 7: '00', 8: '1E', 9: 'D9', 10: '00', 11: '88',
       12: 'B0', 13: '06', 14: '4A', 15: '01', 16: '14', 17: '00',
       18: '00', 19: '00', 20: '01', 21: '01', 22: '7F', 23: 'FF',
       24: '7F', 25: 'FF', 26: '7F', 27: 'FF', 28: '7F', 29: 'FF',
       30: '7F', 31: 'FF', 32: '7F', 33: 'FF', 34: '7F', 35: 'FF',
       36: '7F', 37: 'FF', 38: '7F', 39: 'FF', 40: '7F', 41: 'FF',
       42: '7F', 43: 'FF', 44: '00', 45: '01', 46: '02', 47: '03',
       48: '04', 49: '05', 50: '06', 51: '07', 52: '08', 53: '09',
       54: '0A', 55: '0B', 56: '00', 57: '00', 58: '00', 59: '00',
       60: '00', 61: '00', 62: '00', 63: '00', 64: '00', 65: '00',
       66: '00', 67: '00', 68: '00', 69: '00', 70: '00', 71: '00',
       72: '00', 73: '00', 74: '00', 75: '00', 76: '00', 77: '00',
       78: '00', 79: '00', 80: '00', 81: '00', 82: '00', 83: '00',
       84: '00', 85: '00', 86: '00', 87: '00', 88: '00', 89: '00',
       90: '00', 91: '00', 92: '00', 93: '00', 94: '00', 95: '00',
       96: '00', 97: '00', 98: '00', 99: '00', 100: '00', 101: '00',
       102: '00', 103: '00', 104: '00', 105: '00', 106: '00', 107: '00',
       108: '00', 109: '00', 110: '00', 111: '00', 112: '00', 113: '00',
       114: '00', 115: '00', 116: '00', 117: '00', 118: '00', 119: '00',
       120: '00', 121: '00', 122: '00', 123: '00', 124: '00', 125: '00',
       126: '00', 127: '00', 128: '00', 129: '00', 130: '00', 131: '00',
       132: '00', 133: '00', 134: '00', 135: '00', 136: '00', 137: '00',
       138: '00', 139: '00', 140: '69', 141: '00', 142: '00', 143: '00',
       144: '00', 145: 'FF', 146: '00', 147: '00', 148: '1E', 149: 'C9',
       150: '00', 151: '10', 152: '38', 153: '06', 154: '4A', 155: '01',
       156: '14', 157: '00', 158: '00', 159: '00', 160: '61'}
  obj = RespuestaConsultaAgendaAnualSemanal()
  retorno = obj.respuestaConsultaAgendaAnualSemanal(trama)
  #
  import pprint

  pp = pprint
  pp.pprint(retorno)
