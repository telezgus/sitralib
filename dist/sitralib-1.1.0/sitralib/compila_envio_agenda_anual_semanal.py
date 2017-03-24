from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *
from collections import *
import time

ASE_DEFAULT = {
	'domingo': '00',
	'lunes': '00',
	'martes': '00',
	'miercoles': '00',
	'jueves': '00',
	'viernes': '00',
	'sabado': '00'
}


class CompilaEnvioAgendaAnualSemanal(object):
	"""
	Envio Agenda Diaria
	x78
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
		trama[9] = '76'  # Codigo según Protocolo
		trama[10] = '00'
		trama[11] = '83'
		trama[12] = '00'  # BCC intermedio
		trama[13] = numeroControlador[:-2]
		trama[14] = numeroControlador[-2:]

		# Agendas anuales
		ase = self.__set_agendas_anuales(kwargs['agendas_anuales_semanas'])
		counter = 15
		for i in ase:
			trama[counter] = i
			counter += 1

		# Numero de las agendas
		trama[39] = '00'
		trama[40] = '01'
		trama[41] = '02'
		trama[42] = '03'
		trama[43] = '04'
		trama[44] = '05'
		trama[45] = '06'
		trama[46] = '07'
		trama[47] = '08'
		trama[48] = '09'
		trama[49] = '0A'
		trama[50] = '0B'

		sem = self.__set_agendas_semanales(kwargs['agendas_semanales'])
		counter = 51
		for valor in sem:
			trama[counter] = valor
			counter += 1

		trama[135] = '00'  # BCC final

		trama_consolidada = self.bcc.consolidate(trama)
		if trama_consolidada:
			return ' '.join(trama_consolidada.values())
		return None

	def __set_agendas_anuales(self, data):
		l = []
		for i in range(0, 12):
			l.append(self.__set_mes_cambio(i, data))
			l.append(self.__set_dia_cambio(i, data))

		return l

	def __set_mes_cambio(self, key, data):
		"""
		Retorna el dia
		:param key: Clave
		:param data: Diccionario
		:return: string
		"""
		try:
			ans_mes = data[key]['ans_mes']
			return str(ans_mes).zfill(2)
		except:
			return '7F'

	def __set_dia_cambio(self, key, data):
		"""
		Retorna el me
		:return: string
		"""
		try:
			ans_dia = data[key]['ans_dia']
			return str(ans_dia).zfill(2)
		except:
			return 'FF'

	def __set_agendas_semanales(self, data):
		ase_num = []
		for i in range(0, 12):
			ase_num.append(self.__set_dia(data, i, "domingo"))
			ase_num.append(self.__set_dia(data, i, "lunes"))
			ase_num.append(self.__set_dia(data, i, "martes"))
			ase_num.append(self.__set_dia(data, i, "miercoles"))
			ase_num.append(self.__set_dia(data, i, "jueves"))
			ase_num.append(self.__set_dia(data, i, "viernes"))
			ase_num.append(self.__set_dia(data, i, "sabado"))

		return ase_num

	def __set_dia(self, data, key, dia):
		"""
		Retorna el dia
		:return: string
		"""
		try:
			val = str(data[key][dia])
			return self.helpers.intToHexString(val)
		except:
			return ASE_DEFAULT[dia]


if __name__ == "__main__":
	o = CompilaEnvioAgendaDiaria()
	o.set_cambios()
