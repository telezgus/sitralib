# -*- coding: utf-8 -*-
from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class BitsStatusI:
  def __init__(self):
    self.helpers = Helpers()

  def bitsStatusI(self, hex):
    if self.helpers.isHex(hex) == False:
      pass

    byte = Byte(hex)
    sta = {}
    estado = {}

    estado = {'VP': {'des': 'Verde del movimiento 1'}}
    if int(byte.binaryReversed[7]) == 1:
      estado['VP'].update({'est': {'val': 1, 'des': 'Encendido'}})
    else:
      estado['VP'].update({'est': {'val': 0, 'des': 'Apagado'}})

    estado.update({'PFL': {'des': 'Plan forzado local desde CC'}})
    if int(byte.binaryReversed[6]) == 1:
      estado['PFL'].update({'est': {'val': 1, 'des': 'Forzado'}})
    else:
      estado['PFL'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'CP': {'des': 'Cambio de Plan'}})
    if int(byte.binaryReversed[5]) == 1:
      estado['CP'].update({'est': {'val': 1, 'des': 'Cambiando'}})
    else:
      estado['CP'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'LP': {'des': 'Llave panel local central'}})
    if int(byte.binaryReversed[4]) == 1:
      estado['LP'].update({'est': {'val': 1, 'des': 'Central'}})
    else:
      estado['LP'].update({'est': {'val': 0, 'des': 'Local'}})

    estado.update({'TD': {'des': 'Tipo de día'}})
    if int(byte.binaryReversed[3]) == 1:
      estado['TD'].update({'est': {'val': 1, 'des': 'Feriado o evento'}})
    else:
      estado['TD'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'C': {'des': 'Centralizado'}})
    if int(byte.binaryReversed[2]) == 1:
      estado['C'].update({'est': {'val': 1, 'des': 'Centralizado'}})
    else:
      estado['C'].update({'est': {'val': 0, 'des': 'Local'}})

    estado.update({'AP': {'des': 'Apagado'}})
    if int(byte.binaryReversed[1]) == 1:
      # Llave panel apagado o EC apagado
      estado['AP'].update({'est': {'val': 1, 'des': 'Apagado'}})
    else:
      estado['AP'].update({'est': {'val': 0, 'des': 'Normal'}})

    estado.update({'TIT': {'des': 'Titilante'}})
    if int(byte.binaryReversed[0]) == 1:
      # Llave panel titilante o EC titilante
      estado['TIT'].update({'est': {'val': 1, 'des': 'Titilante'}})
    else:
      estado['TIT'].update({'est': {'val': 0, 'des': 'Normal'}})

    est = {'bits_status_i': estado}

    return est


if __name__ == "__main__":
  a = BitsStatusI()
  b = a.bitsStatusI('01')
  print(b)
