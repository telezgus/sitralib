# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *


class Fecha:
  def __init__(self):
    self.helpers = Helpers()

  def fecha(self, **kwargs):
    """
    Obtiene la fecha y la retorna en los diferentes formatos segun la app
    :param kwargs: dict
    :return: dict
    """
    timestamp = self.__normalizar_fecha(**kwargs)
    kwargs.update({
      'timestamp': timestamp,
      'wday': self.__day_of_week(kwargs["wday"])
    })
    return kwargs

  def __normalizar_fecha(self, **kwargs):
    """Agrega timestamp y wday a la fecha.

    :param kwargs: dict
    :return: dict
    """
    date_separator = '-'
    time_separator = ':'
    datetime = "{year}{dsep}{month}{dsep}{day}T" \
           "{hour}{tsep}{minutes}{tsep}{seconds}".format(
      dsep=date_separator,
      tsep=time_separator,
      **kwargs
    )
    return datetime

  def __day_of_week(self, tm_wday):
    """
    Retorna el dia de la semana. Español unicamente.
    :param tm_wday: integer
    :return: string
    """
    wday = self.helpers.hexToDec(tm_wday)
    dias = {
      1: 'domingo',
      2: 'lunes',
      3: 'martes',
      4: 'miércoles',
      5: 'jueves',
      6: 'viernes',
      7: 'sábado'
    }
    return dias[wday]


if __name__ == "__main__":
  help_text = """
  Retorna un diccionario con los datos indexados y
  la fecha en formato timestamp (ISO)
  Ejemplo:

    a = Fecha()
    b = a.fecha('2015', '05', '09', '06', '29', '00', '01')
    print(b)
  """
  print(help_text)
  a = Fecha()
  b = a.fecha(
    year='2015',
    month='05',
    day='09',
    hour='06',
    minutes='29',
    seconds='00',
    wday='01'
  )
  print(b)
