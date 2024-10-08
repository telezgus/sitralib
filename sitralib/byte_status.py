# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers


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
        'des': 'Plan {}'.format(num),
        'val': str(num),
        'cod': 'SIPLA'
      }
    elif num == 240:
      status['TIT'] = {
        'des': 'Titilante',
        'val': '240',
        'cod': 'TIT'
      }
    elif num == 241:
      status['AP'] = {
        'des': 'Apagado',
        'val': '241',
        'cod': 'AP'
      }
    # elif num == 242:
    #   status = dict()
    else:
      status = dict()

    return status


if __name__ == "__main__":
  a = ByteStatus()
  b = a.byteStatus('F2')
  print(b)