from sitralib.helpers.byte import *
from sitralib.helpers.funciones import *


class UneBitsForzadura:
    def __init__(self):
        self.helpers = Helpers()


    def bitsForzadura(self, hex):
        if self.helpers.isHex(hex) == False:
            pass

        byte = Byte(hex)

        evaluacion = [
            {"val": 0, "des": "Normal"},
            {"val": 1, "des": "Falla"},
        ]

        estado = {
            "ciclo": {
                "des": "Forzadura de ciclo",
                "est": evaluacion[int(byte.binaryReversed[0])]
            },
            "desfazaje": {
                "des": "Forzadura de desfazaje",
                "est": evaluacion[int(byte.binaryReversed[1])]
            },
            "fases": {
                "des": "Forzadura de fases",
                "est": evaluacion[int(byte.binaryReversed[2])]
            },
        }

        est = {"une_bits_forzadura": estado}
        return est



if __name__ == "__main__":
    import pprint as pp
    byte = '84'
    a = UneBitsForzadura()
    b = a.bitsForzadura(byte)
    
    print('='*79)
    print(byte)
    print('-'*79)
    pp.pprint(b)
    print('='*79)
