from sitralib.helpers.funciones import *


class Bcc(object):
    POSICION_BCC_INTERMEDIO = 12

    def __init__(self):
        self.helpers = Helpers()

    def isValidBcc(self, trama, *args):
        bcc1 = self.POSICION_BCC_INTERMEDIO
        bcc2 = self.__posicion_bcc2(trama)

        b1 = self.validateBccIntermadio(trama, bcc1)
        b2 = self.validateBccFinal(trama, bcc1, bcc2)

        if bcc1 in trama.keys() and bcc2 in trama.keys():
            if self.helpers.hexToDec(trama[bcc1]) == self.helpers.hexToDec(
                    b1) and self.helpers.hexToDec(
                trama[bcc2]) == self.helpers.hexToDec(b2):
                return True
            else:
                return False

        return False

    def validateBccIntermadio(self, trama, *args):
        bcc1 = 0
        for i in trama:
            if i == self.POSICION_BCC_INTERMEDIO:
                break
            else:
                bcc1 = bcc1 ^ self.helpers.hexToDec(trama[i])
        return self.helpers.intToHexString(bcc1)

    def validateBccFinal(self, trama, *args):
        bcc_final_position = self.__posicion_bcc2(trama)
        bcc2 = 0
        for i in trama:
            if i == bcc_final_position:
                break
            elif self.helpers.validateBetween(
                    min=self.POSICION_BCC_INTERMEDIO,
                    max=bcc_final_position,
                    number=i
            ):
                bcc2 = bcc2 ^ self.helpers.hexToDec(trama[i])

        return self.helpers.intToHexString(bcc2)

    def consolidate(self, trama):
        bcc1 = self.validateBccIntermadio(trama)
        trama[self.POSICION_BCC_INTERMEDIO] = bcc1

        bcc2 = self.validateBccFinal(trama)
        trama[self.__posicion_bcc2(trama)] = bcc2

        if self.isValidBcc(trama):
            return trama
        else:
            return False

    def __posicion_bcc2(self, trama):
        """
        Retorna el indice para la posicion del bcc2 en la trama
        :param trama: dict
        :return: integer
        """
        # Cuento el comienzo del diccionario y le resto 1, porque el
        # valor (segun protocolo), inicia en cero.
        return 5 + (self.__longitud_total(trama) - 1)

    def __longitud_total(self, trama):
        """
        Obtengo la posicion para el bcc2
        :param trama:
        :return: integer
        """
        return int(trama[10] + trama[11], 16)


if __name__ == "__main__":
    from sitralib.helpers.ordenar_trama import *

    trama1 = '00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F'
    trama2 = "00 00 00 00 FF 00 00 01 69 00 F6 61 0B B8 00 04 41 00 00 00 00 00 00 01 00 00 00 00 04 41 00 00 00 00 00 00 00 00 00 00 00 02 21 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 01 14 00 00 00 00 00 00 00 00 00 00 00 01 19 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 43 31 00 00 00 00 00 00 05 00 00 00 FF A9 32 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 EE"

    # Necesito procesar la trama para convertirla en Diccionario
    o = OrdenarTrama()
    trm = o.ordenarTrama(trama1)


    n = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: '7C', 10: '00', 11: '0C', 12: '8E', 13: '1B', 14:  '01', 16: '00'}
    a = Bcc()
    c = a.consolidate(n)

    print(c)

    b = a.isValidBcc(n)
    print( b )

    trama_consolidada = a.consolidate(trm)
    print(trama_consolidada)

