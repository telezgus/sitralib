# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


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

      res = {'byte_status_a': self.bytSta.byteStatus(trama_ordenada.get(15))}
      res.update(self.bitStaI.bitsStatusI(trama_ordenada.get(16)))
      res.update(self.bitStaII.bitsStatusII(trama_ordenada.get(17)))
      res.update(self.bitAla.bitsAlarma(trama_ordenada.get(18)))
      res.update(self.bitStaIII.bitsStatusIII(trama_ordenada.get(19)))
      # Valor de espira
      res.update(self.__espira(1, trama_ordenada.get(20)))
      res.update(self.__espira(2, trama_ordenada.get(21)))
      res.update(self.__espira(3, trama_ordenada.get(22)))
      res.update(self.__espira(4, trama_ordenada.get(23)))
      res.update(self.__espira(5, trama_ordenada.get(24)))
      res.update(self.__espira(6, trama_ordenada.get(25)))
      res.update(self.__espira(7, trama_ordenada.get(26)))
      res.update(self.__espira(8, trama_ordenada.get(27)))
      # Tiempo de ocupacion
      res.update(self.__ocupacion(1, trama_ordenada.get(28)))
      res.update(self.__ocupacion(2, trama_ordenada.get(29)))
      res.update(self.__ocupacion(3, trama_ordenada.get(30)))
      res.update(self.__ocupacion(4, trama_ordenada.get(31)))
      res.update(self.__ocupacion(5, trama_ordenada.get(32)))
      res.update(self.__ocupacion(6, trama_ordenada.get(33)))
      res.update(self.__ocupacion(7, trama_ordenada.get(34)))
      res.update(self.__ocupacion(8, trama_ordenada.get(35)))
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
  trama5 = ['0x0', '0x0', '0x0', '0x0', '0xff', '0x0', '0x0', '0x1e', '0xe0',
            '0x0', '0x21', '0x20', '0x6', '0x49', '0x1', '0x94', '0x0', '0x0',
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0x3c', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0xc6', '0x0', '0x0', '0x0', '0x0', '0xff', '0x0', '0x0', '0x1e',
            '0xc5', '0x0', '0x56', '0x72', '0x6', '0x49', '0x1', '0x94', '0x0',
            '0x0', '0x0', '0x44', '0x1', '0x0', '0x0', '0xdd', '0xdd', '0xdd',
            '0xdd', '0x19', '0x4', '0x2', '0x4', '0x34', '0x27', '0x3', '0x0',
            '0x1', '0x1', '0x0', '0x1', '0x0', '0x0', '0x1', '0x18', '0x0',
            '0x1', '0x0', '0x0', '0x0', '0x50', '0x0', '0x0', '0x0', '0x1e',
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0',
            '0xb1']
  trama = trama5
  respuestaPuestoConteo = RespuestaConsultaPuestoConteo()


  retorno = respuestaPuestoConteo.get(trama)
  pp.pprint(retorno)
