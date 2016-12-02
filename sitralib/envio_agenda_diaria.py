from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class EnvioAgendaDiaria(object):
    """
    Tabla 4.25:
        Trama de envío de matriz de conflictos desde CC hacia EC
    x6C
    """

    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def __cambios(self, **kwargs):
        adh = dict()
        idx = 15
        for i in range(0, 10):
            idx += 1
            adh[idx] = i
            idx += 1
            adh[idx] = i
            idx += 1
            adh[idx] = i
            idx += 1
            adh[idx] = self.__demanda_almacenada(i)

        return adh

    def __demanda_almacenada(self, *args):
        return '00'

    def create(self, **kwargs):
        print(self.__cambios())
        numeroControlador = self.helpers.intToHexString(
            kwargs['crs_numero'],
            4
        )

        trama = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',
            6: '00',
            7: '00',
            8: self.helpers.intToHexString(kwargs['grp_id_numero']),
            9: '6C',  # Codigo según Protocolo
            10: '00',
            11: '26',
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: '00',
            16: '00',
            17: '00',
            18: '00',
            19: '00',
            20: '00',
            21: '00',
            22: '00',
            23: '00',
            24: '00',
            25: '00',
            26: '00',
            27: '00',
            28: '00',
            29: '00',
            30: '00',
            31: '00',
            32: '00',
            33: '00',
            34: '00',
            35: '00',
            36: '00',
            37: '00',
            38: '00',
            39: '00',
            40: '00',
            41: '00',
            42: '00'  # BCC
        }

        trama_consolidada = self.bcc.consolidate(trama)
        if trama_consolidada:
            return ' '.join(trama_consolidada.values())
        return None


if __name__ == "__main__":
    o = EnvioAgendaDiaria()
    a = o.create(crs_numero=3000, grp_id_numero=1)
    print(a)
