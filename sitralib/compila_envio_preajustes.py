# -*- coding: utf-8 -*-
from collections import *

from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class CompilaEnvioPreajustes:
  """
  Envio de preajustes
  x70
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):

    numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

    trama     = defaultdict(dict)
    trama[1]  = '00'
    trama[2]  = '00'
    trama[3]  = '00'
    trama[4]  = '00'
    trama[5]  = 'FF'
    trama[6]  = '00'
    trama[7]  = '00'
    trama[8]  = self.helpers.intToHexString(kwargs['grp_id_num'])
    trama[9]  = '70'  # Codigo según Protocolo
    trama[10] = '00'
    trama[11] = '51'
    trama[12] = '00'  # BCC intermedio
    trama[13] = numeroControlador[:-2]
    trama[14] = numeroControlador[-2:]
    trama[15] = '00'
    trama[16] = '00'
    trama[17] = '00'
    trama[18] = self.helpers.intToHexString(kwargs['grp_id_num'])
    trama[19] = numeroControlador[:-2]
    trama[20] = numeroControlador[-2:]

    for i in range(21, 85):
      trama[i] = '00'

    trama[85] = '00'  # BCC final

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None
