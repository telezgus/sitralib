# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *


class ByteLamparas:
  def __init__(self):
    self.helpers = Helpers()


  def byteLamparas(self, hex, mov=False, **kwargs):
    """Obtiene los valores para los movimientos de lámpara
    :param hex: string, Numero hexadecimal
    :return: dict, con los valores para cada movimiento
    """
    if self.helpers.isHex(hex) == False:
      pass

    print('------>', hex)


    val   = self.helpers.getNibbles(hex)
    valLo = self.__getTipo(val['lo'])
    valHi = self.__getTipo(val['hi'])

    if mov == kwargs['hi']:
      return valHi
    elif mov == kwargs['lo']:
      return valLo
    else:
      return {
        'mov{hi}'.format(kwargs): valHi,
        'mov{lo}'.format(kwargs): valLo
      }


  def __getTipo(self, val):

    try:
      hexdec = self.helpers.hexToDec(val)

      dispatch = {
          0  : {
                  "val": 1,
                  "des": 'Apagado',
                  "cod": 'apagado'
               },
          1  : {
                  "val": 1,
                  "des": 'Rojo',
                  "cod": 'rojo'
               },
          2  : {
                  "val": 1,
                  "des": 'Amarillo',
                  "cod": 'amarillo'
               },
          3  : {
                  "val": 1,
                  "des": 'Rojo + Amarillo',
                  "cod": 'rojo-amarillo'
               },
          4  : {
                  "val": 1,
                  "des": 'Verde',
                  "cod": 'verde'
               },
          9  : {
                  "val": 1,
                  "des": 'Rojo intermitente',
                  "cod": 'rojo-intermitente'
               },
          10 : {
                  "val": 1,
                  "des": 'Amarillo intermitente',
                  "cod": 'amarillo-intermitente'
               },
          12 : {
                  "val": 1,
                  "des": 'Verde intermitente',
                  "cod": 'verde-intermitente'
               },
          11 : {
                  "val": 1,
                  "des": 'Rojo + Amarillo intermitente',
                  "cod": 'rojo-amarillo-intermitente'
               },
          14 : {
                  "val": 1,
                  "des": 'Verde + Amarillo intermitente',
                  "cod": 'verde-amarillo-intermitente'
               },
          13 : {
                  "val": 1,
                  "des": 'Inexistente',
                  "cod": 'inexistente'
               }
      }
      return dispatch.get(hexdec)

    except:
      return None



if __name__ == "__main__":
  opt = {'hi': 2, 'lo': 1}
  a = ByteLamparas()
  b = a.byteLamparas('01', hi=2, lo=1, mov=2)
  print(b)
