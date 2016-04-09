from sitralib.helpers.byte import *

from sitralib.helpers.funciones import *


class BitsDeStatusIII(object):
    def __init__(self):
        self.helpers = Helpers()

    def bitsDeStatusIII(self, hex):
        if self.helpers.isHex(hex) == False:
            pass

        byte = Byte(hex)
        sta = {}
        estado = {}

        if self.helpers.isHex(hex) == False:
            pass

        estado = {'D1': {'des': 'Demanda 1'}}
        if int(byte.binaryReversed[0]) == 1:
            estado['D1'].update({'est': {'val': 1, 'des': 'Ocupada'}})
        else:
            estado['D1'].update({'est': {'val': 0, 'des': 'Desocupada'}})

        estado.update({'D2': {'des': 'Demanda 2'}})
        if int(byte.binaryReversed[1]) == 1:
            estado['D2'].update({'est': {'val': 1, 'des': 'Ocupada'}})
        else:
            estado['D2'].update({'est': {'val': 0, 'des': 'Desocupada'}})

        est = {'bitsDeStatusIII': estado}
        return est


if __name__ == "__main__":
    help_text = """
    Ejemplo:
        a = BitsDeStatusIII()
        b = a.bitsDeStatusIII('01')
        print(b)
    """
    # ejemplo
    print(help_text)
    a = BitsDeStatusIII()
    b = a.bitsDeStatusIII('01')
    print(b)
