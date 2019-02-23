# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *
from collections import *
import time
from datetime import datetime

ASE_DEFAULT = {
  'domingo'   : '00',
  'lunes'     : '00',
  'martes'    : '00',
  'miercoles' : '00',
  'jueves'    : '00',
  'viernes'   : '00',
  'sabado'    : '00'
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
    for i in range(12):
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
      a = datetime.strptime(str(data[key]['ans_fecha']), "%Y-%m-%d")
      return str(a.month).zfill(2)
    except:
      return '7F'

  def __set_dia_cambio(self, key, data):
    """
    Retorna el me
    :return: string
    """
    try:
      a = datetime.strptime(str(data[key]['ans_fecha']), "%Y-%m-%d")
      return str(a.day).zfill(2)
    except:
      return 'FF'

  def __set_agendas_semanales(self, data):
    ase_num = []
    for i in range(12):
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
      val = str(data[key]['ase_{0}'.format(dia)])
      return self.helpers.intToHexString(val)
    except:
      return ASE_DEFAULT[dia]


if __name__ == "__main__":
  data = {
    'agendas_semanales': [
        {'id': 1, 'anuales': 1, 'ase_id_num': 1, 'ase_nombre': 'Agenda semanal 1', 'ase_descripcion': '', 'ase_lunes': 2, 'ase_martes': 1, 'ase_miercoles': 1, 'ase_jueves': 1, 'ase_viernes': 1, 'ase_sabado': 1, 'ase_domingo': 1},
        {'id': 2, 'anuales': 1, 'ase_id_num': 2, 'ase_nombre': '', 'ase_descripcion': '', 'ase_lunes': 1, 'ase_martes': 2, 'ase_miercoles': 1, 'ase_jueves': 2, 'ase_viernes': 1, 'ase_sabado': 1, 'ase_domingo': 1}
      ],
    'agendas_anuales_semanas': [
        {'ans_id': 1, 'anuales': 1, 'semanales': 1, 'ans_fecha': '2016-01-01' },
        {'ans_id': 2, 'anuales': 2, 'semanales': 2, 'ans_fecha': '2017-06-20' }
      ]
  }

  o = CompilaEnvioAgendaAnualSemanal()
  result = o.create(
    agendas_anuales_semanas=data['agendas_anuales_semanas'],
    agendas_semanales=data['agendas_semanales'],
    crs_numero=3000,
    grp_id_num=1
  )
  print(result)
