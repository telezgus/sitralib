from sitralib.helpers.funciones import *

from sitralib.helpers.ordenar_trama import *
from sitralib.respuesta_consulta_gurpo_extendido import *
from sitralib.respuesta_estado_envio_comando import *

from sitralib.respuesta_envio_comando import *
from sitralib.envio_comando import *

from sitralib.respuesta_consulta_puesto_conteo import *
# Grabacion
from sitralib.grabacion_eeprom import *
from sitralib.respuesta_agenda_anual import *
from sitralib.respuesta_estrucutra_parte_alta import *
from sitralib.respuesta_estrucutra_parte_baja import *
from sitralib.respuesta_agenda_feriados_especial import *
from sitralib.respuesta_preajustes import *
from sitralib.respuesta_agenda_diaria import *
from sitralib.respuesta_funciones import *
from sitralib.respuesta_programa_tiempos import *
from sitralib.respuesta_matriz_conflictos import *


class Respuesta(object):
    def __init__(self):
        self.helpers = Helpers()
        self.ordtrama = OrdenarTrama()

    def obtenerRespuesta(self, trama):
        trm = self.ordtrama.ordenarTrama(trama)

        if 9 in trm:
            dec = self.helpers.hexToDec(trm[9])
            if dec == 201:
                obj = RespuestaEnvioComando()
                return obj.respuestaEnvioComando(trm)

            elif dec == 200:
                obj = RespuestaConsultaGrupoExtendido()
                return obj.respuestaConsultaGrupoExtendido(trm)

            elif dec == 197:
                obj = RespuestaEstadoEnvioComando()
                return obj.respuestaEstadoEnvioComando(trm)

            elif dec == 224:
                obj = RespuestaConsultaPuestoConteo()
                return obj.respuesta(trm)

            elif dec == 226:
                # 0xE2
                # Trama de grabación de EEPROM
                obj = GrabacionEeprom()
                return obj.grabar(trm)

            elif dec == 212:
                # 0xD4
                # Trama de respuesta de envio de preajustes
                obj = RespuestaPreajustes()
                return obj.respuesta(trm)

            elif dec == 216:
                # 0xD8
                # Trama de respuesta de agenda de feriados y especial
                obj = RespuestaAgendaFeriadosEspecial()
                return obj.respuesta(trm)

            elif dec == 218:
                # 0xDA
                # Respuesta Envío de agenda anual
                obj = RespuestaAgendAnual()
                return obj.respuesta(trm)

            elif dec == 220:
                # 0xDC
                # Trama de respuesta de agenda diaria
                obj = RespuestaAgendaDiaria()
                return obj.respuesta(trm)

            elif dec == 214:
                # 0xD6
                # Respuesta Envío de programa de tiempos
                obj = RespuestaProgramaTiempos()
                return obj.respuesta(trm)

            elif dec == 210:
                # 0xD2
                # Respuesta Envío de funciones
                obj = RespuestaFunciones()
                return obj.respuesta(trm)

            elif dec == 208:
                # 0xD0
                # Respuesta Envío matriz de conflictos
                obj = RespuestaMatrizConflictos()
                return obj.respuesta(trm)

            elif dec == 206:
                # 0xCE
                # Respuesta Envío de estructura (parte baja)
                obj = RespuestaEstrucutraParteBaja()
                return obj.respuesta(trm)

            elif dec == 205:
                # 0xCD
                # Respuesta Envío de estructura (parte alta)
                obj = RespuestaEstrucutraParteAlta()
                return obj.respuesta(trm)

            else:
                return None


if __name__ == "__main__":
    # RespuestaFunciones
    trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D2', 10: '00', 11: '10',
             12: '3C', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
             18: '20', 19: '00', 20: 'FF'}

    # Grabacion EEPROM
    trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'E2', 10: '00', 11: '16',
             12: '0A', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
             18: '20', 19: '00', 20: '03', 21: '00', 22: '10', 23: '00',
             24: '10', 25: 'EA', 26: '20'}

    # RespuestaPreajustes
    trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D4', 10: '00', 11: '10',
             12: '3A', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
             18: '20', 19: '00', 20: 'F9'}

    # RespuestaAgendaFeriadosEspecial
    trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D8', 10: '00', 11: '10',
             12: '36', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
             18: '20', 19: '00', 20: 'F5'}

    rta = Respuesta()
    resultado = rta.obtenerRespuesta(trama)
    print(resultado)
