from sitralib.helpers.funciones import *

from sitralib.helpers.ordenartrama import *
from sitralib.respuestaconsultagurpoextendido import *
from sitralib.respuestaestadoenviocomando import *

from sitralib.respuestaenviocomando import *
from sitralib.enviocomando import *


class Respuesta(object):
    def __init__(self):
        self.helpers = Helpers()
        self.ordtrama = OrdenarTrama()

    def obtenerRespuesta(self, trama):
        trm = self.ordtrama.ordenartrama(trama)

        if 9 in trm:
            dec = self.helpers.hexToDec(trm[9])
            if dec == 201:
                rtaenvcom = RespuestaEnvioComando()
                return rtaenvcom.respuestaEnvioComando(trm)
            elif dec == 200:
                tacongrpext = RespuestaConsultaGrupoExtendido()
                return tacongrpext.respuestaConsultaGrupoExtendido(trm)
            elif dec == 197:
                rtaestadoenviocomando = RespuestaEstadoEnvioComando()
                return rtaestadoenviocomando.respuestaEstadoEnvioComando(trm)
            else:
                return None


if __name__ == "__main__":
    pass
