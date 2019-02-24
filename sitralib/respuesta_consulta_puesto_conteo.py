# -*- coding: utf-8 -*-
from sitralib.validators.bcc import *
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *


class RespuestaConsultaPuestoConteo:
  def __init__(self):
    self.helpers       = Helpers()
    self.bytSta        = ByteStatus()
    self.bitStaI       = BitsStatusI()
    self.bitStaII      = BitsStatusII()
    self.bitStaIII     = BitsStatusIII()
    self.bitAla        = BitsAlarma()
    self.validateBcc   = Bcc()
    self.ordenar_trama = OrdenarTrama()

  def get(self, trm):
    res = None
    trama_ordenada = self.ordenar_trama.ordenarTrama(trm)

    if self.validateBcc.isValidBcc(trama_ordenada)\
          and trama_ordenada.get(9) == 'E0':

      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      # Valor de espira
      res.update(self.__espira(1, trm[20]))
      res.update(self.__espira(2, trm[21]))
      res.update(self.__espira(3, trm[22]))
      res.update(self.__espira(4, trm[23]))
      res.update(self.__espira(5, trm[24]))
      res.update(self.__espira(6, trm[25]))
      res.update(self.__espira(7, trm[26]))
      res.update(self.__espira(8, trm[27]))
      # Tiempo de ocupacion
      res.update(self.__ocupacion(1, trm[28]))
      res.update(self.__ocupacion(2, trm[29]))
      res.update(self.__ocupacion(3, trm[30]))
      res.update(self.__ocupacion(4, trm[31]))
      res.update(self.__ocupacion(5, trm[32]))
      res.update(self.__ocupacion(6, trm[33]))
      res.update(self.__ocupacion(7, trm[34]))
      res.update(self.__ocupacion(8, trm[35]))
      res.update({'object': 'RespuestaConsultaPuestoConteo'})

    return res


  def __espira(self, numero, valor):
    a = {
      'espira{0}'.format(numero): {
        'des': 'espira {0}'.format(numero),
        'val': int(valor, 16),
      }
    }
    return a


  def __ocupacion(self, numero, valor):
    b = {
      'ocupacion{0}'.format(numero): {
        'des': 'ocupación {0}'.format(numero),
        'val': int(valor, 16),
      }
    }
    return b



if __name__ == "__main__":
  from sitralib.helpers.ordenar_trama import *
  import pprint
  pp = pprint.PrettyPrinter(indent=4, width=200, depth=8, compact=True)
  #
  trama1 = ('00 00 00 00 FF 01 00 01 E1 00 21 3E 1B BB 01 D0 00 00 00 00 00 00 '
           '00 00 00 00 00 00 00 00 00 00 00 00 00 FF B0')
  trama2 = ('00 00 00 00 FF 01 00 01 E0 00 21 3E 1B BB F0 51 01 02 01 00 00 00 '
           '00 00 00 00 00 00 00 00 00 00 00 00 00 00 3D')
  trama3 = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'E0', 10: '00', 11: '21', 
            12: '3F', 13: '0B', 14: 'B8', 15: '00', 16: '14', 17: '00', 
            18: '20', 19: '00', 20: '01', 21: '02', 22: '03', 23: '04', 
            24: '05', 25: '06', 26: '07', 27: '08', 28: '0A', 29: '0B', 
            30: '0C', 31: '0D', 32: '0E', 33: '0F', 34: '10', 35: '11', 
            36: '00', 37: 'B0'}
  trama4 = '00 00 00 00 FF 00 00 01 71 00 0C 83 0B B8 00 30'
  trama5 = ['0x0', '0x0', '0x0', '0x0', '0xff', '0x0', '0x0', '0x1', '0xe0', 
            '0x0', '0x21', '0x3f', '0xb', '0xb8', '0x3', '0x94', '0x0', 
            '0x20', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', 
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', 
            '0x0', '0x3b']
  trama = trama5
  b = Bcc()

  print(b.isValidBcc(trama))
  print(trama, end='\n\n')

  respuestaPuestoConteo = RespuestaConsultaPuestoConteo()
  ot = OrdenarTrama()

  tramaOrdenada = ot.ordenarTrama(trama)

  retorno = respuestaPuestoConteo.get(tramaOrdenada)
  pp.pprint(retorno)
