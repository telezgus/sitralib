from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class UnemConsultaEstadoEnvioComando:
    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def create(self, **kwargs):
        numeroControlador = self.helpers.intToHexString(
            kwargs['crs_numero'], 4)

        trama = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',
            6: '00',
            7: self.helpers.intToHexString(kwargs.get('esclavo', 0)), # Esclavo,
            8: self.helpers.intToHexString(kwargs['grp_id_num']),
            9: '4F',  # Codigo según Protocolo
            10: '00',
            11: '0C',
            12: '00',  # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: self.helpers.intToHexString(kwargs['ccm_id'], 2),
            16: '00',  # BCC
        }

        trama_consolidada = self.bcc.consolidate(trama)
        if trama_consolidada:
            return ' '.join(trama_consolidada.values())
        
        return None


if __name__ == "__main__":
    envioEstadoComando = UnemConsultaEstadoEnvioComando()
    kwargs = {
        'grp_id_num': 1,
        'ccm_id': 2,
        'crs_numero': 3100, 
        'esclavo': 0
    }
    trama = envioEstadoComando.create(**kwargs)
    print(trama)