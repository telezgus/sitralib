from sitralib.helpers.funciones import *
from sitralib.helpers.ordenar_trama import *

"""
Validacion
12 es la posición de la primer validación. Los XOR sumados desde el
primer número hasta el valor previo a la posición 12, deben dar como resultado
el valor expresado en la posición 12.

Y la suma desde la posición a la ante-ultima debe dar el resultado expresado en
el valor final
"""


class Bcc(object):
	POSICION_BCC_INTERMEDIO = 12

	def __init__(self):
		self.helpers = Helpers()

	def trama_to_type(self, trama):
		if type(trama) == str:
			ordenar = OrdenarTrama()
			return ordenar.ordenarTrama(trama)

		return trama

	def isValidBcc(self, trama, *args):

		trama = self.trama_to_type(trama)

		bcc1 = self.POSICION_BCC_INTERMEDIO
		bcc2 = self.__posicion_bcc2(trama)

		b1 = self.validateBccIntermadio(trama)
		b2 = self.validateBccFinal(trama, bcc2)

		if bcc1 and bcc2 in trama.keys():
			if self.helpers.hexToDec(trama[bcc1]) == self.helpers.hexToDec(
					b1) and self.helpers.hexToDec(
				trama[bcc2]) == self.helpers.hexToDec(b2):
				return True
			else:
				return False

		return False

	def validateBccIntermadio(self, trama, *args):
		bcc1 = 0
		for i in trama:
			if i == self.POSICION_BCC_INTERMEDIO:
				break
			else:
				bcc1 = bcc1 ^ self.helpers.hexToDec(trama[i])
		return self.helpers.intToHexString(bcc1)

	def validateBccFinal(self, trama, *args):

		bcc_final_position = self.__posicion_bcc2(trama)

		bcc2 = 0
		# al len de la trama hay que sumarle 4 por los 00 hasta FF,
		# luego al range se le suma 1 porque los key comienzan en 0
		for i in range(self.POSICION_BCC_INTERMEDIO, (len(trama) + 5)):
			if i in trama:
				if i == bcc_final_position: break
				bcc2 = bcc2 ^ self.helpers.hexToDec(trama[i])
			else:
				return None

		return self.helpers.intToHexString(bcc2)

	def consolidate(self, trama):
		bcc1 = self.validateBccIntermadio(trama)
		trama[self.POSICION_BCC_INTERMEDIO] = bcc1

		bcc2 = self.validateBccFinal(trama)
		trama[self.__posicion_bcc2(trama)] = bcc2

		if self.isValidBcc(trama):
			return trama
		else:
			return False

	def __posicion_bcc2(self, trama):
		"""
		Retorna el indice para la posicion del bcc2 en la trama
		:param trama: dict
		:return: integer
		"""
		# Cuento el comienzo del diccionario y le resto 1, porque el
		# valor (segun protocolo), inicia en cero.
		return 5 + (self.__longitud_total(trama) - 1)

	def __longitud_total(self, trama):
		"""
		Obtengo la posicion para el bcc2
		:param trama:
		:return: integer
		"""
		if 10 and 11 in trama:
			return int(trama[10] + trama[11], 16)

		return 0


if __name__ == "__main__":
	trama1 = '00 00 00 00 FF 00 00 1E 64 00 0B 8E 07 84 0D'
	# trama1 = '00 00 00 00 FF 00 00 1E 64 00 0B 8E 07 85 0D'
	# trama1 = "00 00 00 00 FF 00 00 01 69 00 F6 61 0B B8 00 04 41 00 00 00 00 00 00 01 00 00 00 00 04 41 00 00 00 00 00 00 00 00 00 00 00 02 21 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 01 14 00 00 00 00 00 00 00 00 00 00 00 01 19 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 43 31 00 00 00 00 00 00 05 00 00 00 FF A9 32 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 EE"

	# Necesito procesar la trama para convertirla en Diccionario
	n = {
		5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'CB', 10: '00', 11: 'FB',
		12: 'CE', 13: '0B', 14: 'B8', 15: '0B', 16: '10', 17: '00', 18: '20',
		19: '00', 20: '00', 21: '04', 22: '41', 23: '00', 24: '00', 25: '00',
		26: '00', 27: '00', 28: '00', 29: '01', 30: '00', 31: '00', 32: '00',
		33: '00', 34: '04', 35: '41', 36: '00', 37: '00', 38: '00', 39: '00',
		40: '00', 41: '00', 42: '00', 43: '00', 44: '00', 45: '00', 46: '00',
		47: '02', 48: '21', 49: '00', 50: '00', 51: '00', 52: '00', 53: '00',
		54: '00', 55: '00', 56: '00', 57: '00', 58: '00', 59: '00', 60: '01',
		61: '11', 62: '00', 63: '00', 64: '00', 65: '00', 66: '00', 67: '00',
		68: '00', 69: '00', 70: '00', 71: '00', 72: '00', 73: '01', 74: '14',
		75: '00', 76: '00', 77: '00', 78: '00', 79: '00', 80: '00', 81: '00',
		82: '00', 83: '00', 84: '00', 85: '00', 86: '01', 87: '19', 88: '00',
		89: '00', 90: '00', 91: '00', 92: '00', 93: '00', 94: '00', 95: '00',
		96: '00', 97: '00', 98: '00', 99: '01', 100: '11', 101: '00', 102: '00',
		103: '00', 104: '00', 105: '00', 106: '00', 107: '00', 108: '00',
		109: '00', 110: '00', 111: '00', 112: '43', 113: '31', 114: '00',
		115: '00', 116: '00', 117: '00', 118: '00', 119: '00', 120: '00',
		121: '00', 122: '00', 123: '00', 124: '00', 125: 'A9', 126: '32',
		127: '00', 128: '00', 129: '00', 130: '00', 131: '00', 132: '00',
		133: '05', 134: '00', 135: '00', 136: '00', 137: 'FF', 138: '00',
		139: '00', 140: '00', 141: '00', 142: '00', 143: '00', 144: '00',
		145: '00', 146: '00', 147: '00', 148: '00', 149: '00', 150: '00',
		151: '00', 152: '00', 153: '00', 154: '00', 155: '00', 156: '00',
		157: '00', 158: '00', 159: '00', 160: '00', 161: '00', 162: '00',
		163: '00', 164: '00', 165: '00', 166: '00', 167: '00', 168: '00',
		169: '00', 170: '00', 171: '00', 172: '00', 173: '00', 174: '00',
		175: '00', 176: '00', 177: '00', 178: '00', 179: '00', 180: '00',
		181: '00', 182: '00', 183: '00', 184: '00', 185: '00', 186: '00',
		187: '00', 188: '00', 189: '00', 190: '00', 191: '00', 192: '00',
		193: '00', 194: '00', 195: '00', 196: '00', 197: '00', 198: '00',
		199: '00', 200: '00', 201: '00', 202: '00', 203: '00', 204: '00',
		205: '00', 206: '00'
		}
	t = '00 00 00 00 FF 00 00 01 72 00 48 C4 0B B8 0F 00 00 00 00 00 00 7F FF 7F FF 7F FF 7F FF 7F FF 7F FF 7F FF 7F FF 7F FF F8 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
	a = Bcc()
	b = a.isValidBcc(t)
	print(b)
