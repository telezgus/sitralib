# -*- coding: utf-8 -*-
import json
from collections import *

from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class CompilaEnvioProgramaTiempos:
  """
  Envio programa tiempos
  x6E
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):
    esp_data = json.loads(kwargs['esp_data'])

    numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)
    espCiclo = self.helpers.intToHexString(esp_data['espCiclo'], 4)
    espSup = self.helpers.intToHexString(esp_data['espSup'], 4)
    espDesfasaje = self.helpers.intToHexString(esp_data['espDesfasaje'], 4)

    intervalos = self.__set_intervalo(esp_data['espData'])

    trama = {}
    trama[1] = '00'
    trama[2] = '00'
    trama[3] = '00'
    trama[4] = '00'
    trama[5] = 'FF'
    trama[6] = '00'
    trama[7] = '00'
    trama[8] = self.helpers.intToHexString(kwargs['grp_id_num'])
    trama[9] = '72'  # Codigo según Protocolo
    trama[10] = '00'
    trama[11] = '48'
    trama[12] = '00'  # BCC intermedio
    trama[13] = numeroControlador[:-2]
    trama[14] = numeroControlador[-2:]
    trama[15] = self.helpers.intToHexString(kwargs['esp_id_num'])
    # ...Intervalos 16 a 51

    # trama.update(intervalos)
    for i in intervalos: trama[i] = intervalos[i]

    trama[52] = espCiclo[:-2]
    trama[53] = espCiclo[-2:]
    trama[54] = espSup[:-2]
    trama[55] = espSup[-2:]
    trama[56] = espDesfasaje[:-2]
    trama[57] = espDesfasaje[-2:]
    trama[58] = '7F'
    trama[59] = 'FF'
    trama[60] = '7F'
    trama[61] = 'FF'
    trama[62] = '7F'
    trama[63] = 'FF'
    trama[64] = '7F'
    trama[65] = 'FF'
    trama[66] = '7F'
    trama[67] = 'FF'
    trama[68] = '7F'
    trama[69] = 'FF'
    trama[70] = '7F'
    trama[71] = 'FF'
    trama[72] = '7F'
    trama[73] = 'FF'
    trama[74] = '7F'
    trama[75] = 'FF'
    trama[76] = '00'  # BCC final


    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None


  def __set_intervalo(self, data):
    posicion = defaultdict(dict)
    counter = 0
    for i in range(16, 52):
      posicion[i] = self.helpers.intToHexString(data[counter])
      counter += 1

    return posicion



if __name__ == "__main__":
    o = CompilaEnvioProgramaTiempos()
    a = o.create(
    crs_numero=3000,
    grp_id_num=1,
    esp_id_num=0,
    esp_data='{"espDesfasaje": "0", "espCiclo": "48", "espSup": "0", "espData": ["10", "10", "2", "1", "2", "10", "10", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "5", "5"]}'
  )
    print(a)
