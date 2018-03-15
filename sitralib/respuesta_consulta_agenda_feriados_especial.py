from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaConsultaAgendaFeriadosEspecial(object):
  """
  Tabla 4.49:
    Trama de respuesta de agenda de feriados y especial desde EC hacia CC
  0xD7
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bytSta = ByteStatus()
    self.bitStaI = BitsStatusI()
    self.bitStaII = BitsStatusII()
    self.bitStaIII = BitsStatusIII()
    self.bitAla = BitsAlarma()
    self.validateBcc = Bcc()

  def get(self, trm):
    if (self.validateBcc.isValidBcc(trm, 12, 164)):

      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update(
        {'feriados': self.__set_feriados(trm)})
      res.update(
        {'especiales': self.__set_eventos_especiales(trm)})
      res.update({'object': 'RespuestaConsultaAgendaFeriadosEspecial'})

      return res
    else:
      return []

  def __get_feriados_planes(self, trm):
    """
    Obtiene los planes para los eventos especiales.
    """
    index = 132
    a = list()
    for i in range(0, 32):
      a.append(trm[index])
      index += 1
    return a

  def __get_eventos_especiales_planes(self, trm):
    """
    Obtiene los planes para los eventos especiales.
    """
    index = 116
    a = list()
    for i in range(0, 16):
      a.append(trm[index])
      index += 1

    return a

  def __set_feriados(self, trm):
    """
    Obtiene la información para cada agenda
    """
    feriados = self.__get_feriados_planes(trm)
    iter = list()
    contador = 1
    index = 0

    for i in range(52, 116):
      if contador == 1:
        iter.append(dict())
        iter[index].update({'indice': index})
        iter[index].update({'dia': trm[i]})

      if contador == 2:
        iter[index].update({'mes': trm[i]})
        iter[index].update({'adi_id': feriados[index]})
        # Reset
        contador = 0
        index += 1

      contador += 1

    return iter

  def __set_eventos_especiales(self, trm):
    """
    Obtiene la información para cada agenda
    :return:
    """
    planes = self.__get_eventos_especiales_planes(trm)

    iter = list()
    contador = 1
    index = 0

    for i in range(20, 52):
      if contador == 1:
        iter.append(dict())
        iter[index].update({'indice': index})
        iter[index].update({'dia': trm[i]})

      if contador == 2:
        iter[index].update({'mes': trm[i]})
        iter[index].update({'adi_id': planes[index]})
        # Reset
        contador = 0
        index += 1

      contador += 1

    return iter


if __name__ == "__main__":
  help_text = """
  obj = RespuestaConsultaAgendaFeriadosEspecial()
  retorno = obj.RespuestaConsultaAgendaFeriadosEspecial(
            {5: 'FF', 6: '00', 8: ... })
  """
  print(help_text)

  trama = {5: 'FF', 6: '00', 7: '00', 8: '1E', 9: 'D7', 10: '00', 11: 'A0',
       12: '96', 13: '06', 14: '4A', 15: '01', 16: '14', 17: '00',
       18: '00', 19: '00', 20: '7F', 21: 'FF', 22: '7F', 23: 'FF',
       24: '7F', 25: 'FF', 26: '7F', 27: 'FF', 28: '7F', 29: 'FF',
       30: '7F', 31: 'FF', 32: '7F', 33: 'FF', 34: '7F', 35: 'FF',
       36: '7F', 37: 'FF', 38: '7F', 39: 'FF', 40: '7F', 41: 'FF',
       42: '7F', 43: 'FF', 44: '7F', 45: 'FF', 46: '7F', 47: 'FF',
       48: '7F', 49: 'FF', 50: '7F', 51: 'FF', 52: '7F', 53: 'FF',
       54: '7F', 55: 'FF', 56: '7F', 57: 'FF', 58: '7F', 59: 'FF',
       60: '7F', 61: 'FF', 62: '7F', 63: 'FF', 64: '7F', 65: 'FF',
       66: '7F', 67: 'FF', 68: '7F', 69: 'FF', 70: '7F', 71: 'FF',
       72: '7F', 73: 'FF', 74: '7F', 75: 'FF', 76: '7F', 77: 'FF',
       78: '7F', 79: 'FF', 80: '7F', 81: 'FF', 82: '7F', 83: 'FF',
       84: '7F', 85: 'FF', 86: '7F', 87: 'FF', 88: '7F', 89: 'FF',
       90: '7F', 91: 'FF', 92: '7F', 93: 'FF', 94: '7F', 95: 'FF',
       96: '7F', 97: 'FF', 98: '7F', 99: 'FF', 100: '7F', 101: 'FF',
       102: '7F', 103: 'FF', 104: '7F', 105: 'FF', 106: '7F', 107: 'FF',
       108: '7F', 109: 'FF', 110: '7F', 111: 'FF', 112: '7F', 113: 'FF',
       114: '7F', 115: 'FF', 116: '00', 117: '00', 118: '00', 119: '00',
       120: '00', 121: '00', 122: '00', 123: '00', 124: '00', 125: '00',
       126: '00', 127: '00', 128: '00', 129: '00', 130: '00', 131: '00',
       132: '00', 133: '00', 134: '00', 135: '00', 136: '00', 137: '00',
       138: '00', 139: '00', 140: '00', 141: '00', 142: '00', 143: '00',
       144: '00', 145: '00', 146: '00', 147: '00', 148: '00', 149: '00',
       150: '00', 151: '00', 152: '00', 153: '00', 154: '00', 155: '00',
       156: '00', 157: '00', 158: '00', 159: '00', 160: '00', 161: '00',
       162: '00', 163: '00', 164: 'CF'}
  obj = RespuestaConsultaAgendaFeriadosEspecial()
  retorno = obj.respuestaConsultaAgendaFeriadosEspecial(trama)
  #
  import pprint

  pp = pprint
  pp.pprint(retorno)
