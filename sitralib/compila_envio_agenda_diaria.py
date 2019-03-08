# -*- coding: utf-8 -*-
import time
from collections import *

from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *

ADI_DEFAULT = {
  0: {
    'adh_hora': '00:01:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '01',
  },
  1: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  2: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  3: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  4: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  5: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  6: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  7: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  8: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
  9: {
    'adh_hora': '00:00:00',
    'adh_plan': '00',
    'adh_hrs': '00',
    'adh_min': '00',
  },
}


class CompilaEnvioAgendaDiaria:
  """
  Envio Agenda Diaria
  x78
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, *args, **kwargs):
    numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

    trama     = defaultdict(dict)
    trama[1]  = '00'
    trama[2]  = '00'
    trama[3]  = '00'
    trama[4]  = '00'
    trama[5]  = 'FF'
    trama[6]  = '00'
    trama[7]  = '00'
    trama[8]  = self.helpers.intToHexString(kwargs['grp_id_num'])
    trama[9]  = '78'  # Codigo según Protocolo
    trama[10] = '00'
    trama[11] = '34'
    trama[12] = '00'  # BCC intermedio
    trama[13] = numeroControlador[:-2]
    trama[14] = numeroControlador[-2:]
    trama[15] = self.helpers.intToHexString(kwargs['adi_id_num'])

    cambios = self.set_cambios(*args)
    for i in cambios:
      trama[i] = cambios[i]

    trama[56] = '00' # BCC final

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None

  def set_cambios(self, *args):
    idx = 16
    adh = defaultdict(dict)

    for i in range(10):
      adh[idx] = self.__get_hora(i, args)

      idx += 1
      adh[idx] = self.__get_minutos(i, args)

      idx += 1
      adh[idx] = self.__get_plan(i, args)

      idx += 1
      adh[idx] = self.__get_demanda_almacenada()

      idx += 1

    return adh


  def __get_plan(self, key, data):
    try:
      return str(data[key]['pla_hex'])
    except:
      return ADI_DEFAULT[key]['adh_plan']


  def __get_minutos(self, key, data):
    try:
      adh_hora = str(data[key]['adh_hora'])
      t = time.strptime(adh_hora, '%H:%M:%S')
      return str(t.tm_min).zfill(2)
    except:
      return ADI_DEFAULT[key]['adh_min']


  def __get_hora(self, key, data):
    try:
      adh_hora = str(data[key]['adh_hora'])
      t = time.strptime(adh_hora, '%H:%M:%S')
      return str(t.tm_hour).zfill(2)
    except:
      return ADI_DEFAULT[key]['adh_hrs']


  def __get_demanda_almacenada(self):
    return '00'
