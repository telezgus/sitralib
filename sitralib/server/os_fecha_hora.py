# -*- coding: utf-8 -*-
import os
import sys


class OsFechaHora:
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

    elif s == 3:
      try:
        os.system(
          'date {mon}{mday}{hour}{min}{year}.{sec}'.format(
            **self.kwargs
          )
        )
      except:
        print('No es posible imponer la Fecha y la hora del servidor.')

    else:
      print('Parámetro equivocado')


  def check_os(self):
    if sys.platform == 'linux2' or sys.platform == 'linux':
      self.change(1)
    elif sys.platform == 'win32':
      self.change(2)
    elif sys.platform == 'darwin':
      self.change(3)
    else:
      print(
        'El sistema operativo ({0}), no se encuentra activado.'.format(
          sys.platform
        )
      )


if __name__ == '__main__':
  d = OsFechaHora(
    year=2017,
    mon='04',
    mday='04',
    wday='04',
    hour='06',
    min='20',
    sec='00',
    mis='00'
  )
  d.check_os()
