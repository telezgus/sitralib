from sitralib.validators.bcc import *
from sitralib.bitsdealarma import *
from sitralib.bitsdestatusi import *
from sitralib.bitsdestatusii import *
from sitralib.bitsdestatusiii import *
from sitralib.bytedestatus import *
from sitralib.helpers.funciones import *

POSICION_BCC_INTERMEDIO = 12
POSICION_BCC_FINAL = 37


class RespuestaConsultaPuestoConteo(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteDeStatus()
        self.bitStaI = BitsDeStatusI()
        self.bitStaII = BitsDeStatusII()
        self.bitStaIII = BitsDeStatusIII()
        self.bitAla = BitsDeAlarma()
        self.validateBcc = Bcc()

    def respuesta(self, trm):
        res = None
        r = {}

        if (self.validateBcc.isValidBcc(trm, POSICION_BCC_INTERMEDIO, POSICION_BCC_FINAL)):
            res = {15: self.bytSta.byteDeStatus(trm[15])}
            res.update({16: self.bitStaI.bitsDeStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsDeStatusII(trm[17])})
            res.update({18: self.bitAla.bitsDeAlarma(trm[18])})
            res.update({19: self.bitStaIII.bitsDeStatusIII(trm[19])})
            # Valor de espira
            res.update({20: self.__espira(1, trm[20])})
            res.update({21: self.__espira(2, trm[21])})
            res.update({22: self.__espira(3, trm[22])})
            res.update({23: self.__espira(4, trm[23])})
            res.update({24: self.__espira(5, trm[24])})
            res.update({25: self.__espira(6, trm[25])})
            res.update({26: self.__espira(7, trm[26])})
            res.update({27: self.__espira(8, trm[27])})
            # Tiempo de ocupacion
            res.update({28: self.__ocupacion(1, trm[28])})
            res.update({29: self.__ocupacion(2, trm[29])})
            res.update({30: self.__ocupacion(3, trm[30])})
            res.update({31: self.__ocupacion(4, trm[31])})
            res.update({32: self.__ocupacion(5, trm[32])})
            res.update({33: self.__ocupacion(6, trm[33])})
            res.update({34: self.__ocupacion(7, trm[34])})
            res.update({35: self.__ocupacion(8, trm[35])})
            r = {'RespuestaConsultaPuestoConteo': res}
        return r

    def __espira(self, numero, valor):
        a = {
            'espira{0}'.format(numero): {
                'des': 'Espira {0}'.format(numero),
                'val': int(valor),
            }
        }
        return a

    def __ocupacion(self, numero, valor):
        b = {
            'tiempoOcupacion{0}'.format(numero): {
                'des': 'Tiempo de ocupación de espira {0}'.format(numero),
                'val': int(valor),
            }
        }
        return b


if __name__ == "__main__":
    from sitralib.helpers.ordenartrama import *
    import pprint

    #
    trama1 = '00 00 00 00 FF 01 00 01 E0 00 21 3E 1B BB 01 D0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF B0'
    trama2 = '00 00 00 00 FF 01 00 01 E0 00 21 3E 1B BB F0 51 01 02 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 3D'
    #
    print(trama1 + '\n')
    respuestaPuestoConteo = RespuestaConsultaPuestoConteo()
    ot = OrdenarTrama()
    tramaOrdenada = ot.ordenartrama(trama1)
    retorno = respuestaPuestoConteo.respuesta(tramaOrdenada)
    pp = pprint.PrettyPrinter(indent=4, width=200, depth=8, compact=True)
    pp.pprint(retorno)
