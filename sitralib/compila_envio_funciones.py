# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *
from collections import *


class CompilaEnvioFunciones:
  """
  Envio de funciones
  x6E
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
    trama[9]  = '6E'  # Codigo según Protocolo
    trama[10] = '00'
    trama[11] = '26'
    trama[12] = '00'  # BCC intermedio
    trama[13] = numeroControlador[:-2]
    trama[14] = numeroControlador[-2:]
    trama[15] = '00'
    trama[16] = '00'
    trama[17] = '00'
    trama[18] = '00'
    trama[19] = '00'
    trama[20] = '00'
    trama[21] = '00'
    trama[22] = '00'
    trama[23] = '00'
    trama[24] = '00'
    trama[25] = '00'
    trama[26] = '00'
    trama[27] = '00'
    trama[28] = '00'
    trama[29] = '00'
    trama[30] = '00'
    trama[31] = '00'
    trama[32] = '00'
    trama[33] = '00'
    trama[34] = '00'
    trama[35] = '00'
    trama[36] = '00'
    trama[37] = '00'
    trama[38] = '00'
    trama[39] = '00'
    trama[40] = '00'
    trama[41] = '00'
    trama[42] = '00'  # BCC Final

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None
