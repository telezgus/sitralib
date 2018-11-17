# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaAgendasAnualesSemanales(object):
  def __init__(self, tramas):
    self.helpers = Helpers()
    self.trm = tramas

  def compile(self):
    tramas = self.helpers.tramas_by_codigo(
      tramas=self.trm,
      codigo='D9'
    )

    data = {
      'anuales': self.__anuales(tramas),
      'semanales': self.__semanales(tramas)
    }
    return data

  def __agendas(self, data):
    respuesta = dict()
    respuesta.update(
      {
        'adi_id_num': self.__numero_agenda(data),
        'hora_minutos_plan': self.__horas_minutos_plan(data)
      }
    )
    return respuesta

  def __anuales(self, data):
    a = defaultdict(dict)
    counter1 = 1
    counter2 = 0
    for i in range(20, 44):
      valor = data[0][str(i)]


      if valor.upper() == '7F' or valor.upper() == 'FF':
        continue

      a[counter2]['ase_id_num'] = counter2

      if counter1 == 1:
        a[counter2]['day'] = valor

      if counter1 == 2:
        a[counter2]['month'] = valor
        counter1 = 0
        counter2 += 1

      counter1 += 1

    return a

  def __semanales(self, data):
    a = defaultdict(list)
    counter1 = 1
    counter2 = 0
    # en la posición 21 comienzan los cambios de hh/mm plan
    # for $i = 56; $i <= 139; ++$i):
    for i in range(56, 140):
      a[counter2].append(int(data[0][str(i)], 16))

      if counter1 == 7:
        counter1 = 0
        counter2 += 1

      counter1 += 1

    return a


if __name__ == '__main__':
  import json

  open_file = open('test_tramas.json', 'r')
  tramas = open_file.read()
  trm = json.loads(tramas, object_pairs_hook=OrderedDict)
  #
  o = CompilaRespuestaAgendasAnualesSemanales(trm)
  trm = o.compile()
  for x in trm['anuales']:
    print('\n')
    print('Anuales')
    print('-' * 30)
    print('N'.ljust(9), 'Dia'.ljust(9), 'Mes'.ljust(10), )
    print('-' * 30)
    print(
      str(trm['anuales'][x]['ase_id_num']).ljust(9),
      str(trm['anuales'][x]['day']).ljust(9),
      str(trm['anuales'][x]['month']).ljust(9),
    )
  print('\n')
  dias = (
    'domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'
  )
  for x in trm['semanales']:
    counter = 0
    print(x)
    for i in trm['semanales'][x]:
      print(dias[counter].title().ljust(15), i)
      counter += 1
    print('-' * 30)
