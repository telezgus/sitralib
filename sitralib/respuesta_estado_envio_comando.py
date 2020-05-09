# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_falta import *
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


class RespuestaEstadoEnvioComando:
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
    self.bits_falta  = BitsFalta()



  def get(self, trm):

    if self.validateBcc.isValidBcc(trm, 12, 90):
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
          year    =trm[28],
          month   =trm[29],
          day     =trm[30],
          hour    =trm[31],
          minutes =trm[32],
          seconds =trm[33],
          wday    =trm[34])
      })

      res.update({'desfasaje': self._joinNibblesCuad(trm[52], trm[53])})
      res.update({'tiempo_real_2': self._joinNibblesCuad(trm[44], trm[45])})
      res.update({'estructura': self.helpers.hexToDec(trm[35])})
      res.update({'programa_tiempos': self.helpers.hexToDec(trm[36])})
      res.update({'byte_status_b': self.bytSta.byteStatus(trm[37])})
      res.update({'numero_paso': self.helpers.hexToDec(trm[38])})
      res.update({'segundo_paso': self.helpers.hexToDec(trm[39])})
      res.update({'byte_status_c': self.bytSta.byteStatus(trm[42])})
      res.update({'duracion_paso': self.helpers.hexToDec(trm[43])})


      bits_falta = {}
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[58], name="falta_rojo_1",
                                    label="Rojo {0}", prefix="FR{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[59], name="falta_rojo_2",
                                    label="Rojo {0}", prefix="FR{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[60], name="falta_amarillo_1",
                                    label="Amarillo {0}", prefix="FA{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[61], name="falta_amarillo_2",
                                    label="Amarillo {0}", prefix="FA{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[62], name="falta_verde_1",
                                    label="Verde {0}", prefix="FV{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[63], name="falta_verde_2",
                                    label="Verde {0}", prefix="FV{0}",
                                    start=9))


      bits_falta.update(
          self.bits_falta.bitsFalta(trm[64], name="conflicto_rojo_1",
                                    label="Conflicto Rojo {0}",
                                    prefix="FR{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[65], name="conflicto_rojo_2",
                                    label="Conflicto Rojo {0}",
                                    prefix="FR{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[66], name="conflicto_amarillo_1",
                                    label="Conflicto Amarillo {0}",
                                    prefix="FA{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[67], name="conflicto_amarillo_2",
                                    label="Conflicto Amarillo {0}",
                                    prefix="FA{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[68], name="conflicto_verde_1",
                                    label="Conflicto Verde {0}",
                                    prefix="FV{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[69], name="conflicto_verde_2",
                                    label="Conflicto Verde {0}",
                                    prefix="FV{0}",
                                    start=9))


      bits_falta.update(
          self.bits_falta.bitsFalta(trm[70], name="fusible_rojo_1",
                                    label="Fusible Rojo {0}",
                                    prefix="FR{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[71], name="fusible_rojo_2",
                                    label="Fusible Rojo {0}",
                                    prefix="FR{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[72], name="fusible_amarillo_1",
                                    label="Fusible Amarillo {0}",
                                    prefix="FA{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[73], name="fusible_amarillo_2",
                                    label="Fusible Amarillo {0}",
                                    prefix="FA{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[74], name="fusible_verde_1",
                                    label="Fusible Verde {0}",
                                    prefix="FV{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[75], name="fusible_verde_2",
                                    label="Fusible Verde {0}",
                                    prefix="FV{0}",
                                    start=9))


      bits_falta.update(
          self.bits_falta.bitsFalta(trm[76], name="detector_demanda_1",
                                    label="Detector {0}", prefix="DD{0}",
                                    start=1))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[77], name="detector_demanda_2",
                                    label="Detector {0}", prefix="DD{0}",
                                    start=9))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[78], name="detector_demanda_3",
                                    label="Detector {0}", prefix="DD{0}",
                                    start=17))
      bits_falta.update(
          self.bits_falta.bitsFalta(trm[79], name="detector_demanda_4",
                                    label="Detector {0}", prefix="DD{0}",
                                    start=25))




      res.update(bits_falta)
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
  import pprint as pp

  # Falta de rojo 5
  trama = "00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 14 00 00 00 EE EE EE EE EE EE 1E 00 19 07 10 12 50 11 04 00 00 00 08 01 00 00 00 05 00 29 00 00 00 2D 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 95"
  # Falta de amarillo 2
  trama = "00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 14 00 00 00 EE EE EE EE EE EE 1E 00 19 07 10 12 50 11 04 00 00 00 08 01 00 00 00 05 00 29 00 00 00 2D 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 87"
  # Falta de fusible rojo 1
  trama = "00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 14 00 00 00 EE EE EE EE EE EE 1E 00 19 07 10 12 50 11 04 00 00 00 08 01 00 00 00 05 00 29 00 00 00 2D 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 84"
  # Falta de Fusible Verde 16
  trama = "00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 14 00 00 00 EE EE EE EE EE EE 1E 00 19 07 10 12 50 11 04 00 00 00 08 01 00 00 00 05 00 29 00 00 00 2D 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05"


  bcc = Bcc()
  # b = bcc.isValidBcc(trama)
  # print(b)
  # print(bcc.consolidate(trama))
  # print(bcc.isValidBcc(trama))


  obj     = RespuestaEstadoEnvioComando()
  retorno = obj.get(bcc.consolidate(trama))
  pp.pprint(retorno)
