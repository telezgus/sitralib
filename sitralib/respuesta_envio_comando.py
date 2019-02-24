# -*- coding: utf-8 -*-
from sitralib.validators.bcc import *
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *


class RespuestaEnvioComando:
  def __init__(self):
    self.helpers     = Helpers()
    self.bytSta      = ByteStatus()
    self.bitStaI     = BitsStatusI()
    self.bitStaII    = BitsStatusII()
    self.bitStaIII   = BitsStatusIII()
    self.bitAla      = BitsAlarma()
    self.validateBcc = Bcc()

  def get(self, trm):
    res = None
    r = {}

    if (self.validateBcc.isValidBcc(trm, 12, 20)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])}
      )
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update({'object': 'respuestaEnvioComando'})

    return res


if __name__ == '__main__':
  trm = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'C9', 10: '00', 11: '10',
       12: '27', 13: '0B', 14: 'B8', 15: '01', 16: '14', 17: '00', 18: '20',
       19: '00', 20: 'A1'}
  obj = RespuestaEnvioComando()
  retorno = obj.respuestaEnvioComando(trm)
  #

  import pprint

  pp = pprint
  pp.pprint(retorno)
