# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *

class OrdenarTrama(object):
  def __init__(self):
    self.helpers = Helpers()

  def ordenarTrama(self, trama):
    trmdict = self.__tramaToDict(trama)
    key = self.__getFfPosition(trmdict)

    if key == None: return {}
    c = 5  # 5 es la posición FF en el protocolo
    trm = {}
    for i in trmdict.keys():
      if i >= key:
        trm[c] = trmdict[i]
        c += 1
    return trm

  def __listtodict(self, trama):
    a = {}
    for i in range(0, len(trama)):
      a[i] = self.helpers.sanitizeHex(trama[i])

    return a

  def __stringToDict(self, trama):
    sanitizeString = trama.replace(' ', '')
    listTrama = self.helpers.chunkStr(sanitizeString, 2)

    return self.__listtodict(listTrama)

  def __getFfPosition(self, trama):
    """
    Retorna el la posicion en la que se encuentra FF.
    :param trama: dict
    :return: integer
    """
    for valor in trama:
      if self.helpers.hexToDec(trama[valor]) == 255:
        return valor
    return None

  def __dicttodict(self, trama):
    trm = {}
    for key in trama:
      trm[key] = self.helpers.sanitizeHex(trama[key])

    return trm

  def __tramaToDict(self, trama):
    getType = type(trama)
    if getType == list:
      return self.__listtodict(trama)
    elif getType == dict:
      return self.__dicttodict(trama)
    elif getType == str:
      return self.__stringToDict(trama)
    else:
      return None


  def get_codigo_trama(self, trama):
    """
    Retorna el codigo de la trama
    """
    trm = self.ordenarTrama(trama)
    try:
      return trm[9]
    except KeyError:
      return None




if __name__ == '__main__':
  help_text = """
  Ordena una trama de números hexadecimales

  Ejemplo:
    o = Ordenartrama()
    trm1 = o.ordenarTrama('00000000FF0000017C000C8E1BBB012F')
    trm2 = o.ordenarTrama('00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F')
    print(trm1)
    print(trm2)
  """
  print(help_text)

  # Ejemplo
  o = OrdenarTrama()
  trm0 = o.ordenarTrama(['0x0', '0x0', '0x0', '0x0', '0xff', '0x0', '0x0', '0x1', '0xc9', '0x0', '0x10', '0x27', '0xb', '0xb8', '0x1', '0x14', '0x0', '0x20', '0x0', '0xa1'])
  trm1 = o.ordenarTrama('00000000FF0000017C000C8E1BBB012FEEFF00')
  trm2 = o.ordenarTrama('00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F')
  trm3 = o.ordenarTrama('00 00 00 00 00 FF 00 00 01 C5 00 56 6D 0B B8 00 34 40 20 00 99 99 DD DD DD DD DD DD 16 04 23 15 02 57 07 00 00 00 22 03 00 00 00 05 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CC')
  trm4 = o.ordenarTrama('00 00 FF 00 00 01 C8 00 36 00 0B B8 01 14 00 20 00 99 99 DD DD DD DD DD DD 16 04 23 19 21 36 07 00 01 01 02 02 00 00 01 0A 00 16 00 00 00 28 00 00 00 00 00 00 00 00 8B')
  trm5 = o.ordenarTrama('00 FF 00 00 01 C8 00 36 00 0B B8 01 14 00 20 00 99 99 DD DD DD DD DD DD 16 04 23 19 21 36 07 00 01 01 02 02 00 00 01 0A 00 16 00 00 00 28 00 00 00 00 00 00 00 00 8B')
  trm6 = o.ordenarTrama('00 00 00 00 00 00 00 00 00 00 00 00 FF 00 00 01 C8 00 36 00 0B B8 01 14 00 20 00 99 99 DD DD DD DD DD DD 16 04 23 19 21 36 07 00 01 01 02 02 00 00 01 0A 00 16 00 00 00 28 00 00 00 00 00 00 00 00 8B')

  # print(trm0, '\n')
  print(trm1, '\n')
  # print(trm2, '\n')
  # print(trm3, '\n')
  # print(trm4, '\n')
  # print(trm5, '\n')
  print(trm6)
