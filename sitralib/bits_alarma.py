# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsAlarma(object):
  def __init__(self):
    self.helpers = Helpers()

  def bitsAlarma(self, hex):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)

    estado = {'FR': {'des': 'Falta de rojo'}}

    if int(byte.binaryReversed[0]) == 1:
      estado['FR'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['FR'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'TSUP': {'des': 'Tiempo suplementario de ciclo'}})
    if int(byte.binaryReversed[1]) == 1:
      estado['TSUP'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['TSUP'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'CV': {'des': 'Conflicto de verde'}})
    if int(byte.binaryReversed[2]) == 1:
      estado['CV'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['CV'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'BT': {'des': 'Baja tensión'}})
    if int(byte.binaryReversed[3]) == 1:
      estado['BT'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['BT'].update({'est': {'val': 0, 'des': 'Normal'}})

    # NUEVOS
    estado.update({'FV': {'des': 'Falta de verde'}})
    if int(byte.binaryReversed[4]) == 1:
      estado['FV'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['FV'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'GPS': {'des': 'Sistema de posicionamiento global'}})
    if int(byte.binaryReversed[5]) == 1:
      estado['GPS'].update({'est': {'val': 1, 'des': 'Falla'}})
    else:
      estado['GPS'].update({'est': {'val': 0, 'des': 'Normal'}})

    est = {'bits_alarma': estado}
    return est

if __name__ == "__main__":
  a = BitsAlarma()
  b = a.bitsAlarma('01')
  print(b)