# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *


class ByteFuncion:
  def __init__(self):
    self.helpers = Helpers()


  def get(self, hex):

    try:
      dec = self.helpers.hexToDec(hex)

      dispatch = [
          {'cod': 'NAN', 'val': '00', 'des': 'Ninguna'},
          {'cod': 'SY', 'val': '01', 'des': 'Sincronismo'},
          {'cod': 'FO', 'val': '02', 'des': 'Avance'},
          {'cod': 'JC', 'val': '03', 'des': 'Salto incondicional'},
          {'cod': 'STE', 'val': '04', 'des': 'Extensión'},
          {'cod': 'JU', 'val': '05', 'des': 'Salto incondicional'},
          {'cod': 'SY', 'val': '06', 'des': 'Sincronismo + salto condicional'},
          {'cod': 'FO', 'val': '07', 'des': 'Avance + salto incondicional'},
          {'cod': 'RD1', 'val': '08', 'des': 'Borrar demanda 1'},
          {'cod': 'RD2', 'val': '09', 'des': 'Borrar demanda 2'},
          {'cod': 'RD3', 'val': '0A', 'des': 'Borrar demanda 3'},
          {'cod': 'RD4', 'val': '0B', 'des': 'Borrar demanda 4'},
          {'cod': 'RD5', 'val': '0C', 'des': 'Borrar demanda 5'},
          {'cod': 'RD6', 'val': '0D', 'des': 'Borrar demanda 6'},
          {'cod': 'RD7', 'val': '0D', 'des': 'Borrar demanda 7'},
          {'cod': 'RD8', 'val': '0F', 'des': 'Borrar demanda 8'},
          {'cod': 'RAD', 'val': '10', 'des': 'Borra todas las demandas'},
      ]

      return dispatch[dec]
    except:
      return dict()



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
  b = a.get('0b')
  print(b)
