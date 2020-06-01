# -*- coding: utf-8 -*-
"""
Referencia de codigos
"""
'''
Matriz de codigos de envio y respusta
'''
CONSULTA_RESPUESTA = {
  # PC a Equipo controlador
  '69': 'CD',
  '6A': 'CE',
  '6C': 'D0',
  '6E': 'D2',
  '72': 'D6',
  '78': 'DC',
  '76': 'DA',
  '74': 'D8',
  '70': 'D4',
  '7E': 'E2',
  # Equipo controlador a PC
  '67': 'CB',
  '68': 'CC',
  '6B': 'CF',
  '6D': 'D1',
  '71': 'D5',
  '77': 'DB',
  '75': 'D9',
  '73': 'D7',
  '6F': 'D3'
}

CODE_REFERENCES = {
  '00': {
    'technical': '',
    'humanize': ''
  },
  '64': {
    'technical': 'Consulta de grupos extendidos',
    'humanize': ''
  },
  '65': {
    'technical': 'Envio comando',
    'humanize': 'Envio comando'
  },
  '66': {
    'technical': 'fecha y hora',
    'humanize': 'fecha y hora'
  },
  '67': {
    'technical': 'Consulta de estructura (parte alta)',
    'humanize': 'Estructura, parte alta'
  },
  '68': {
    'technical': 'Consulta de estructura (parte baja)',
    'humanize': 'Estructura, parte baja'
  },
  '69': {
    'technical': 'Envio de estructura (parte alta)',
    'humanize': 'Estructura, parte alta'
  },
  '6A': {
    'technical': 'Envio de estructura (parte baja)',
    'humanize': 'Estructura, parte baja'
  },
  '6B': {
    'technical': 'Consulta de matriz de conflictos',
    'humanize': 'Matriz de conflictos'
  },
  '6C': {
    'technical': 'Envio de matriz de conflictos',
    'humanize': 'Matriz de conflictos'
  },
  '6D': {
    'technical': 'Consulta de funciones',
    'humanize': 'Funciones'
  },
  '6E': {
    'technical': 'Envio de funciones',
    'humanize': 'Funciones'
  },
  '6F': {
    'technical': 'Consulta de preajustes',
    'humanize': 'Preajustes'
  },
  '70': {
    'technical': 'Envio de preajustes',
    'humanize': 'Preajustes'
  },
  '71': {
    'technical': 'Consulta de programa de tiempos',
    'humanize': 'Tiempo de los programas'
  },
  '72': {
    'technical': 'Envio de programa de tiempos',
    'humanize': 'Tiempo de los programas'
  },
  '73': {
    'technical': 'Consulta de agenda feriados y especial',
    'humanize': 'Agenda feriados y eventos especiales'
  },
  '74': {
    'technical': 'Envio de agenda feriados y especial',
    'humanize': 'Agenda feriados y eventos especiales'
  },
  '75': {
    'technical': 'Consulta de agenda anual',
    'humanize': 'Agenda anual y agendas semanales'
  },
  '76': {
    'technical': 'Envio de agenda anual',
    'humanize': 'Agenda anual y agendas semanales'
  },
  '77': {
    'technical': 'Consulta de agenda diaria',
    'humanize': 'Agendas diarias'
  },
  '78': {
    'technical': 'Envio de agenda diaria',
    'humanize': 'Agendas diarias'
  },
  '79': {
    'technical': 'Consulta de ultimo evento',
    'humanize': 'Consulta de ultimo evento'
  },
  '7A': {
    'technical': 'Consulta de eventos',
    'humanize': 'Consulta de eventos'
  },
  '7D': {
    'technical': 'Envio de contrasena hardware',
    'humanize': 'Envio de contrasena hardware'
  },
  '7E': {
    'technical': 'Envio de grabacion EEPROM',
    'humanize': 'Grabacion de EEPROM'
  },
  'C8': {
    'technical': 'Respuesta consulta de grupos extendidos',
    'humanize': 'Respuesta consulta de grupos extendidos',
  },
  'C9': {
    'technical': 'Respuesta envio comando',
    'humanize': 'Respuesta envio comando'
  },
  'CA': {
    'technical': 'Respuesta envio fecha y hora',
    'humanize': 'Respuesta envio fecha y hora'
  },
  'CB': {
    'technical': 'Respuesta consulta de estructura (parte alta)',
    'humanize': 'Respuesta consulta de estructura (parte alta)'
  },
  'CC': {
    'technical': 'Respuesta consulta de estructura (parte baja)',
    'humanize': 'Respuesta consulta de estructura (parte baja)'
  },
  'CD': {
    'technical': 'Respuesta envio de estructura (parte alta)',
    'humanize': 'Respuesta envio de estructura (parte alta)'
  },
  'CE': {
    'technical': 'Respuesta envio de estructura (parte baja)',
    'humanize': 'Respuesta envio de estructura (parte baja)'
  },
  'CF': {
    'technical': 'Respuesta consulta matriz de conflictos',
    'humanize': ''
  },
  'D0': {
    'technical': 'Respuesta envio matriz de conflictos',
    'humanize': ''
  },
  'D1': {
    'technical': 'Respuesta consulta de funciones',
    'humanize': ''
  },
  'D2': {
    'technical': 'Respuesta envio de funciones',
    'humanize': ''
  },
  'D3': {
    'technical': 'Respuesta consulta de preajustes',
    'humanize': ''
  },
  'D4': {
    'technical': 'Respuesta envio de preajustes',
    'humanize': ''
  },
  'D5': {
    'technical': 'Respuesta consulta de programa de tiempos',
    'humanize': ''
  },
  'D6': {
    'technical': 'Respuesta envio de programa de tiempos',
    'humanize': ''
  },
  'D7': {
    'technical': 'Respuesta consulta de agenda feriados y especial',
    'humanize': ''
  },
  'D8': {
    'technical': 'Respuesta envio de agenda feriados y especial',
    'humanize': ''
  },
  'D9': {
    'technical': 'Respuesta consulta de agenda anual',
    'humanize': ''
  },
  'DA': {
    'technical': 'Respuesta envio de agenda anual',
    'humanize': ''
  },
  'DB': {
    'technical': 'Respuesta consulta de agenda diaria',
    'humanize': ''
  },
  'DC': {
    'technical': 'Respuesta envio de agenda diaria',
    'humanize': ''
  },
  'DD': {
    'technical': 'Respuesta consulta de ultimo evento',
    'humanize': ''
  },
  'DE': {
    'technical': 'Respuesta consulta de eventos',
    'humanize': ''
  },
  'E1': {
    'technical': 'Respuesta envio de contrasena hardware',
    'humanize': ''
  },
  'E2': {
    'technical': 'Respuesta envio de grabacion EEPROM',
    'humanize': ''
  },
}

MENSAJES = {
  1: {
    'tipo': 'advertencia',
    'mensaje': 'TIMEOUT',
  },
  2: {
    'tipo': 'advertencia',
    'mensaje': 'Trama incompleta',
  },
  3: {
    'tipo': 'error',
    'mensaje': 'Falla de conexion',
  },
  4: {
    'tipo': 'error',
    'mensaje': 'No se puede crear el archivo de alertas',
  },
  5: {
    'tipo': 'error',
    'mensaje': 'Error al procesar el archivo extendido',
  },
  6: {
    'tipo': 'error',
    'mensaje': 'No se puede imponer la fecha y hora en el servidor',
  },
  7: {
    'tipo': 'error',
    'mensaje': 'No se puede imponer fecha y hora en el cruce',
  },
  8: {
    'tipo' : 'error',
    'mensaje': "Fallo despues de {0} intentos",
  },
  9: {
    'tipo' : 'error',
    'mensaje': "Trama invalida",
  },
  10: {
    'tipo' : 'exito',
    'mensaje': "Trama correcta",
  },
  11: {
    'tipo' : 'error',
    'mensaje': "Falla de SOCKET",
  },
}


if __name__ == "__main__":
  print(CODE_REFERENCES['71']['humanize'])
