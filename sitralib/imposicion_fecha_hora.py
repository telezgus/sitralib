# -*- coding: utf-8 -*-
import time

from sitralib.validators.bcc import Bcc
from sitralib.helpers.funciones import Helpers

class ImposicionFechaHora:
  """
  Trama de imposición fecha y hora desde CC hacia EC
  0x66
  """
  
  # Modifico el numero de dia de acuerdo con el protocolo SITAR.
  WEEKDAYS = [2, 3, 4, 5, 6, 7, 1]

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

    """"[summary]"

    En la PC CITAR a reemplazar manda un telegrama 0x66 cada 10 minutos con
    los campos siguientes en blanco:
    numero de esclavo = 0x00
    numero de grupo = 0x00
    numero de cruce = 0x00 0x00
    """
    trama = {
      1  : '00',
      2  : '00',
      3  : '00',
      4  : '00',
      5  : 'FF',
      6  : '00',
      7  : kwargs.get("num_esclavo", "00"),
      8  : self.helpers.intToHexString(kwargs['grp_id_num']),
      9  : '66',                            # Codigo según Protocolo
      10 : '00',
      11 : '12',
      12 : '00',                            # BCC intermedio
      13 : numeroControlador[:-2],
      14 : numeroControlador[-2:],
      15 : self.__zFill(tme.tm_year)[2:4],  # Año
      16 : self.__zFill(tme.tm_mon),        # Mes
      17 : self.__zFill(tme.tm_mday),       # Día
      18 : self.__zFill(tme.tm_hour),       # hora
      19 : self.__zFill(tme.tm_min),        # Minutos
      20 : self.__zFill(tme.tm_sec),        # Segundos
      21 : self.__zFill(self.WEEKDAYS[tme.tm_wday]),       # Día de la semana
      # 21 : self.__zFill(tme.tm_wday),       # Día de la semana
      22 : '00',                            # BCC
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

  # date_lun = datetime.datetime.strptime('2020-06-22 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_mar = datetime.datetime.strptime('2020-06-23 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_mie = datetime.datetime.strptime('2020-06-24 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_jue = datetime.datetime.strptime('2020-06-25 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_vie = datetime.datetime.strptime('2020-06-26 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_sab = datetime.datetime.strptime('2020-06-27 00:00:00','%Y-%m-%d %H:%M:%S')
  # date_dom = datetime.datetime.strptime('2020-06-28 00:00:00','%Y-%m-%d %H:%M:%S')

  date_lun = '2020-06-22 00:00:00'
  date_mar = '2020-06-23 00:00:00'
  date_mie = '2020-06-24 00:00:00'
  date_jue = '2020-06-25 00:00:00'
  date_vie = '2020-06-26 00:00:00'
  date_sab = '2020-06-27 00:00:00'
  date_dom = '2020-06-28 00:00:00'

  impf = ImposicionFechaHora()

  trama_lun = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_lun)
  trama_mar = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_mar)
  trama_mie = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_mie)
  trama_jue = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_jue)
  trama_vie = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_vie)
  trama_sab = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_sab)
  trama_dom = impf.create(grp_id_num=30, crs_numero=3000, datetime=date_dom)
  print(trama_lun)
  print(trama_mar)
  print(trama_mie)
  print(trama_jue)
  print(trama_vie)
  print(trama_sab)
  print(trama_dom)
