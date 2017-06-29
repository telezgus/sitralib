from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *
from collections import *
import time, datetime

DIA_ANULADO = '7F'
MES_ANULADO = 'FF'
ADI_DEFAULT = '00'


class CompilaEnvioAgendaFeriadosEspecial(object):
	"""
	Envio Agenda Feriados y especial
	x74
	"""

	def __init__(self):
		self.helpers = Helpers()
		self.bcc = Bcc()

	def create(self, **kwargs):
		numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

		trama = defaultdict(dict)
		trama[1] = '00'
		trama[2] = '00'
		trama[3] = '00'
		trama[4] = '00'
		trama[5] = 'FF'
		trama[6] = '00'
		trama[7] = '00'
		trama[8] = self.helpers.intToHexString(kwargs['grp_id_num'])
		trama[9] = '74'  # Codigo según Protocolo
		trama[10] = '00'
		trama[11] = '9B'
		trama[12] = '00'  # BCC intermedio
		trama[13] = numeroControlador[:-2]
		trama[14] = numeroControlador[-2:]

		agendas_especiales = self.__set_agenda_especial_cambio(
			data=kwargs['especiales']
		)
		agendas_feriados = self.__set_agenda_feriado_cambio(
			data=kwargs['feriados']
		)

		c = 15
		for value in self.__set_dias_meses(agendas_especiales):
			trama[c] = value
			c += 1

		c = 47
		for value in self.__set_dias_meses(agendas_feriados):
			trama[c] = value
			c += 1

		c = 111
		for value in self.__set_agendas_diarias(agendas_especiales):
			trama[c] = value
			c += 1

		c = 127
		for value in self.__set_agendas_diarias(agendas_feriados):
			trama[c] = value
			c += 1


		trama[159] = '00'  # BCC final

		trama_consolidada = self.bcc.consolidate(trama)
		if trama_consolidada:
			return ' '.join(trama_consolidada.values())
		return None

	def __set_dia_mes(self, key, data):
		a = defaultdict(dict)

		try:
			fecha = time.strptime(str(data[key]['fer_fecha']), '%Y-%m-%d')
			mes = str(fecha.tm_mon).zfill(2)
			dia = str(fecha.tm_mday).zfill(2)
			a['dia'] = dia
			a['mes'] = mes
			a['adi'] = self.helpers.intToHexString(data[key]['adi_id_num'])
		except:
			a['dia'] = DIA_ANULADO
			a['mes'] = MES_ANULADO
			a['adi'] = ADI_DEFAULT

		return a

	def __set_agenda_especial_cambio(self, data):
		return [self.__set_dia_mes(i, data) for i in range(0, 16)]

	def __set_agenda_feriado_cambio(self, data):
		return [self.__set_dia_mes(i, data) for i in range(0, 32)]

	def __set_dias_meses(self, data):
		a = []
		for item in data:
			a.append(item['dia'])
			a.append(item['mes'])
		return a

	def __set_agendas_diarias(self, data):
		return [item['adi'] for item in data]



if __name__ == "__main__":
	d = {
		'feriados': [
			{'diarias__adi_id_num': 3, 'fer_fecha': '2017-05-24', 'fer_id': 1, 'fer_nombre': 'Feriado Test', 'anuales__anu_id': 1, 'feriadotipo': 1}
			],
		'especiales': [
			{
				'feriadotipo': 2,
				'diarias': 2,
				'anuales': 1,
				'adi_id_num' : 2,
				'fer_id': 3,
				'fer_nombre': 'especial test',
				'fer_fecha': '2017-05-24'
				}
			]
	}

	o = CompilaEnvioAgendaFeriadosEspecial()
	result = o.create(
		feriados=d['feriados'],
		especiales=d['especiales'],
		crs_numero=3000,
		grp_id_num=1,
	)

	print(result)
