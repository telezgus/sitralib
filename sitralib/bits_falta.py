# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsFalta:

  def __init__(self):
    self.helpers = Helpers()


  def bitsFalta(self, hex, name="Falta de rojo 1", label="Rojo {0}",
                prefix="FR{0}", start=9, autoincrement=False):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)
    estado = []
    evaluacion = [{"val": 0, "des": "Normal"}, {"val": 1, "des": "Falla"},]

    counter = 0
    for i in range(start, start+8):
      idx = i if autoincrement else ''
      byte_eval = int(byte.binaryReversed[counter])
      estado.append({
          prefix.format(idx) : {
            'des': label.format(idx).strip(),
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
  b = a.bitsFalta("02", name="verde_1", label="Verde {0}", prefix="FV{0}", 
                  start=1)
  pp.pprint(b)
