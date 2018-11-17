# -*- coding: utf-8 -*-
from sitralib.validators.bcc import *
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *


class RespuestaConsultaMatrizConflictos(object):
  """
  Trama de respuesta a consulta de matriz de conflictos desde EC hacia CC
  0xCF
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
    res = None

    if (self.validateBcc.isValidBcc(trm, 12, 50)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])}
      )
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update({'estructura': self.helpers.hexToDec(trm[20])})
      res.update({'object': 'RespuestaConsultaMatrizConflictos'})

    return res


if __name__ == '__main__':
  trm = {
    5: "FF", 6: "00", 7: "00", 8: "1E", 9: "CF", 10: "00", 11: "2E",
    12: "00", 13: "06", 14: "41", 15: "01", 16: "94", 17: "00",
    18: "00", 19: "00", 20: "00", 21: "00", 22: "00", 23: "00",
    24: "00", 25: "00", 26: "00", 27: "00", 28: "00", 29: "00",
    30: "00", 31: "00", 32: "00", 33: "00", 34: "00", 35: "00",
    36: "00", 37: "00", 38: "00", 39: "00", 40: "00", 41: "00",
    42: "00", 43: "00", 44: "00", 45: "00", 46: "00", 47: "00",
    48: "00", 49: "00", 50: "D2"
  }

  obj = RespuestaConsultaMatrizConflictos()
  retorno = obj.get(trm)

  import pprint

  pp = pprint
  pp.pprint(retorno)
