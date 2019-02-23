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


class RespuestaEstadoEnvioComando(object):
  def __init__(self):
    self.helpers     = Helpers()
    self.bytSta      = ByteStatus()
    self.bitStaI     = BitsStatusI()
    self.bitStaII    = BitsStatusII()
    self.bitStaIII   = BitsStatusIII()
    self.bitAla      = BitsAlarma()
    self.validateBcc = Bcc()
    self.bytLamp     = ByteLamparas()
    self.fecha       = Fecha()
    self.bytFun      = ByteFuncion()

  def get(self, trm):

    if (self.validateBcc.isValidBcc(trm, 12, 90)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))

      # Lamparas
      byte_de_lamparas = dict()
      byte_de_lamparas.update({'mov1': self.bytLamp.byteLamparas(
        trm[20], hi=2, lo=1, mov=1)})
      byte_de_lamparas.update({'mov2': self.bytLamp.byteLamparas(
        trm[20], hi=2, lo=1, mov=2)})
      byte_de_lamparas.update({'mov3': self.bytLamp.byteLamparas(
        trm[21], hi=4, lo=3, mov=3)})
      byte_de_lamparas.update({'mov4': self.bytLamp.byteLamparas(
        trm[21], hi=4, lo=3, mov=4)})
      byte_de_lamparas.update({'mov5': self.bytLamp.byteLamparas(
        trm[22], hi=6, lo=5, mov=5)})
      byte_de_lamparas.update({'mov6': self.bytLamp.byteLamparas(
        trm[22], hi=6, lo=5, mov=6)})
      byte_de_lamparas.update({'mov7': self.bytLamp.byteLamparas(
        trm[23], hi=8, lo=7, mov=7)})
      byte_de_lamparas.update({'mov8': self.bytLamp.byteLamparas(
        trm[23], hi=8, lo=7, mov=8)})
      byte_de_lamparas.update({'mov9': self.bytLamp.byteLamparas(
        trm[24], hi=10, lo=9, mov=9)})
      byte_de_lamparas.update({'mov10': self.bytLamp.byteLamparas(
        trm[24], hi=10, lo=9, mov=10)})
      byte_de_lamparas.update({'mov11': self.bytLamp.byteLamparas(
        trm[25], hi=12, lo=11, mov=11)})
      byte_de_lamparas.update({'mov12': self.bytLamp.byteLamparas(
        trm[25], hi=12, lo=11, mov=12)})
      byte_de_lamparas.update({'mov13': self.bytLamp.byteLamparas(
        trm[26], hi=14, lo=13, mov=13)})
      byte_de_lamparas.update({'mov14': self.bytLamp.byteLamparas(
        trm[26], hi=14, lo=13, mov=14)})
      byte_de_lamparas.update({'mov15': self.bytLamp.byteLamparas(
        trm[27], hi=16, lo=15, mov=15)})
      byte_de_lamparas.update({'mov16': self.bytLamp.byteLamparas(
        trm[27], hi=16, lo=15, mov=16)})
      res.update({'byte_lamparas': byte_de_lamparas})

      res.update({
        'datetime': self.fecha.fecha(
          year=trm[28],
          month=trm[29],
          day=trm[30],
          hour=trm[31],
          minutes=trm[32],
          seconds=trm[33],
          wday=trm[34])
      })

      res.update({'desfasaje': self._joinNibblesCuad(trm[52], trm[53])})
      res.update(
        {'tiempo_real_2': self._joinNibblesCuad(trm[44], trm[45])})
      res.update({'estructura': self.helpers.hexToDec(trm[35])})
      res.update({'programa_tiempos': self.helpers.hexToDec(trm[36])})
      res.update({'byte_status_b': self.bytSta.byteStatus(trm[37])})
      res.update({'numero_paso': self.helpers.hexToDec(trm[38])})
      res.update({'segundo_paso': self.helpers.hexToDec(trm[39])})
      res.update({'byte_status_c': self.bytSta.byteStatus(trm[42])})
      res.update({'duracion_paso': self.helpers.hexToDec(trm[43])})

      res.update(self.bytFun.get(trm[54]))
      res.update({'object': 'respuestaEstadoEnvioComando'})

      return res
    else:
      return []

  def _joinNibbles(self, hex1, hex2):
    a = self.helpers.getNibbles(hex1)
    b = self.helpers.getNibbles(hex2)

    hexNum = '{0}{1}'.format(a['hi'], b['lo'])
    return self.helpers.hexToDec(hexNum)

  def _joinNibblesCuad(self, hex1, hex2):
    n = (self.helpers.hexToDec(hex1) * 256) + self.helpers.hexToDec(hex2)
    return n


if __name__ == "__main__":
  trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'C5', 10: '00', 11: '56',
       12: '6D', 13: '0B', 14: 'B8', 15: '00', 16: '14', 17: '00',
       18: '20', 19: '00', 20: '99', 21: '99', 22: 'DD', 23: 'DD',
       24: 'DD', 25: 'DD', 26: 'DD', 27: 'DD', 28: '01', 29: '60',
       30: '60', 31: '60', 32: '62', 33: '42', 34: '00', 35: '20',
       36: '00', 37: '00', 38: '00', 39: '20', 40: '50', 41: '00',
       42: '00', 43: '00', 44: '50', 45: '00', 46: 'F0', 47: '00',
       48: '00', 49: '01', 50: '40', 51: '00', 52: '00', 53: '00',
       54: '00', 55: '00', 56: '00', 57: '00', 58: '00', 59: '00',
       60: '00', 61: '00', 62: '00', 63: '00', 64: '00', 65: '00',
       66: '00', 67: '00', 68: '00', 69: '00', 70: '00', 71: '00',
       72: '00', 73: '00', 74: '00', 75: '00', 76: '00', 77: '00',
       78: '00', 79: '00', 80: '00', 81: '00', 82: '00', 83: '00',
       84: '00', 85: '00', 86: '00', 87: '00', 88: '00', 89: '00',
       90: '00', 91: '0E', 92: '50', 93: '00', 94: '00', 95: '00',
       96: '0F', 97: 'F0', 98: '00', 99: '00', 100: '01', 101: 'C5',
       102: '00', 103: '56', 104: '6D', 105: '0B', 106: 'B8', 107: '00',
       108: '14', 109: '00', 110: '20', 111: '00', 112: 'AA', 113: 'AA',
       114: 'DD', 115: 'DD', 116: 'DD', 117: 'DD', 118: 'DD', 119: 'DD',
       120: '16', 121: '06', 122: '00', 123: '60', 124: '62', 125: '42',
       126: '10', 127: '20', 128: '00', 129: '00', 130: '00', 131: '30',
       132: '10', 133: '00', 134: '00', 135: '00', 136: '50', 137: '01',
       138: '00', 139: '00', 140: '00', 141: '01', 142: '40', 143: '00',
       144: '00', 145: '00', 146: '00', 147: '00', 148: '00', 149: '00',
       150: '00', 151: '00', 152: '00', 153: '00', 154: '00', 155: '00',
       156: '00', 157: '00', 158: '00', 159: '00', 160: '00', 161: '00',
       162: '00', 163: '00', 164: '00', 165: '00', 166: '00', 167: '00',
       168: '00', 169: '00', 170: '00', 171: '00', 172: '00', 173: '00',
       174: '00', 175: '00', 176: '00', 177: '00', 178: '00', 179: '00',
       180: '00', 181: '00', 182: '00', 183: '0F', 184: '0E'}
  obj = RespuestaEstadoEnvioComando()
  retorno = obj.get(trama)
  #
  import pprint

  pp = pprint
  pp.pprint(retorno)
