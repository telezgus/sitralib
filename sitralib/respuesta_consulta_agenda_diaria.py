from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
# from sitralib.helpers.byte import *
# from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaConsultaAgendaDiaria(object):
    """
    Trama de respuesta de consulta de agenda diaria desde EC hacia CC
    xDB
    """

    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteStatus()
        self.bitStaI = BitsStatusI()
        self.bitStaII = BitsStatusII()
        self.bitStaIII = BitsStatusIII()
        self.bitAla = BitsAlarma()
        self.validateBcc = Bcc()

    def respuestaConsultaAgendaDiaria(self, trm):
        if (self.validateBcc.isValidBcc(trm, 12, 61)):

            self.__set_agendas_diarias_horas(trm)

            res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
            res.update(
                {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
            res.update(self.bitStaI.bitsStatusI(trm[16]))
            res.update(self.bitStaII.bitsStatusII(trm[17]))
            res.update(self.bitAla.bitsAlarma(trm[18]))
            res.update(self.bitStaIII.bitsStatusIII(trm[19]))
            res.update(
                {'numero_programa': self.helpers.hexToDec(trm[20])})
            res.update(
                {'hora_programa': self.__set_agendas_diarias_horas(trm)})
            res.update({'object': 'respuestaConsultaAgendaDiaria'})

            return res
        else:
            return []

    def __set_agendas_diarias_horas(self, trm):

        contador = 1
        index = 0
        iter = list()

        # en la posición 21 comienzan los cambios de hh/mm plan
        for i in range(21, 61):
            if contador == 1:
                iter.append(dict())
                iter[index].update({'indice': index})
                iter[index].update({
                    'hora': trm[i] if self.helpers.validateBetween(
                        min=0, max=23, number=trm[i]) else False
                })

            if contador == 2:
                iter[index].update({
                    'minutos': trm[i] if self.helpers.validateBetween(
                        min=0, max=59, number=trm[i]) else False
                })

            if contador == 3:
                iter[index].update({
                    'programa': trm[i] if self.helpers.validateBetween(
                        min=0, max=20, number=trm[i]) else False
                })

            if contador == 4:
                iter[index].update({'demanda': trm[i]})
                # Reset counters
                contador = 0
                index += 1

            contador += 1

        return iter


if __name__ == "__main__":
    help_text = """
    obj = RespuestaConsultaAgendaDiaria()
    retorno = obj.respuestaConsultaAgendaDiaria({5: 'FF', 6: '00', 8: ... })
    """
    print(help_text)

    trama = {5: "FF", 6: "00", 7: "00", 8: "1E", 9: "DB", 10: "00", 11: "39",
             12: "03", 13: "06", 14: "4A", 15: "01", 16: "14", 17: "00",
             18: "00", 19: "00", 20: "00", 21: "00", 22: "01", 23: "01",
             24: "00", 25: "00", 26: "00", 27: "00", 28: "00", 29: "00",
             30: "00", 31: "00", 32: "00", 33: "00", 34: "00", 35: "00",
             36: "00", 37: "00", 38: "00", 39: "00", 40: "00", 41: "00",
             42: "00", 43: "00", 44: "00", 45: "00", 46: "00", 47: "00",
             48: "00", 49: "00", 50: "00", 51: "00", 52: "00", 53: "00",
             54: "00", 55: "00", 56: "00", 57: "00", 58: "00", 59: "00",
             60: "00", 61: "5A", 62: "00", 63: "00", 64: "00", 65: "00",
             66: "FF", 67: "00", 68: "00", 69: "1E", 70: "C9", 71: "00",
             72: "10", 73: "38", 74: "06", 75: "4A", 76: "01", 77: "14",
             78: "00", 79: "00", 80: "00", 81: "61"}
    obj = RespuestaConsultaAgendaDiaria()
    retorno = obj.respuestaConsultaAgendaDiaria(trama)
    #
    import pprint

    pp = pprint
    pp.pprint(retorno)
