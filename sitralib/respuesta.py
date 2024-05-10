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