"""
Crea la trama de imposición de hora

Ver referencias en Protocolo SITAR
"Trama de imposición fecha y hora desde CC hacia EC"
"""
import time

from sitralib.validators.bcc import *

POSICION_BCC_INTERMEDIO = 12
POSICION_BCC_FINAL = 22


class ImposicionFechaHora(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def create(self, **kwargs):
        numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)
        tme = time.strptime(kwargs['datetime'], "%Y-%m-%d %H:%M:%S")

        telegramaEnvio = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',
            6: '00',
            7: '00',
            8: self.helpers.intToHexString(kwargs['grp_id_numero']),
            9: '66',  # Codigo según Protocolo
            10: '00',
            11: '12',
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: self.__zFill(tme.tm_year)[2:4],  # Año
            16: self.__zFill(tme.tm_mon),  # Mes
            17: self.__zFill(tme.tm_mday),  # Día
            18: self.__zFill(tme.tm_hour),  # hora
            19: self.__zFill(tme.tm_min),  # Minutos
            20: self.__zFill(tme.tm_sec),  # Segundos
            21: self.__zFill(tme.tm_wday),  # Día de la semana
            22: '00',  # BCC
        }

        # Primer validación BCC
        bcc1 = self.bcc.validateBccIntermadio(telegramaEnvio)
        telegramaEnvio[POSICION_BCC_INTERMEDIO] = bcc1
        # Segunda validación BCC
        bcc2 = self.bcc.validateBccFinal(telegramaEnvio,
                                         POSICION_BCC_INTERMEDIO,
                                         POSICION_BCC_FINAL)
        telegramaEnvio[POSICION_BCC_FINAL] = bcc2

        if self.bcc.isValidBcc(telegramaEnvio, POSICION_BCC_INTERMEDIO,
                               POSICION_BCC_FINAL):
            return ' '.join(telegramaEnvio.values())
        else:
            return None

    def __zFill(self, value):
        return str(value).zfill(2)


if __name__ == '__main__':
    help_text = """
    Crea la trama de imposición de hora

    Ejemplo:
        imposicionFechaHora = ImposicionFechaHora()
        trama = imposicionFechaHora.create(
            grp_id_numero=30,
            crs_numero=3000,
            datetime='2015-10-09 06:29:00'
        )
        print(trama)
    """
    print(help_text)
    # Ejemplo
    imposicionFechaHora = ImposicionFechaHora()
    trama = imposicionFechaHora.create(
            grp_id_numero=30,
            crs_numero=3000,
            datetime='2015-10-09 06:29:00'
    )
    print(trama)
