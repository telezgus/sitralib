from sitralib.helpers.funciones import *


class ByteDeFuncion(object):
    def __init__(self):
        self.helpers = Helpers()

    def byteDeFuncion(self, hex):

        std = {}
        dec = self.helpers.hexToDec(hex)

        if (dec == 0):
            std = {'NAN': {'est': {
                'val': 1,
                'des': 'Ninguna'
            }}}

        elif (dec == 1):
            std = {'SY': {'est': {
                'val': 1,
                'des': 'Sincronismo'
            }}}

        elif (dec == 2):
            std = {'FO': {'est': {
                'val': 1,
                'des': 'Avance'
            }}}

        elif (dec == 3):
            std = {'JC': {'est': {
                'val': 1,
                'des': 'Salto incondicional'
            }}}

        elif (dec == 4):
            std = {'STE': {'est': {
                'val': 1,
                'des': 'Extensión'
            }}}

        elif (dec == 5):
            std = {'JU': {'est': {
                'val': 1,
                'des': 'Salto incondicional'
            }}}

        elif (dec == 6):
            std = {'SY+JC': {'est': {
                'val': 1,
                'des': 'Sincronismo + salto condicional'
            }}}

        elif (dec == 7):
            std = {'FO+JC': {'est': {
                'val': 1,
                'des': 'Avance + salto incondicional'
            }}}

        elif (dec == 8):
            std = {'RD1': {'est': {
                'val': 1,
                'des': 'Borrar demanda 1'
            }}}

        elif (dec == 9):
            std = {'RD2': {'est': {
                'val': 1,
                'des': 'Borrar demanda 2'
            }}}

        elif (dec == 10):
            std = {'RD3': {'est': {
                'val': 1,
                'des': 'Borrar demanda 3'
            }}}

        elif (dec == 11):
            std = {'RD4': {'est': {
                'val': 1,
                'des': 'Borrar demanda 4'
            }}}

        elif (dec == 12):
            std = {'RD5': {'est': {
                'val': 1,
                'des': 'Borrar demanda 5'
            }}}

        elif (dec == 13):
            std = {'RD6': {'est': {
                'val': 1,
                'des': 'Borrar demanda 6'
            }}}

        elif (dec == 14):
            std = {'RD7': {'est': {
                'val': 1,
                'des': 'Borrar demanda 7'
            }}}

        elif (dec == 15):
            std = {'RD8': {'est': {
                'val': 1,
                'des': 'Borrar demanda 8'
            }}}

        elif (dec == 16):
            std = {'RAD': {'est': {
                'val': 1,
                'des': 'Borra todas las demandas'
            }}}

        r = {'byteDeFuncion': std}
        return r


if __name__ == "__main__":
    help_text = """
    Ejemplo:
        a = ByteDeFuncion()
        b = a.byteDeFuncion('01')
        print(b)
    """
    print(help_text)
    # Ejemplo
    a = ByteDeFuncion()
    b = a.byteDeFuncion('01')
    print(b)
