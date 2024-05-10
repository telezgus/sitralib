# -*- coding: utf-8 -*-
from sitralib.helpers.byte import Byte
from sitralib.helpers.funciones import Helpers


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
        "des": "Error de segundero RTC",
        "est": evaluacion[int(byte.binaryReversed[0])]
      },
      "MEEX": {
        "des": "Modo emergencia externo",
        "est": evaluacion[int(byte.binaryReversed[1])]
      },
      "MMEX": {
        "des": "Modo manual externo",
        "est": evaluacion[int(byte.binaryReversed[2])]
      },
      "PMMX": {
        "des": "Pulso del modo manual externo",
        "est": evaluacion[int(byte.binaryReversed[3])]
      },
      "CLCO": {
        "des": "Cambio local configuracion",
        "est": evaluacion[int(byte.binaryReversed[4])]
      },
      "CLAG": {
        "des": "Cambio local agendas",
        "est": evaluacion[int(byte.binaryReversed[5])]
      },
      "CLPR": {
        "des": "Cambio local programas",
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
  b = a.bitsAlarmaII("ff")
  pp.pprint(b)
