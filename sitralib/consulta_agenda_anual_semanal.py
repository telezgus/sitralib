# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class ConsultaAgendaAnualSemanal:
  """
  Tabla 4.44:
    Trama de consulta de agenda diaria desde CC hacia EC
  x75
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
      9: '75',  # Codigo según Protocolo
      10: '00',
      11: '0B',
      12: '00',  # BCC intermedio
      13: numeroControlador[:-2],
      14: numeroControlador[-2:],
      15: '00',  # BCC
    }

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None


if __name__ == "__main__":
  o = ConsultaAgendaAnualSemanal()
  a = o.create(crs_numero=3000, grp_id_num=1)
  print(a)
# "00 00 00 00 FF 00 00 01 75 00 0B 80 0B B8 33"
