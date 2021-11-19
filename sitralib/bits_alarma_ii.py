# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsAlarmaII:
  def __init__(self):
    self.helpers = Helpers()


  def bitsAlarmaII(self, hex):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)

    evaluacion = [
        {"val": 0, "des": "Normal"},
        {"val": 1, "des": "Falla"},
    ]

    estado = {
      "ERTC": {
        "des": "Error Seg RTC",
        "est": evaluacion[int(byte.binaryReversed[0])]
      },
      "MEEX": {
        "des": "Modo Emergencia Externo",
        "est": evaluacion[int(byte.binaryReversed[1])]
      },
      "MMEX": {
        "des": "Modo Manual Externo",
        "est": evaluacion[int(byte.binaryReversed[2])]
      },
      "PMMX": {
        "des": "Pulso del Modo Manual Externo",
        "est": evaluacion[int(byte.binaryReversed[3])]
      },
      "CLCO": {
        "des": "Cambio Local Configuracion",
        "est": evaluacion[int(byte.binaryReversed[4])]
      },
      "CLAG": {
        "des": "Cambio Local Agendas",
        "est": evaluacion[int(byte.binaryReversed[5])]
      },
      "CLPR": {
        "des": "Cambio Local Programas",
        "est": evaluacion[int(byte.binaryReversed[6])]
      },
      "PPPC": {
        "des": "Programacion por PC",
        "est": evaluacion[int(byte.binaryReversed[7])]
      },
    }

    est = {"bits_alarma_ii": estado}
    return est



if __name__ == "__main__":
  import pprint as pp

  a = BitsAlarmaII()
  b = a.bitsAlarmaII("10")
  pp.pprint(b)
