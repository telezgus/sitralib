from sitralib.helpers.funciones import *


class ByteDeStatus(object):
    def __init__(self):
        self.helpers = Helpers()

    def byteDeStatus(self, hex):
        sta = {}
        status = {}
        if self.helpers.isHex(hex) == False:
            pass

        num = self.helpers.hexToDec(hex)
        sipla = self.helpers.validateBetween(
            {'min': 0, 'max': 47, 'number': num})

        if sipla:
            status['SIPLA'] = {
                'des': 'Plan',
                'val': str(num),
                'cod': 'SIPLA'
            }
        elif num == 240:
            status['TIT'] = {
                'des': 'Titilante',
                'val': True,
                'cod': 'TIT'
            }
        elif num == 241:
            status['AP'] = {
                'des': 'Apagado',
                'val': True,
                'cod': 'AP'
            }
        else:
            status = False

        sta['byteDeStatus'] = status
        return sta


if __name__ == "__main__":
    help_text = """
    Ejemplo:
        a = ByteDeStatus()
        b = a.byteDeStatus('F0')
        print(b)
    """
    print(help_text)

    a = ByteDeStatus()
    b = a.byteDeStatus('F0')
    print(b)
