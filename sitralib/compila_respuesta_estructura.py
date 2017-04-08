from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaEstructura(object):
	def __init__(self, tramas):
		self.helpers = Helpers()
		self.trm = tramas

	def compile(self):
		alta = self.helpers.tramas_by_codigo(tramas=self.trm, codigo='CB')
		baja = self.helpers.tramas_by_codigo(tramas=self.trm, codigo='CC')

		listado_alta = {}
		for i in alta:
			numero_estructura = int(i['20'], 16)
			intervalos = self.__intervalos(trama=i)

			listado_alta.update({
				numero_estructura:
					self.__movimientos_por_intervalo(intervalos=intervalos)
			})

		listado_baja = list()
		for i in baja:
			intervalos = self.__intervalos(trama=i)
			listado_baja.append(
				self.__movimientos_por_intervalo(intervalos=intervalos)
			)

		r = list()
		for i in range(3):
			r.append(self.combine_array(listado_alta[i], listado_baja[i]))

		return r

	def __movimientos_por_intervalo(self, **kwargs):

		f = {}
		mov = defaultdict(dict)
		for i in kwargs['intervalos']:
			intervalos = kwargs['intervalos'][i]
			counter = 0
			for x in range(8):
				counter += 1
				mov[i][counter] = self.helpers.getNibbles(
					intervalos[x], 2)['lo']
				counter += 1
				mov[i][counter] = self.helpers.getNibbles(
					intervalos[x], 2)['hi']

			f[i] = intervalos[8]

		fun = [f[i] for i in f]

		c = 0
		est = {}

		# defino los valores por defecto
		for x in range(1, 17):
			key = 'mov-{0}'.format(x)
			est.update({key: []})

		for i in range(len(mov)):
			for x in range(1, 17):
				key = 'mov-{0}'.format(x)
				try:
					# print(key, c,  x, mov[c][x])
					est[key].append(mov[c][x])
				except:
					print(c, key)

			c += 1
		est.update({'fun': fun})

		return est

	def __slice(self, **kwargs):
		trama_sliced = dict()
		for i in kwargs['trama']:
			validate = self.helpers.validateBetween(
				max=254, min=21, number=i
			)
			if validate:
				trama_sliced[i] = kwargs['trama'][i]
		return trama_sliced

	def __intervalos(self, **kwargs):
		"""
		Separa la colección de datos en intervalos.
		$trama dict
		:return: dict
		"""
		counter = 0
		idx = 0
		mov = dict()
		# Verificacion
		trama = dict()

		# print( kwargs['trama'])
		# print('\n')

		for i in range(5, 256):
			try:
				key = str(i) if str(i) in kwargs['trama'] else i
				trama[i] = kwargs['trama'][key]
			except:
				print(i)

		trama_sliced = self.__slice(trama=trama)
		a = list()
		for i in trama_sliced:

			if counter == 13:
				a = list()
				counter = 0
				idx += 1

			a.append(trama[i])
			mov[idx] = a
			counter += 1

		return mov

	def combine_array(self, alta, baja):
		e = {}
		for key in alta:
			for i in range(18):
				alta[key].append(baja[key][i])

		return alta

