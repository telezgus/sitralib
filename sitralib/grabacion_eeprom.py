# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.validators.bcc import *
from sitralib.helpers.funciones import *

class GrabacionEeprom(object):
  """
  Trama SITAR 0xE2
  Trama de grabación de EEPROM desde CC hacia EC
  #bookmark105
  """

  def __init__(self):
    self.bytSta = ByteStatus()
    self.bitStaI = BitsStatusI()
    self.bitStaII = BitsStatusII()
    self.bitStaIII = BitsStatusIII()
    self.bitAla = BitsAlarma()
    self.validateBcc = Bcc()
    self.helpers = Helpers()

  def grabar(self, trm):
    res = None

    if (self.validateBcc.isValidBcc(trm, 12, 26)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(
        {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      res.update({'status_grabacion': trm[20]})
      res.update({'posicion_actual_grabacion_msb': trm[21]})
      res.update({'posicion_actual_grabacion_lsb': trm[22]})
      res.update({'posicion_final_memoria_msb': trm[23]})
      res.update({'posicion_final_memoria_lsb': trm[24]})
      res.update({'object': 'GrabacionEeprom'})

    return res
