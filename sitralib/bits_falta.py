# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsFalta:

  def __init__(self):
    self.helpers = Helpers()


  def bitsFalta(self, hex, name="", label="", prefix="",
                start=9, autoincrement=False):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)
    estado = []
    evaluacion = [{"val": 0, "des": "Normal"}, {"val": 1, "des": "Falla"}]

    counter = 0
    for i in range(start, start+8):
      idx = i if autoincrement else ''

      byte_eval = int(byte.binaryReversed[counter])
      bit = counter + 1
      estado.append({
          '{prefix}{id}'.format(prefix=prefix, id=bit) : {
            'des': '{label}, id {id}'.format(label=label, id=bit),
            'bit': bit,
            'est':{
              'val': byte_eval,
              'des': "Falla" if byte_eval == 1 else "Normal"
            }
          }
        }
      )
      counter +=1

    est = {name: estado}
    return est


if __name__ == "__main__":
  import pprint as pp

  a = BitsFalta()
  b = a.bitsFalta(
      "A1",
      name="verde_1",
      label="Verde",
      prefix="FV",
      start=1
  )
  pp.pprint(b)
