from sitralib.helpers.funciones import *


class ByteLamparas(object):
  def __init__(self):
    self.helpers = Helpers()

  def byteLamparas(self, hex, mov=False, **kwargs):
    """
    Obtiene los valores para los movimientos de lámpara
    :param hex: string, Numero hexadecimal
    :return: dict, con los valores para cada movimiento
    """
    if self.helpers.isHex(hex) == False:
      pass

    val = self.helpers.getNibbles(hex)
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
    hexdec = self.helpers.hexToDec(val)

    if hexdec == 0:
      val = 1
      des = 'Apagado'
      cod = 'apagado'
    elif hexdec == 1:
      val = 1
      des = 'Rojo'
      cod = 'rojo'
    elif hexdec == 2:
      val = 1
      des = 'Amarillo'
      cod = 'amarillo'
    elif hexdec == 3:
      val = 1
      des = 'Rojo + Amarillo'
      cod = 'rojo-amarillo'
    elif hexdec == 4:
      val = 1
      des = 'Verde'
      cod = 'verde'
    elif hexdec == 9:
      val = 1
      des = 'Rojo intermitente'
      cod = 'rojo-intermitente'
    elif hexdec == 10:
      val = 1
      des = 'Amarillo intermitente'
      cod = 'amarillo-intermitente'
    elif hexdec == 12:
      val = 1
      des = 'Verde intermitente'
      cod = 'verde-intermitente'
    elif hexdec == 11:
      val = 1
      des = 'Rojo + Amarillo intermitente'
      cod = 'rojo-amarillo-intermitente'
    elif hexdec == 14:
      val = 1
      des = 'Verde + Amarillo intermitente'
      cod = 'verde-amarillo-intermitente'
    elif hexdec == 13:
      val = 1
      des = 'Inexistente'
      cod = 'inexistente'
    else:
      return None

    estado = {'val': val, 'des': des, 'cod': cod}
    return estado


if __name__ == "__main__":
  opt = {'hi': 2, 'lo': 1}
  a = ByteLamparas()
  b = a.byteLamparas('01', hi=2, lo=1, mov=2)
  print(b)
