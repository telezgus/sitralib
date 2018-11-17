# -*- coding: utf-8 -*-
import string

class Helpers(object):
  def sanitizeHex(self, num, fill=2):
    hexToDec = self.hexToDec(num)
    toHex = '{:X}'.format(hexToDec)
    zFill = toHex.zfill(fill)

    return zFill

  def hexToDec(self, num):
    """
    Hace la conversión de un número hexadecimal a decimal.
    :param num: str
    :return: int
    """
    try:
      return int(num, 16)
    except TypeError:
      return None
    else:
      if type(num) == 'string':
        return int(str(num), 16)

    return None

  def intToHexString(self, num, zfill=2):
    """
    Hace la conversión de un número decimal (integer), a un
    hexadecimal del tipo (string).
    :param num: Integer
    :param zfill: Cantidad de ceros antes del número.
    :return: string
    """
    return '{:X}'.format(int(num)).zfill(zfill)

  def listToDict(self, lista):
    """
    Convierte un list a dict.
    :param lista: List
    :return: Dict
    """
    a = {}
    for i in range(0, len(lista)):
      a[i] = lista[i]
    return a

  def chunkStr(self, str, chunk_size):
    """
    Divide una cadena de texto y la convierte en una lista de
    string del tamano de chunk_size
    :param str: Cadena de texto
    :param chunk_size: Integer
    :return: list
    """
    return [str[i:i + chunk_size] for i in range(0, len(str), chunk_size)]

  def isHex(self, num):
    """
    Valida si un número es hexadecimal.
    :param num: Número hexadecimal
    :return: boolean
    """
    if all(c in string.hexdigits for c in num):
      return True
    else:
      return False

  def validateBetween(self, **kwargs):
    """
    Valida un que un número este comprendido entre un valor máximo y
    un mínimo. Lo valores se toman inclusivamente; esto es, contando los
    minimos y máximos.
    :param kwargs: Diccionario {'min':int, 'max': int, 'number':int}
    :return: boolean
    """
    if kwargs['min'] <= int(kwargs['number']) <= kwargs['max']:
      return True
    else:
      return False

  def getNibbles(self, hex, zfill=None):
    hex.zfill(2)
    if not zfill:
      nibble = {
        'hi': hex[0],
        'lo': hex[1]
      }
    else:
      nibble = {
        'hi': self.sanitizeHex(hex[0], zfill),
        'lo': self.sanitizeHex(hex[1], zfill)
      }
    return nibble

  def sliceDict(self, dict_original, **kwargs):
    """
    Obtiene una porción de un diccionario con indices numéricos.
    :param dict_original: dict
    :param kwargs: min=[int], max=[int]
    :return: dict
    """
    slice = dict()
    for val in dict_original:
      if kwargs['min'] <= val <= kwargs['max']:
        slice.update({val: dict_original[val]})
    return slice;

  def tramas_by_codigo(self, **kwargs):
    """
    Obtiene las tramas de un código específico
    :param kwargs:
    :return: list
    """
    arr = list()
    for i in kwargs['tramas']:
      if i.get('9', 9).upper() == kwargs['codigo'].upper():
        arr.append(i)
    return arr

  def ddict2dict(self, d):
    """
    Convierte un diccionario creado con defaultdict a un
    diccionario convencional
    """
    for k, v in d.items():
      if isinstance(v, dict):
        d[k] = self.ddict2dict(v)
    return dict(d)

if __name__ == '__main__':
  hlp = Helpers()

  print(hlp.hexToDec('AA'), '\n')
  print(
    hlp.getNibbles('AB'), hlp.sanitizeHex(hlp.getNibbles('AB')['hi']), '\n'
  )
  print(hlp.sanitizeHex('B'), '\n')
  print(hlp.sanitizeHex('B', 4), '\n')
  print(hlp.validateBetween(max=47, min=0, number=3), '\n')
  print(hlp.chunkStr('1234567890', 2), '\n')
  test = {0: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'aA', 10: '00',
        11: '0C', 12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      1: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: '7C', 10: '00',
        11: '0C',
        12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      2: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: '44', 10: '00',
        11: '0C',
        12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      3: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'aa', 10: '00',
        11: '0C',
        12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      4: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: '7C', 10: '00',
        11: '0C',
        12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      5: {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'aa', 10: '00',
        11: '0C',
        12: '8E', 13: '1B', 14: 'BB', 15: '01', 16: '2F'},
      }
  print(hlp.tramas_by_codigo(tramas=test, codigo='AA'))
