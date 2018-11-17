# -*- coding: utf-8 -*-
import time
from sitralib.validators.bcc import *


class ImposicionFechaHora(object):
  """
  Trama de imposición fecha y hora desde CC hacia EC
  0x66
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):
    numeroControlador = self.helpers.intToHexString(
      kwargs['crs_numero'],
      4
    )
    tme = time.strptime(
      kwargs['datetime'],
      "%Y-%m-%d %H:%M:%S"
    )

    trama = {
      1: '00',
      2: '00',
      3: '00',
      4: '00',
      5: 'FF',
      6: '00',
      7: '00',
      8: self.helpers.intToHexString(kwargs['grp_id_num']),
      9: '66',  # Codigo según Protocolo
      10: '00',
      11: '12',
      12: '00',  # BCC intermedio
      13: numeroControlador[:-2],
      14: numeroControlador[-2:],
      15: self.__zFill(tme.tm_year)[2:4],  # Año
      16: self.__zFill(tme.tm_mon),  # Mes
      17: self.__zFill(tme.tm_mday),  # Día
      18: self.__zFill(tme.tm_hour),  # hora
      19: self.__zFill(tme.tm_min),  # Minutos
      20: self.__zFill(tme.tm_sec),  # Segundos
      21: self.__zFill(tme.tm_wday),  # Día de la semana
      22: '00',  # BCC
    }

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None

  def __zFill(self, value):
    return str(value).zfill(2)


if __name__ == '__main__':
  import datetime

  # Ejemplo
  date = datetime.datetime.now()
  date_now = date.strftime('%Y-%m-%d %H:%M:%S')
  imposicionFechaHora = ImposicionFechaHora()
  trama = imposicionFechaHora.create(
    grp_id_num=30,
    crs_numero=3000,
    datetime=date_now
  )
  print(trama)
