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

    def validateBetween(self, data={}):
        """
        Valida un que un número este comprendido entre un valor máximo y
        un mínimo. Lo valores se toman inclusivamente; esto es, contando los
        minimos y máximos.
        :param data: Diccionario {'min':int, 'max': int, 'number':int}
        :return: boolean
        """
        if data['min'] <= data['number'] <= data['max']:
            return True
        else:
            return False

    def getNibbles(self, hex):
        hex.zfill(2)
        nibble = {'hi': hex[0], 'lo': hex[1]}
        return nibble


if __name__ == '__main__':
    hlp = Helpers()

    print('hexToDec("AB")')
    print(hlp.hexToDec('AB'))
    print('\t')
    print('getNibbles("AB")')
    print(hlp.getNibbles('AB'))
    print('\t')
    print("sanitizeHex('B', 2)")
    print(hlp.sanitizeHex('B'))
    print('\t')
    print("sanitizeHex('B', 4)")
    print(hlp.sanitizeHex('B', 4))
    print('\t')
