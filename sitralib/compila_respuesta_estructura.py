from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaEstructura(object):
    def __init__(self, tramas):
        self.helpers = Helpers()
        self.trm = tramas

    def compile(self):
        alta = self.helpers.tramas_by_codigo(tramas=self.trm, codigo='CB')
        baja = self.helpers.tramas_by_codigo(tramas=self.trm, codigo='CC')

        for i in alta:
            intervalos = self.__intervalos(trama=i)
            intervalos_por_movimientos = self.__movimientos_por_intervalo(
                intervalos=intervalos
            )
            print(intervalos_por_movimientos)
            print('\n\n')

        for i in baja:
            intervalos = self.__intervalos(trama=i)
            intervalos_por_movimientos = self.__movimientos_por_intervalo(
                intervalos=intervalos
            )
            print(intervalos_por_movimientos)
            print('\n\n')

    def __movimientos_por_intervalo(self, **kwargs):
        f = dict()
        mov = defaultdict(dict)
        for i in kwargs['intervalos']:
            intervalos = kwargs['intervalos'][i]
            counter = 0
            for x in range(0, 8):
                counter += 1
                mov[i][counter] = self.helpers.getNibbles(
                    intervalos[x], 2)['lo']
                counter += 1
                mov[i][counter] = self.helpers.getNibbles(
                    intervalos[x], 2)['hi']

            f[i] = intervalos[8]

        est = defaultdict(list)
        for i in range(0, 18):
            for x in range(1, 17):
                est['mov-{0}'.format(x)].append(mov[i][x])
        est['fun'] = f.values()

        return est

    def __slice(self, **kwargs):
        trama_sliced = dict()
        for i in kwargs['trama']:
            validate = self.helpers.validateBetween(
                max=254, min=21, number=i
            )
            if validate:
                trama_sliced[i] = kwargs['trama'][i]
        return trama_sliced

    def __intervalos(self, **kwargs):
        """
        Separa la colección de datos en intervalos.
        $trama dict
        :return: dict
        """
        counter = 0
        idx = 0
        mov = dict()
        # Verificacion
        trama = dict()
        for i in range(5, 256):
            # key = str(i) if str(i) in kwargs['trama'] else int(i)
            trama[i] = kwargs['trama'][str(i)]

        trama_sliced = self.__slice(trama=trama)
        a = list()
        for i in trama_sliced:

            if counter == 13:
                a = list()
                counter = 0
                idx += 1

            a.append(trama[i])
            mov[idx] = a
            counter += 1

        return mov


if __name__ == '__main__':
    import json

    open_file = open('test_tramas.json', 'r')
    tramas = open_file.read()
    trm = json.loads(tramas, object_pairs_hook=OrderedDict)
    #
    o = CompilaRespuestaEstructura(trm)
    o.compile()
