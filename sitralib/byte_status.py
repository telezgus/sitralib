# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *


class ByteStatus:
  def __init__(self):
    self.helpers = Helpers()

  def byteStatus(self, hex):
    status = {}
    if self.helpers.isHex(hex) == False:
      pass

    num = self.helpers.hexToDec(hex)
    sipla = self.helpers.validateBetween(min=0, max=47, number=num)

    if sipla:
      status['SIPLA'] = {
        'des': 'Plan',
        'val': str(num),
        'cod': 'SIPLA'
      }
    elif num == 240:
      status['TIT'] = {
        'des': 'Titilante',
        'val': True,
        'cod': 'TIT'
      }
    elif num == 241:
      status['AP'] = {
        'des': 'Apagado',
        'val': True,
        'cod': 'AP'
      }
    else:
      status = False

    return status


if __name__ == "__main__":
  a = ByteStatus()
  b = a.byteStatus('F0')
  print(b)
