from distutils.core import setup

setup(
	name='sitralib',
	version='1.1.4',
	py_modules=[
		'sitralib.server.os_fecha_hora',
		'sitralib.validators.bcc',
		'sitralib.helpers.fecha',
		'sitralib.helpers.byte',
		'sitralib.helpers.funciones',
		'sitralib.helpers.ordenar_trama',
		'sitralib.bits_alarma',
		'sitralib.bits_status_i',
		'sitralib.bits_status_ii',
		'sitralib.bits_status_iii',
		'sitralib.byte_funcion',
		'sitralib.byte_lamparas',
		'sitralib.byte_status',
		'sitralib.compila_envio_agenda_anual_semanal',
		'sitralib.compila_envio_agenda_diaria',
		'sitralib.compila_envio_agenda_feriados_especial',
		'sitralib.compila_envio_estructura_parte_alta',
		'sitralib.compila_envio_estructura_parte_baja',
		'sitralib.compila_envio_funciones',
		'sitralib.compila_envio_grabacion_eeprom',
		'sitralib.compila_envio_matriz_conflictos',
		'sitralib.compila_envio_preajustes',
		'sitralib.compila_envio_programa_tiempos',
		'sitralib.compila_respuesta_agendas_anuales_semanales',
		'sitralib.compila_respuesta_agendas_diarias',
		'sitralib.compila_respuesta_agendas_feriados_especial',
		'sitralib.compila_respuesta_estructura',
		'sitralib.compila_respuesta_programa_tiempos',
		'sitralib.consulta_agenda_anual_semanal',
		'sitralib.consulta_agenda_diaria',
		'sitralib.consulta_agenda_feriados_especial',
		'sitralib.consulta_estado_envio_comando',
		'sitralib.consulta_estado_extendido',
		'sitralib.consulta_estructura_parte_alta',
		'sitralib.consulta_estructura_parte_baja',
		'sitralib.consulta_funciones',
		'sitralib.consulta_matriz_conflicto',
		'sitralib.consulta_preajustes',
		'sitralib.consulta_programa_tiempos',
		'sitralib.consulta_puesto_conteo',
		'sitralib.envio_agenda_diaria',
		'sitralib.envio_comando',
		'sitralib.envio_funciones',
		'sitralib.envio_grabacion_eeprom',
		'sitralib.envio_matriz_conflictos',
		'sitralib.grabacion_eeprom',
		'sitralib.imposicion_fecha_hora',
		'sitralib.referencias',
		'sitralib.reporte_estado',
		'sitralib.respuesta_agenda_anual',
		'sitralib.respuesta_agenda_diaria',
		'sitralib.respuesta_agenda_feriados_especial',
		'sitralib.respuesta_consulta_agenda_anual_semanal',
		'sitralib.respuesta_consulta_agenda_diaria',
		'sitralib.respuesta_consulta_agenda_feriados_especial',
		'sitralib.respuesta_consulta_estructura_parte_alta',
		'sitralib.respuesta_consulta_estructura_parte_baja',
		'sitralib.respuesta_consulta_funciones',
		'sitralib.respuesta_consulta_gurpo_extendido',
		'sitralib.respuesta_consulta_matriz_conflictos',
		'sitralib.respuesta_consulta_preajustes',
		'sitralib.respuesta_consulta_puesto_conteo',
		'sitralib.respuesta_envio_comando',
		'sitralib.respuesta_envio_estructura_parte_alta',
		'sitralib.respuesta_envio_programa_tiempos',
		'sitralib.respuesta_estado_envio_comando',
		'sitralib.respuesta_estrucutra_parte_alta',
		'sitralib.respuesta_estrucutra_parte_baja',
		'sitralib.respuesta_funciones',
		'sitralib.respuesta_matriz_conflictos',
		'sitralib.respuesta_preajustes',
		'sitralib.respuesta_programa_tiempos',
		'sitralib.respuesta',
		'sitralib.generador_tramas_captura',
		'sitralib.generador_tramas_grabacion',
		'sitralib.respuesta_imposicion_fecha_hora.py'
	],
	author='Agustin Bouillet',
	author_email='agustin.bouillet@gmail.com',
	url='http://www.bouillet.com.ar/',
	description='Libreria SITRA',
	# long_description = """Really long text here."""
)
