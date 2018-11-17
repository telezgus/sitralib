# -*- coding: utf-8 -*-
from sitralib.respuesta_consulta_gurpo_extendido import *
from sitralib.respuesta_consulta_puesto_conteo import *
from sitralib.respuesta_envio_comando import *
from sitralib.respuesta_estado_envio_comando import *

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
from sitralib.respuesta_consulta_estructura_parte_baja import *
from sitralib.helpers.ordenar_trama import *
from sitralib.respuesta_consulta_funciones import *
from sitralib.respuesta_consulta_matriz_conflictos import *
from sitralib.respuesta_envio_programa_tiempos import *
from sitralib.respuesta_consulta_agenda_diaria import *
from sitralib.respuesta_consulta_agenda_anual_semanal import *
from sitralib.respuesta_consulta_agenda_feriados_especial import *
from sitralib.respuesta_consulta_preajustes import *
from sitralib.respuesta_consulta_estructura_parte_alta import *

class Respuesta(object):
  def __init__(self):
    self.helpers = Helpers()
    self.ordtrama = OrdenarTrama()

  def obtenerRespuesta(self, trama):
    trm = self.ordtrama.ordenarTrama(trama)


    try:
      dec = self.helpers.hexToDec(trm[9])
      if dec == 201:
        obj = RespuestaEnvioComando()
        return obj.get(trm)

      elif dec == 200:
        obj = RespuestaConsultaGrupoExtendido()
        return obj.get(trm)

      elif dec == 197:
        obj = RespuestaEstadoEnvioComando()
        return obj.get(trm)

      elif dec == 224:
        obj = RespuestaConsultaPuestoConteo()
        return obj.get(trm)

      elif dec == 226:
        # 0xE2
        # Trama de grabación de EEPROM
        obj = GrabacionEeprom()
        return obj.grabar(trm)

      elif dec == 212:
        # 0xD4
        # Trama de respuesta de envio de preajustes
        obj = RespuestaPreajustes()
        return obj.get(trm)

      elif dec == 216:
        # 0xD8
        # Trama de respuesta de agenda de feriados y especial
        obj = RespuestaAgendaFeriadosEspecial()
        return obj.get(trm)

      elif dec == 218:
        # 0xDA
        # Respuesta Envío de agenda anual
        obj = RespuestaAgendAnual()
        return obj.get(trm)

      elif dec == 220:
        # 0xDC
        # Trama de respuesta de agenda diaria
        obj = RespuestaAgendaDiaria()
        return obj.get(trm)

      elif dec == 214:
        # 0xD6
        # Respuesta Envío de programa de tiempos
        obj = RespuestaProgramaTiempos()
        return obj.get(trm)

      elif dec == 210:
        # 0xD2
        # Respuesta Envío de funciones
        obj = RespuestaFunciones()
        return obj.get(trm)

      elif dec == 208:
        # 0xD0
        # Respuesta Envío matriz de conflictos
        obj = RespuestaMatrizConflictos()
        return obj.get(trm)

      elif dec == 206:
        # 0xCE
        # Respuesta Envío de estructura (parte baja)
        obj = RespuestaEstrucutraParteBaja()
        return obj.get(trm)

      elif dec == 205:
        # 0xCD
        # Respuesta Envío de estructura (parte alta)
        obj = RespuestaEstrucutraParteAlta()
        return obj.get(trm)

      # OBTENCION DE ESTRUCTURA
      elif dec == 203:
        # 0xCB
        # Respuesta de consulta estructura (parte alta).
        obj = RespuestaConsultaEstructuraParteAlta()
        return obj.get(trm)

      elif dec == 204:
        # 0xCC
        # Trama de respuesta de consulta estructura (parte baja)
        obj = RespuestaConsultaEstructuraParteBaja()
        return obj.get(trm)

      elif dec == 207:
        # 0xCF
        # Trama de respuesta a consulta de matriz de conflictos
        obj = RespuestaConsultaMatrizConflictos()
        return obj.get(trm)

      elif dec == 209:
        # 0xD1
        # Trama de respuesta a consulta de funciones
        obj = RespuestaConsultaFunciones()
        return obj.get(trm)

      elif dec == 213:
        # 0xD5
        #  Trama de respuesta de envío de programa de tiempos
        obj = RespuestaEnvioProgramaTiempos()
        return obj.get(trm)

      elif dec == 219:
        # 0xDB
        # Trama de respuesta de consulta de agenda diaria
        obj = RespuestaConsultaAgendaDiaria()
        return obj.get(trm)

      elif dec == 217:
        # 0xD9
        # Trama de Respuesta consulta de agenda anual semanal
        obj = RespuestaConsultaAgendaAnualSemanal()
        return obj.get(trm)

      elif dec == 215:
        # 0xD7
        # Trama de respuesta consulta de agenda feriados y especial
        obj = RespuestaConsultaAgendaFeriadosEspecial()
        return obj.get(trm)

      elif dec == 211:
        # 0xD3
        # Trama de consulta de preajustes
        obj = RespuestaConsultaPreajustes()
        return obj.get(trm)

    except:
      return None


if __name__ == "__main__":
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

  rta = Respuesta()
  resultado = rta.obtenerRespuesta(trama33)
  print(resultado)
