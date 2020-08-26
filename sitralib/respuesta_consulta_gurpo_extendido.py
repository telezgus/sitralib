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


class RespuestaConsultaGrupoExtendido:
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

    if (self.validateBcc.isValidBcc(trm, 12, 58)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])}
      )
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
          year    = '20{}'.format(trm[28]),
          month   = trm[29],
          day     = trm[30],
          hour    = trm[31],
          minutes = trm[32],
          seconds = trm[33],
          wday    = trm[34])
      })

      res.update(
        {'desfasaje': self._joinNibblesCuad(trm[52], trm[53])}
      )
      res.update(
        {'tiempo_real_2': self._joinNibblesCuad(trm[44], trm[45])}
      )
      res.update({
        'tiempo_prescripto_2': self._joinNibblesCuad(
          trm[48],
          trm[49]
        )
      })
      res.update({'estructura': self.helpers.hexToDec(trm[35])})
      res.update({'programa_tiempos': self.helpers.hexToDec(trm[36])})
      res.update({'byte_status_b': self.bytSta.byteStatus(trm[37])})
      res.update({'numero_paso': self.helpers.hexToDec(trm[38])})
      res.update({'segundo_paso': self.helpers.hexToDec(trm[39])})
      res.update({'byte_status_c': self.bytSta.byteStatus(trm[42])})
      res.update({'duracion_paso': self.helpers.hexToDec(trm[43])})

      res.update(self.bytFun.get(trm[54]))
      res.update({'object': 'respuestaConsultaGrupoExtendido'})

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


if __name__ == '__main__':
  trm = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'C8', 10: '00', 11: '36',
       12: '00', 13: '0B', 14: 'B8', 15: '01', 16: '14', 17: '00',
       18: '20',
       19: '00', 20: '99', 21: '99', 22: 'DD', 23: 'DD', 24: 'DD',
       25: 'DD',
       26: 'DD', 27: 'DD', 28: '16', 29: '04', 30: '23', 31: '19',
       32: '21',
       33: '36', 34: '07', 35: '00', 36: '01', 37: '01', 38: '02',
       39: '02',
       40: '00', 41: '00', 42: '01', 43: '0A', 44: '00', 45: '16',
       46: '00',
       47: '00', 48: '00', 49: '28', 50: '00', 51: '00', 52: '00',
       53: '00',
       54: '00', 55: '00', 56: '00', 57: '00', 58: '8B'}
  obj = RespuestaConsultaGrupoExtendido()
  retorno = obj.respuestaConsultaGrupoExtendido(trm)
  #
  import pprint

  pp = pprint
  pp.pprint(retorno)
