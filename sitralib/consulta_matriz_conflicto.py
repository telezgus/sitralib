from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *

POSICION_BCC_INTERMEDIO = 12
POSICION_BCC_FINAL = 15


class ConsultaMatrizConflicto(object):
    """
    Tabla 4.27:
        Trama de consulta de matriz de conflictos desde CC hacia EC
    x6B
    """

    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def create(self, **kwargs):
        numeroControlador = self.helpers.intToHexString(
            kwargs['crs_numero'],
            4
        )

        telegramaEnvio = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',
            6: '00',
            7: '00',
            8: self.helpers.intToHexString(kwargs['grp_id_numero']),
            9: '6B',  # Codigo según Protocolo
            10: '00',
            11: '0B',
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: '00',  # BCC
        }

        bcc1 = self.bcc.validateBccIntermadio(telegramaEnvio)
        telegramaEnvio[POSICION_BCC_INTERMEDIO] = bcc1

        bcc2 = self.bcc.validateBccFinal(
            telegramaEnvio,
            POSICION_BCC_INTERMEDIO,
            POSICION_BCC_FINAL
        )
        telegramaEnvio[POSICION_BCC_FINAL] = bcc2

        if self.bcc.isValidBcc(
                telegramaEnvio,
                POSICION_BCC_INTERMEDIO,
                POSICION_BCC_FINAL
        ):
            return ' '.join(telegramaEnvio.values())
        else:
            return None


if __name__ == "__main__":
    o = ConsultaMatrizConflicto()
    a = o.create(crs_numero=3000, grp_id_numero=1)
    print(a)
    # REf. 00 00 00 00 FF 00 00 01 6B 00 0B 9E 0B B8 2D
