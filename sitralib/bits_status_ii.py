# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsStatusII:
  def __init__(self):
    self.helpers = Helpers()

  def bitsStatusII(self, hex):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)
    sta = {}
    estado = {}

    estado = {
        'AIS': {'des': 'Equipo controlador aislado de grupo (No acepta comandos grupales)'}
    }
    if int(byte.binaryReversed[0]) == 1:
      estado['AIS'].update({'est': {'val': 1, 'des': 'Aislado'}})
    else:
      estado['AIS'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({
        'SI': {'des': 'Equipo controlador en secuencia de inicio (intervalos A [34] y B [35])'}
    })
    if int(byte.binaryReversed[6]) == 1:
      estado['SI'].update({'est': {'val': 1, 'des': 'Secuencia de inicio'}})
    else:
      estado['SI'].update({'est': {'val': 0, 'des': 'Normal'}})

    est = {'bits_status_ii': estado}
    return est


if __name__ == "__main__":
  a = BitsStatusII()
  b = a.bitsStatusII('01')
  print(b)
