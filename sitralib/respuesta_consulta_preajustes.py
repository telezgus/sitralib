from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.validators.bcc import *


class RespuestaConsultaPreajustes(object):
  """
  Trama de consulta de preajustes desde EC hacia CC
  0xD3
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
    if (self.validateBcc.isValidBcc(trm)):
      res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
      res.update(self.bitStaI.bitsStatusI(trm[16]))
      res.update(self.bitStaII.bitsStatusII(trm[17]))
      res.update(self.bitAla.bitsAlarma(trm[18]))
      res.update(self.bitStaIII.bitsStatusIII(trm[19]))
      # Valor de espira
      res.update({'grupo': self.helpers.hexToDec(trm[23])})
      res.update({'demandas': trm[42]})
      res.update({'sistema_operativo': 'P0{0}'.format(trm[90])})
      res.update({
        'sistema_operativo_version': '{0}.{1}'.format(
          trm[91][0],
          trm[91][1]
        )
      })
      res.update({'object': 'RespuestaConsultaPreajustes'})

    return res


if __name__ == "__main__":
  from sitralib.helpers.ordenar_trama import *
  import pprint

  #
  trama = {5: 'FF', 6: '00', 7: '00', 8: '1E', 9: 'D3', 10: '00', 11: '58',
       12: '6A', 13: '06', 14: '4A', 15: '01', 16: '14', 17: '00',
       18: '00', 19: '00', 20: '00', 21: '01', 22: '00', 23: '1E',
       24: '06', 25: '4A', 26: '00', 27: '00', 28: '00', 29: '00',
       30: '00', 31: '00', 32: '00', 33: '00', 34: '00', 35: '00',
       36: '00', 37: '00', 38: '00', 39: '00', 40: '00', 41: '00',
       42: '00', 43: '00', 44: '00', 45: '00', 46: '00', 47: '00',
       48: '00', 49: '00', 50: '7F', 51: '00', 52: '7F', 53: '00',
       54: '7F', 55: '00', 56: '7F', 57: '00', 58: '7F', 59: '00',
       60: '7F', 61: '00', 62: '7F', 63: '00', 64: '7F', 65: '00',
       66: '7F', 67: '00', 68: '7F', 69: '00', 70: '00', 71: '00',
       72: '00', 73: '00', 74: '00', 75: '00', 76: '00', 77: '00',
       78: '00', 79: '00', 80: '00', 81: '00', 82: '00', 83: '00',
       84: '00', 85: '00', 86: '00', 87: '00', 88: '00', 89: '00',
       90: '05', 91: '90', 92: 'F5', 93: '00', 94: '00', 95: '00',
       96: '00', 97: 'FF', 98: '00', 99: '00', 100: '1E', 101: 'C9',
       102: '00', 103: '10', 104: '38', 105: '06', 106: '4A', 107: '01',
       108: '14', 109: '00', 110: '00', 111: '00', 112: '61'}
  #
  respuestaPuestoConteo = RespuestaConsultaPreajustes()
  ot = OrdenarTrama()

  retorno = respuestaPuestoConteo.get(trama)
  pp = pprint.PrettyPrinter()
  pp.pprint(retorno)
