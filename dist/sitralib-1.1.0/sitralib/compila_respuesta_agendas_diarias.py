from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaAgendasDiarias(object):
    def __init__(self, tramas):
        self.helpers = Helpers()
        self.trm = tramas

    def compile(self):
        tramas = self.helpers.tramas_by_codigo(
            tramas=self.trm,
            codigo='DB'
        )
        data = list()
        for i in tramas:
            data.append(self.__agendas(i))
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

    def __horas_minutos_plan(self, data):
        a = defaultdict(dict)
        counter1 = 1
        counter2 = 0
        for i in range(21, 61):
            if counter1 == 1:
                a[counter2]['hora'] = data[str(i)]

            if counter1 == 2:
                a[counter2]['minutos'] = data[str(i)]

            if counter1 == 3:
                a[counter2]['plan'] = data[str(i)]

            if counter1 == 4:
                a[counter2]['demanda'] = data[str(i)]
                counter1 = 0
                counter2 += 1

            counter1 += 1
        return a

    def __numero_agenda(self, data):
        return int(data['20'], 16)


if __name__ == '__main__':
    import json

    open_file = open('test_tramas.json', 'r')
    tramas = open_file.read()
    trm = json.loads(tramas, object_pairs_hook=OrderedDict)
    #
    o = CompilaRespuestaAgendasDiarias(trm)

    for trm in o.compile():
        print('\n')

        print('Agenda', trm['adi_id_num'], '\n' + '-' * 30)
        print(
            'Hora'.ljust(10),
            'Plan'.ljust(10),
            'Demanda'
        )
        print('-' * 30)
        for x in trm['hora_minutos_plan']:
            print(
                trm['hora_minutos_plan'][x]['hora'] + ':' +
                trm['hora_minutos_plan'][x]['minutos'].ljust(7),
                str(int(trm['hora_minutos_plan'][x]['plan'], 16)).ljust(10),
                trm['hora_minutos_plan'][x]['demanda']
            )
        print('-' * 30)
