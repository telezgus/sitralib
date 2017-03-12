from sitralib.helpers.funciones import *
from collections import *


class CompilaRespuestaProgramaTiempos(object):
    def __init__(self, tramas):
        self.helpers = Helpers()
        self.trm = tramas

    def compile(self):
        programa_tiempos = self.helpers.tramas_by_codigo(
            tramas=self.trm,
            codigo='D5'
        )
        return programa_tiempos


    def __programa(self, programas):
        v = {
            'espDesfasaje': self.__desfasafe(programas),
            'espCiclo': self.__duracion_ciclo(programas),
            'espSup': self.__tiempo_suplementario(programas),
            'espData': self.__tiempos_intervalos(programas)
        }
        return v

    def __tiempos_intervalos(self, programas):
        """
        Obtiene los intervalos de tiempo
        :param programas: dict
        :return: list
        """
        return [int(programas[i], 16) for i in range(21, 57)]

    def __desfasafe(self, programas):
        """
        Obtiene el tiempo de desfasaje
        :param programas: dict
        :return: int
        """
        msb = programas[61]
        lsb = programas[62]
        valor = msb + lsb
        return self.helpers.hexToDec(valor)

    def __tiempo_suplementario(self, programas):
        """
        Obtiene el tiempo suplementario
        :param programas: dict
        :return: int
        """
        msb = programas[59]
        lsb = programas[60]
        valor = msb + lsb
        return self.helpers.hexToDec(valor)

    def __duracion_ciclo(self, programas):
        """
        Duración del ciclo
        :param programas: dict
        :return: int
        """
        msb = programas[57]
        lsb = programas[58]
        valor = msb + lsb
        return self.helpers.hexToDec(valor)


if __name__ == '__main__':
    import json

    open_file = open('test_tramas.json', 'r')
    tramas = open_file.read()
    trm = json.loads(tramas, object_pairs_hook=OrderedDict)
    #
    o = CompilaRespuestaProgramaTiempos(trm)
    o.compile()
