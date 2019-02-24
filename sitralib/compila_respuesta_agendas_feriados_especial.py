# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaAgendasFeriadosEspecial:
  def __init__(self, tramas):
    self.helpers = Helpers()
    self.trm = tramas

  def compile(self):
    tramas = self.helpers.tramas_by_codigo(
      tramas=self.trm,
      codigo='D7'
    )
    data = dict()
    for i in tramas:
      data = {
        'feriados': self.__feriados(i),
        'especiales': self.__eventos_especiales(i)
      }
    return data

  def __eventos_especiales(self, data):
    planes = self.__eventos_especiales_planes(data)

    a = defaultdict(dict)
    contadorCambio = 1
    agrupadorCambio = 0

    for i in range(20, 52):
      valor = data[str(i)]
      if valor.upper() == '7F' or valor.upper() == 'FF':
        continue

      if contadorCambio == 1:
        a[agrupadorCambio]['day'] = valor

      if contadorCambio == 2:
        a[agrupadorCambio]['month'] = valor
        a[agrupadorCambio]['adi_id_num'] = self.helpers.hexToDec(planes[agrupadorCambio])
        contadorCambio = 0
        agrupadorCambio += 1

      contadorCambio += 1
    return a

  def __feriados(self, data):
    feriados = self.__feriados_planes(data)

    a = defaultdict(dict)
    contadorCambio = 1
    agrupadorCambio = 0

    for i in range(52, 116):
      valor = data[str(i)]
      if valor.upper() == '7F' or valor.upper() == 'FF':
        continue

      if contadorCambio == 1:
        a[agrupadorCambio]['day'] = valor

      if contadorCambio == 2:
        a[agrupadorCambio]['month'] = valor
        a[agrupadorCambio]['adi_id_num'] = self.helpers.hexToDec(feriados[agrupadorCambio])
        contadorCambio = 0
        agrupadorCambio += 1

      contadorCambio += 1

    return a

  def __eventos_especiales_planes(self, trama):
    a = [trama[str(i)] for i in range(116, 132)]
    return a

  def __feriados_planes(self, trama):
    a = [trama[str(i)] for i in range(132, 164)]
    return a

  def __numero_agenda(self, data):
    return int(data['20'], 16)


if __name__ == '__main__':
  import json
  open_file = open('test_tramas.json', 'r')
  tramas = open_file.read()
  trm = json.loads(tramas, object_pairs_hook=OrderedDict)
  #
  o = CompilaRespuestaAgendasFeriadosEspecial(trm)
  result = o.compile()
  print(result)
  for i in result:
    print(i, result[i])
