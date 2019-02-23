# -*- coding: utf-8 -*-
from sitralib.validators.bcc import *
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.byte_funcion import *
from sitralib.helpers.funciones import *


class RespuestaConsultaEstructuraParteBaja(object):
  """
  Trama de respuesta de consulta estructura (parte baja)
  0xCC
  """

  def __init__(self):
    self.helpers      = Helpers()
    self.bytSta       = ByteStatus()
    self.bitStaI      = BitsStatusI()
    self.bitStaII     = BitsStatusII()
    self.bitStaIII    = BitsStatusIII()
    self.bitAla       = BitsAlarma()
    self.byte_funcion = ByteFuncion()
    self.validateBcc  = Bcc()

  def __get_intervalos(self, trama):
    """
    Separa la colección de datos en intervalos.
    :param trama: dict
    :return: dict
    """
    counter = idx = 0
    mov = dict()
    values = list()

    for val in self.helpers.sliceDict(trama, min=21, max=254):
      if counter == 13:
        # Reseteo valores
        values = list()
        counter = 0
        # Incremento el indice
        idx += 1

      mov.update({idx: values})
      values.append(trama[val])
      counter += 1
    return mov

  def __movimientos_por_intervalo(self, trama_sliced):
    m = dict()
    est = dict()
    f = list()

    for val in trama_sliced:
      movimiento = dict()
      mov = trama_sliced[val]
      nibble = self.helpers.getNibbles(mov[0], 2)
      movimiento.update({
        1: nibble['lo'],
        2: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[1], 2)
      movimiento.update({
        3: nibble['lo'],
        4: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[2], 2)
      movimiento.update({
        5: nibble['lo'],
        6: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[3], 2)
      movimiento.update({
        7: nibble['lo'],
        8: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[4], 2)
      movimiento.update({
        9: nibble['lo'],
        10: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[5], 2)
      movimiento.update({
        11: nibble['lo'],
        12: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[6], 2)
      movimiento.update({
        13: nibble['lo'],
        14: nibble['hi'],
      })
      nibble = self.helpers.getNibbles(mov[7], 2)
      movimiento.update({
        15: nibble['lo'],
        16: nibble['hi'],
      })

      f.append(self.byte_funcion.get(mov[8]))
      m.update({val: movimiento})

    for i in range(18, 36):
      est.update({'intervalo_{0}'.format(i): m[i - 18]})

    est.update({'funcion': f})
    return est

  def get(self, trm):
    res = None

    if (self.validateBcc.isValidBcc(trm, 12, 255)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update({'estructura': self.helpers.hexToDec(trm[20])})
      res.update(
        self.__movimientos_por_intervalo(self.__get_intervalos(trm)))
      res.update({'object': 'RespuestaConsultaEstructuraParteAlta'})

    return res


if __name__ == '__main__':
  trm = {5: "FF", 6: "00", 7: "00", 8: "1E", 9: "CC", 10: "00", 11: "FB",
       12: "D6", 13: "06", 14: "41", 15: "01", 16: "94", 17: "00",
       18: "00", 19: "00", 20: "00", 21: "00", 22: "00", 23: "00",
       24: "00", 25: "00", 26: "00", 27: "00", 28: "00", 29: "00",
       30: "00", 31: "00", 32: "00", 33: "00", 34: "00", 35: "00",
       36: "00", 37: "00", 38: "00", 39: "00", 40: "00", 41: "00",
       42: "00", 43: "00", 44: "00", 45: "00", 46: "00", 47: "00",
       48: "00", 49: "00", 50: "00", 51: "00", 52: "00", 53: "00",
       54: "00", 55: "00", 56: "00", 57: "00", 58: "00", 59: "00",
       60: "00", 61: "00", 62: "00", 63: "00", 64: "00", 65: "00",
       66: "00", 67: "00", 68: "00", 69: "00", 70: "00", 71: "00",
       72: "00", 73: "00", 74: "00", 75: "00", 76: "00", 77: "00",
       78: "00", 79: "00", 80: "00", 81: "00", 82: "00", 83: "00",
       84: "00", 85: "00", 86: "00", 87: "00", 88: "00", 89: "00",
       90: "00", 91: "00", 92: "00", 93: "00", 94: "00", 95: "00",
       96: "00", 97: "00", 98: "00", 99: "00", 100: "00", 101: "00",
       102: "00", 103: "00", 104: "00", 105: "00", 106: "00", 107: "00",
       108: "00", 109: "00", 110: "00", 111: "00", 112: "00", 113: "00",
       114: "00", 115: "00", 116: "00", 117: "00", 118: "00", 119: "00",
       120: "00", 121: "00", 122: "00", 123: "00", 124: "00", 125: "00",
       126: "00", 127: "00", 128: "00", 129: "00", 130: "00", 131: "00",
       132: "00", 133: "00", 134: "00", 135: "00", 136: "00", 137: "00",
       138: "00", 139: "00", 140: "00", 141: "00", 142: "00", 143: "00",
       144: "00", 145: "00", 146: "00", 147: "00", 148: "00", 149: "00",
       150: "00", 151: "00", 152: "00", 153: "00", 154: "00", 155: "00",
       156: "00", 157: "00", 158: "00", 159: "00", 160: "00", 161: "00",
       162: "00", 163: "00", 164: "00", 165: "00", 166: "00", 167: "00",
       168: "00", 169: "00", 170: "00", 171: "00", 172: "00", 173: "00",
       174: "00", 175: "00", 176: "00", 177: "00", 178: "00", 179: "00",
       180: "00", 181: "00", 182: "00", 183: "00", 184: "00", 185: "00",
       186: "00", 187: "00", 188: "00", 189: "00", 190: "00", 191: "00",
       192: "00", 193: "00", 194: "00", 195: "00", 196: "00", 197: "00",
       198: "00", 199: "00", 200: "00", 201: "00", 202: "00", 203: "00",
       204: "00", 205: "00", 206: "00", 207: "00", 208: "00", 209: "00",
       210: "00", 211: "00", 212: "00", 213: "00", 214: "00", 215: "00",
       216: "00", 217: "00", 218: "00", 219: "00", 220: "00", 221: "00",
       222: "00", 223: "00", 224: "00", 225: "00", 226: "00", 227: "00",
       228: "00", 229: "AA", 230: "99", 231: "09", 232: "00", 233: "00",
       234: "00", 235: "00", 236: "00", 237: "00", 238: "00", 239: "00",
       240: "00", 241: "00", 242: "11", 243: "11", 244: "01", 245: "00",
       246: "00", 247: "00", 248: "00", 249: "00", 250: "00", 251: "00",
       252: "00", 253: "00", 254: "BB", 255: "84"}
  obj = RespuestaConsultaEstructuraParteBaja()
  retorno = obj.get(trm)

  import pprint

  pp = pprint
  pp.pprint(retorno)
