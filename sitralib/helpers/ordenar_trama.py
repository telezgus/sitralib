# -*- coding: utf-8 -*-
import re
from sitralib.helpers.funciones import *


class OrdenarTrama(object):
  def __init__(self):
    self.helpers = Helpers()


  def ordenarTrama(self, trama):
    """Recibe una trama
    """
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
    """Convierte una trama pasada como list a un dict. Si un byte tiene
    solo un valor lo retorna con lu leading zero.

    Parameters
    ----------
    trama : list
        Trama pasada como list. Sus valores pueden ser enteros o strings.


    >>> __listtodict(["0", "1", "aa", "bb",])
    {0: '00', 1: '01', 2: 'AA', 3: 'BB'}

    >>> __listtodict([0, 1, "aa", "bb",])
    {0: '00', 1: '01', 2: 'AA', 3: 'BB'}

    >>> __listtodict([0, 1, "aa", "b",])
    {0: '00', 1: '01', 2: 'AA', 3: '0B'}
    """
    a = {}
    for i in range(0, len(trama)):
      a[i] = self.helpers.sanitizeHex(trama[i])
    return a


  def __stringToDict(self, trama):
    """Convierte una trama pasada como string a un diccionario.
    1. Si la trama tiene espacios se considera que estos separan bytes.
    2. Si la trama no tiene espacios se separa los bytes de grupos de 
    dos.

    Parameters
    ----------
    trama : string
        Trama pasada como string. Ésta puede tener espacios o 
        prescindir de ellos.


    >>> __stringToDict("0011223344")
    {0: '00', 1: '11', 2: '22', 3: '33', 4: '44'}

    >>> __stringToDict("0 11 22 33 44")
    {0: '00', 1: '11', 2: '22', 3: '33', 4: '44'}

    >>> __stringToDict("0 11 2233440")
    {0: '00', 1: '11', 2: '2233440'}
    """
    trama_stripped = trama.strip()
    contain_spaces = re.search(r"\s", trama_stripped)
    if contain_spaces:
      return self.__listtodict(trama_stripped.split())
    else:
      trama_to_list = self.helpers.chunkStr(trama_stripped, 2)
      return self.__listtodict(trama_to_list)

    return None


  def __getFfPosition(self, trama):
    """Retorna el la posicion en la que se encuentra el primer 
    0xff de la trama.

    Parameters
    ----------
    trama : dict
        Trama en formato dict.

    Returns
    -------
    int
        Posición o key del diccionario.
    None
        Si no existe la posición 0xff.

    >>> __getFfPosition({
              0: '00', 1: '00', 2: '00', 3: '00', 4: 'FF', 5: '00', 6: '00', 
              7: '01', 8: '7C', 9: '00', 10: '0C', 11: '8E', 12: '1B', 
              13: 'BB', 14: '01', 15: '2F'
        })
    4

    >>> __getFfPosition({
              0: '00', 1: 'FF', 2: '00', 3: '00', 4: '01', 5: '7C', 6: '00', 
              7: '0C', 8: '8E', 9: '1B', 10: 'BB', 11: '01', 12: '2F'
        })
    1

    >>> __getFfPosition({0: '00', 1: 'F1', 2: '00', 3: '00', 4: '00'})
    None
    """
    for valor in trama:
      if self.helpers.hexToDec(trama[valor]) == 255:
        return valor

    return None


  def __dicttodict(self, trama):
    """Retorna el diccionario con correccion de keys y valoes"""
    trm = {}
    for key in trama:
      trm[key] = self.helpers.sanitizeHex(trama[key])

    return trm


  def __tramaToDict(self, trama):
    """Retorna el diccionario de la trama habiendo recibido list, 
    dict o string.
    """
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
    """Retorna el codigo de la trama.
    
    Params
    —————-
    trama : string
    
    Return
    —————-
      str : Código hexadecimal.
    
    """
    trm = self.ordenarTrama(trama)
    try:
      return trm[9]
    except KeyError:
      return None




if __name__ == '__main__':
  help_text = """Ordena una trama de números hexadecimales

  Ejemplo:
    o = Ordenartrama()
    trm1 = o.ordenarTrama('00000000FF0000017C000C8E1BBB012F')
    trm2 = o.ordenarTrama('00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F')
    print(trm1)
    print(trm2)
  """
  print(help_text)
  print("-"*79, end="\n\n")

  # Ejemplo
  o = OrdenarTrama()
  trm0 = o.ordenarTrama(
        ['0x0', '0x0', '0x0', '0x0', '0xff', '0x0', '0x0', '0x1', '0xc9',
         '0x0', '0x10', '0x27', '0xb', '0xb8', '0x1', '0x14', '0x0', '0x20',
         '0x0', '0xa1']
  )
  trm1 = o.ordenarTrama('00000000FF0000017C000C8E1BBB012FEEFF00')
  trm2 = o.ordenarTrama('00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F')
  trm3 = o.ordenarTrama(
        ('0 0 0 0 FF 0 0 1 D1 0 2B 4 13 89 0 10 0 20 0 0 0 0 0 0 0 0 0 0 0 0 '
         '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 AE')
  )

  print(trm0, end='\n')
  print(trm1, end='\n')
  print(trm2, end='\n')
  print(trm3, end='\n')


