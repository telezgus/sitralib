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
        :param num: String
        :return: Integer
        """
        return int(num, 16)

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


if __name__ == '__main__':
    hlp = Helpers()

    print('hexToDec("AB")')
    print(hlp.hexToDec('AB'))
    print('\t')
    print('getNibbles("AB")')
    print(hlp.getNibbles('AB'), hlp.sanitizeHex(hlp.getNibbles('AB')['hi']))
    print('\t')
    print("sanitizeHex('B', 2)")
    print(hlp.sanitizeHex('B'))
    print('\t')
    print("sanitizeHex('B', 4)")
    print(hlp.sanitizeHex('B', 4))
    print('\t')
    print('validateBetween(max=47, min=0, number=3)')
    print(hlp.validateBetween(max=47, min=0, number=3))
    print('\t')
    print("chunkStr('1234567890', 2)")
    print(hlp.chunkStr('1234567890', 2))
