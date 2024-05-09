# -*- coding: utf-8 -*-
from sitralib.grabacion_eeprom import *
from sitralib.helpers.ordenar_trama import *
from sitralib.respuesta_agenda_anual import *
from sitralib.respuesta_agenda_diaria import *
from sitralib.respuesta_agenda_feriados_especial import *
from sitralib.respuesta_consulta_agenda_anual_semanal import *
from sitralib.respuesta_consulta_agenda_diaria import *
from sitralib.respuesta_consulta_agenda_feriados_especial import *
from sitralib.respuesta_consulta_estructura_parte_alta import *
from sitralib.respuesta_consulta_estructura_parte_baja import *
from sitralib.respuesta_consulta_funciones import *
from sitralib.respuesta_consulta_gurpo_extendido import *
from sitralib.respuesta_consulta_matriz_conflictos import *
from sitralib.respuesta_consulta_preajustes import *
from sitralib.respuesta_consulta_puesto_conteo import *
from sitralib.respuesta_envio_comando import *
from sitralib.respuesta_envio_programa_tiempos import *
from sitralib.respuesta_estado_envio_comando import *
from sitralib.respuesta_estrucutra_parte_alta import *
from sitralib.respuesta_estrucutra_parte_baja import *
from sitralib.respuesta_funciones import *
from sitralib.respuesta_matriz_conflictos import *
from sitralib.respuesta_preajustes import *
from sitralib.respuesta_programa_tiempos import *
from sitralib.unem_respuesta_estado_envio_comando import *
from sitralib.unem_respuesta_forzadura_ciclo import *
from sitralib.unem_respuesta_forzadura_desfazaje import *
from sitralib.unem_respuesta_forzadura_fases import *
from sitralib.unev_respuesta_estado_envio_comando import *
from sitralib.unev_respuesta_forzadura_ciclo import *
from sitralib.unev_respuesta_forzadura_desfazaje import *
from sitralib.unev_respuesta_forzadura_fases import *


class Respuesta:
    def __init__(self):
        self.helpers = Helpers()
        self.ordtrama = OrdenarTrama()


    def obtenerRespuesta(self, trama):
        respuesta = None

        if trama:
            try:
                trm = self.ordtrama.ordenarTrama(trama)
                dec = self.helpers.hexToDec(trm.get(9))

                dispatch = {
                    201: RespuestaEnvioComando().get,
                    200: RespuestaConsultaGrupoExtendido().get,
                    197: RespuestaEstadoEnvioComando().get,
                    224: RespuestaConsultaPuestoConteo().get,
                    226: GrabacionEeprom().grabar,
                    212: RespuestaPreajustes().get,
                    216: RespuestaAgendaFeriadosEspecial().get,
                    218: RespuestaAgendAnual().get,
                    220: RespuestaAgendaDiaria().get,
                    214: RespuestaProgramaTiempos().get,
                    210: RespuestaFunciones().get,
                    208: RespuestaMatrizConflictos().get,
                    206: RespuestaEstrucutraParteBaja().get,
                    205: RespuestaEstrucutraParteAlta().get,
                    203: RespuestaConsultaEstructuraParteAlta().get,
                    204: RespuestaConsultaEstructuraParteBaja().get,
                    207: RespuestaConsultaMatrizConflictos().get,
                    209: RespuestaConsultaFunciones().get,
                    213: RespuestaEnvioProgramaTiempos().get,
                    219: RespuestaConsultaAgendaDiaria().get,
                    217: RespuestaConsultaAgendaAnualSemanal().get,
                    215: RespuestaConsultaAgendaFeriadosEspecial().get,
                    211: RespuestaConsultaPreajustes().get,
                    # UNE M
                    183: UnemRespuestaForzaduraCiclo().get,
                    181: UnemRespuestaForzaduraDesfazaje().get,
                    182: UnemRespuestaForzaduraFases().get,
                    185: UnemRespuestaEstadoEnvioComando().get,
                    # UNE V
                    179: UnevRespuestaForzaduraCiclo().get,
                    177: UnevRespuestaForzaduraDesfazaje().get,
                    178: UnevRespuestaForzaduraFases().get,
                    184: UnevRespuestaEstadoEnvioComando().get,
                }
 
                respuesta = dispatch[dec](trm)
            except KeyError:
                pass
            except:
                print("Se produjo un error en la libreria SITRALIB / Respuesta")

            return respuesta



if __name__ == "__main__":
    import pprint as pp

    # RespuestaFunciones
    trama = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D2', 10: '00', 11: '10',
        12: '3C', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
        18: '20', 19: '00', 20: 'FF'}

    # Grabacion EEPROM
    trama33 = {5: 'FF', 6: '00', 7: '00', 8: '01', 99: 'E2', 10: '00', 11: '16',
            12: '0A', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
            18: '20', 19: '00', 20: '03', 21: '00', 22: '10', 23: '00',
            24: '10', 25: 'EA', 26: '20'}

    # RespuestaPreajustes
    trama3 = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D4', 10: '00', 11: '10',
            12: '3A', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
            18: '20', 19: '00', 20: 'F9'}

    # RespuestaAgendaFeriadosEspecial
    trama5 = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'D8', 10: '00', 11: '10',
            12: '36', 13: '0B', 14: 'B8', 15: '00', 16: '10', 17: '40',
            18: '20', 19: '00', 20: 'F5'}

    trama_6 = []
    trama_7 = {}
    trama_8 = None

    rta = Respuesta()
    resultado = rta.obtenerRespuesta(trama3)
    pp.pprint(resultado)



