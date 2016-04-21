from sitralib.helpers.funciones import *


class Bcc(object):
    def __init__(self):
        self.helpers = Helpers()

    def isValidBcc(self, trama, bcc1, bcc2):
        b1 = self.validateBccIntermadio(trama, bcc1)
        b2 = self.validateBccFinal(trama, bcc1, bcc2)

        if bcc1 in trama.keys() and bcc2 in trama.keys():
            if self.helpers.hexToDec(trama[bcc1]) == self.helpers.hexToDec(
                    b1) and self.helpers.hexToDec(
                trama[bcc2]) == self.helpers.hexToDec(b2):
                return True
            else:
                return False

    def validateBccIntermadio(self, trama, bccIntermedioPosition=12):
        bcc1 = 0
        for i in trama:
            if i == bccIntermedioPosition:
                break
            else:
                bcc1 = bcc1 ^ self.helpers.hexToDec(trama[i])
        return self.helpers.intToHexString(bcc1)

    def validateBccFinal(self, trama, bccIntermedioPosition, bccFinalPosition):
        bcc2 = 0

        for i in trama:
            if i == bccFinalPosition:
                break
            elif self.helpers.validateBetween(
                    min=bccIntermedioPosition,
                    max=bccFinalPosition,
                    number=i
            ):
                bcc2 = bcc2 ^ self.helpers.hexToDec(trama[i])

        return self.helpers.intToHexString(bcc2)


if __name__ == "__main__":
    from sitralib.helpers.ordenartrama import *

    trama1 = '00 00 00 00 FF 00 00 01 7C 00 0C 8E 1B BB 01 2F'

    # Necesito procesar la trama para convertirla en Diccionario
    o = OrdenarTrama()
    trm = o.ordenartrama(trama1)
    print(trm)
    a = Bcc()
    b = a.isValidBcc(trm, 12, 16)
    print(b)
