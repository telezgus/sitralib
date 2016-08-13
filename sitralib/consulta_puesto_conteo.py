from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *

POSICION_BCC_INTERMEDIO = 12
POSICION_BCC_FINAL = 16


class ConsultaPuestoConteo(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def create(self, **kwargs):
        numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

        telegramaEnvio = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',  # Encabezado
            6: '00',  # Esclavo
            7: '00',  # Destino = 0 CITAR 1F COMCLS
            8: self.helpers.intToHexString(kwargs['grp_id_numero']),
            # Numero de grupo
            9: '7C',  # Codigo segun Protocolo
            10: '00',  # Longitud MSB
            11: '0C',  # Longitud LSB
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: self.helpers.intToHexString(kwargs['ccm_id'], 2),
            16: '00',  # BCC
        }

        bcc1 = self.bcc.validateBccIntermadio(telegramaEnvio)
        telegramaEnvio[POSICION_BCC_INTERMEDIO] = bcc1

        bcc2 = self.bcc.validateBccFinal(telegramaEnvio,
                                         POSICION_BCC_INTERMEDIO,
                                         POSICION_BCC_FINAL)
        telegramaEnvio[POSICION_BCC_FINAL] = bcc2

        if self.bcc.isValidBcc(telegramaEnvio, POSICION_BCC_INTERMEDIO,
                               POSICION_BCC_FINAL):
            return ' '.join(telegramaEnvio.values())
        else:
            return None


if __name__ == "__main__":
    help_text = """
    Consulta puesto de conteo

    Ejemplo:
        a = ConsultaPuestoConteo()
        trama = a.create(grp_id_numero=30, crs_numero=3000, ccm_id=1)
        print(trama)
    """
    print(help_text)

    pc = ConsultaPuestoConteo()
    trama = pc.create(grp_id_numero=30, crs_numero=3000, ccm_id=1)
    print(trama)
