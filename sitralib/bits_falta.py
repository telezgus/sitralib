# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsFalta:

  def __init__(self):
    self.helpers = Helpers()


  def bitsFalta(self, hex, name="Falta de rojo 1", label="Rojo {0}",
                prefix="FR{0}", start=9):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)
    estado = []
    evaluacion = [{"val": 0, "des": "Normal"}, {"val": 1, "des": "Falla"},]

    counter = 0
    for i in range(start, start+8):
      byte_eval = int(byte.binaryReversed[counter])
      estado.append({
              "abbr"  : prefix.format(i),
              "name"  : label.format(i),
              "descr" : "Falla" if byte_eval == 1 else "Normal",
              "value" : byte_eval
      })
      counter +=1



    est = {name: estado}
    return est



if __name__ == "__main__":
  import pprint as pp

  a = BitsFalta()
  b = a.bitsFalta("02", name="verde_1", label="Verde {0}", prefix="FV{0}", 
                  start=1)
  pp.pprint(b)
