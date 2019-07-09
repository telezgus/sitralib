# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class ConsultaAgendaDriaria:
  """
  Tabla 4.40:
    Trama de consulta de agenda diaria desde CC hacia EC
  x77
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
      9: '77',  # Codigo según Protocolo
      10: '00',
      11: '0C',
      12: '00',  # BCC intermedio
      13: numeroControlador[:-2],
      14: numeroControlador[-2:],
      # Número de Programa
      15: self.helpers.intToHexString(kwargs['adi_id_num']),
      16: '00',  # BCC
    }

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None


if __name__ == "__main__":
  o = ConsultaAgendaDriaria()
  a = o.create(crs_numero=3000, grp_id_num=1, adi_id_num=0)
  print(a)
