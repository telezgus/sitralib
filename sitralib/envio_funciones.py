# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class EnvioFunciones:
  """
  Tabla 4.29:
    Trama de envío de funciones desde CC hacia EC
  x6F
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):
    numeroControlador = self.helpers.intToHexString(
      kwargs['crs_numero'],
      4
    )

    trama = {
      1: '00',
      2: '00',
      3: '00',
      4: '00',
      5: 'FF',
      6: '00',
      7: '00',
      8: self.helpers.intToHexString(kwargs['grp_id_num']),
      9: '6E',  # Codigo según Protocolo
      10: '00',
      11: '26',
      12: '00',  # BCC intermedio
      13: numeroControlador[:-2],
      14: numeroControlador[-2:],
      15: '00',
      16: '00',
      17: '00',
      18: '00',
      19: '00',
      20: '00',
      21: '00',
      22: '00',
      23: '00',
      24: '00',
      25: '00',
      26: '00',
      27: '00',
      28: '00',
      29: '00',
      30: '00',
      31: '00',
      32: '00',
      33: '00',
      34: '00',
      35: '00',
      36: '00',
      37: '00',
      38: '00',
      39: '00',
      40: '00',
      41: '00',
      42: '00'  # BCC
    }

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None


if __name__ == "__main__":
  o = EnvioFunciones()
  a = o.create(crs_numero=3000, grp_id_num=1)
  print(a)
# "00 00 00 00 FF 00 00 01 75 00 0B 80 0B B8 33"
