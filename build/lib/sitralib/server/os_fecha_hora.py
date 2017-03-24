import os
import sys


class OsFechaHora(object):
	"""
	Modifica la fecha y la hora del servidor
	"""

	def __init__(self, **kwargs):
		self.kwargs = kwargs

	def to_print(self):
		return '{year}-{mon}-{mday} {hour}:{min}:{sec}'.format(**self.kwargs)

	def change(self, s):
		if s == 1:
			try:
				# os.system('date -s "2016-01-01 00:00:00"')
				os.system(
					'date -s "{year}-{mon}-{mday} {hour}:{min}:{sec}"'.format(
						**self.kwargs
					)
				)
			except:
				print('No es posible imponer la Fecha y la hora del servidor.')

		elif s == 2:
			try:
				import pywin32
			except ImportError:
				print('pywin32 module is missing')
				sys.exit(1)

			pywin32.SetSystemTime(
				year, month, dayOfWeek, day, hour, minute, second, millisecond
			)
		else:
			print('Parámetro equivocado')

	def check_os(self):
		if sys.platform == 'linux2' or sys.platform == 'linux':
			change(1)
		elif sys.platform == 'win32':
			change(2)
		elif sys.platform == 'darwin':
			print('Mac no se reconoce')
		else:
			print(
				'El sistema operativo ({0}), no se encuentra activado.'.format(
					sys.platform
				))


if __name__ == '__main__':
	d = OsFechaHora(
		year=2017,
		mon=12,
		mday=17,
		wday=4,
		hour=2,
		min=0,
		sec=0,
		mis=0
	)
	d.check_os()
