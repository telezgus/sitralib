# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *


class ByteFuncion(object):
  def __init__(self):
    self.helpers = Helpers()

  def get(self, hex):
    dec = self.helpers.hexToDec(hex)

    if (dec == 0):
      cod = 'NAN'
      val = '00'
      des = 'Ninguna'
    elif (dec == 1):
      cod = 'SY'
      val = '01'
      des = 'Sincronismo'
    elif (dec == 2):
      cod = 'FO'
      val = '02'
      des = 'Avance'
    elif (dec == 3):
      cod = 'JC'
      val = '03'
      des = 'Salto incondicional'
    elif (dec == 4):
      cod = 'STE'
      val = '04'
      des = 'Extensión'
    elif (dec == 5):
      cod = 'JU'
      val = '05'
      des = 'Salto incondicional'
    elif (dec == 6):
      cod = 'SY+JC'
      val = '06'
      des = 'Sincronismo + salto condicional'
    elif (dec == 7):
      cod = 'FO+JC'
      val = '07'
      des = 'Avance + salto incondicional'
    elif (dec == 8):
      cod = 'RD1'
      val = '08'
      des = 'Borrar demanda 1'
    elif (dec == 9):
      cod = 'RD2'
      val = '09'
      des = 'Borrar demanda 2'
    elif (dec == 10):
      cod = 'RD3'
      val = '0A'
      des = 'Borrar demanda 3'
    elif (dec == 11):
      cod = 'RD4'
      val = '0B'
      des = 'Borrar demanda 4'
    elif (dec == 12):
      cod = 'RD5'
      val = '0C'
      des = 'Borrar demanda 5'
    elif (dec == 13):
      cod = 'RD6'
      val = '0D'
      des = 'Borrar demanda 6'
    elif (dec == 14):
      cod = 'RD7'
      val = '0D'
      des = 'Borrar demanda 7'
    elif (dec == 15):
      cod = 'RD8'
      val = '0F'
      des = 'Borrar demanda 8'
    elif (dec == 16):
      cod = 'RAD'
      val = '10'
      des = 'Borra todas las demandas'
    else:
      return dict()

    std = {'cod': cod, 'val': val, 'des': des}
    return std


if __name__ == "__main__":
  help_text = """
  Ejemplo:
    a = ByteFuncion()
    b = a.byteFuncion('01')
    print(b)
  """
  print(help_text)
  # Ejemplo
  a = ByteFuncion()
  b = a.get('01')
  print(b)
