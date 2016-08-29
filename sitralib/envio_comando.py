from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *

POSICION_BCC_INTERMEDIO = 12
POSICION_BCC_FINAL = 16


class EnvioComando(object):
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
            9: '65',  # Codigo según Protocolo
            10: '00',
            11: '0C',
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: self.helpers.intToHexString(kwargs['ccm_id'], 2),
            16: '00',  # BCC
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
                POSICION_BCC_FINAL):
            return ' '.join(telegramaEnvio.values())

        return None


if __name__ == "__main__":
    help_text = """
    Ejemplo:
        envioComando = EnvioComando()
        trama = envioComando.create(
            grp_id_numero=30,
            ccm_id=1,
            crs_numero=3000
        )
    """
    print(help_text)

    envioComando = EnvioComando()
    trama = envioComando.create(
        grp_id_numero=30,
        ccm_id=1,
        crs_numero=3000
    )
    print(trama)
