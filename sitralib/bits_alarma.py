# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsAlarma:
  def __init__(self):
    self.helpers = Helpers()


  def bitsAlarma(self, hex):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)

    evaluacion = [
        {"val": 0, "des": "Normal"},
        {"val": 1, "des": "Falla"},
    ]

    estado = {
      "FR": {
        "des": "Falta de rojo",
        "est": evaluacion[int(byte.binaryReversed[0])]
      },
      "TSUP": {
        "des": "Tiempo suplementario de ciclo",
        "est": evaluacion[int(byte.binaryReversed[1])]
      },
      "CV": {
        "des": "Conflicto de verde",
        "est": evaluacion[int(byte.binaryReversed[2])]
      },
      "BTT": {
        "des": "Baja tensión, umbral de titilante",
        "est": evaluacion[int(byte.binaryReversed[3])]
      },
      "PA": {
        "des": "Puerta abierta",
        "est": evaluacion[int(byte.binaryReversed[4])]
      },
      "GPS": {
        "des": "Sistema de posicionamiento global",
        "est": evaluacion[int(byte.binaryReversed[5])]
      },
      "FV": {
        "des": "Falta de verde",
        "est": evaluacion[int(byte.binaryReversed[6])]
      },
      "BTA": {
        "des": "Baja tensión, umbral de apagado",
        "est": evaluacion[int(byte.binaryReversed[7])]
      },
    }

    est = {"bits_alarma": estado}
    return est



if __name__ == "__main__":
  import pprint as pp

  a = BitsAlarma()
  b = a.bitsAlarma("10")
  pp.pprint(b)
