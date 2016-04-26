from sitralib.bitsdealarma import *
from sitralib.bitsdestatusi import *
from sitralib.bitsdestatusii import *
from sitralib.bitsdestatusiii import *
from sitralib.bytedefuncion import *
from sitralib.bytedelamparas import *
from sitralib.bytedestatus import *
from sitralib.helpers.byte import *
from sitralib.helpers.fecha import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaConsultaGrupoExtendido(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteDeStatus()
        self.bitStaI = BitsDeStatusI()
        self.bitStaII = BitsDeStatusII()
        self.bitStaIII = BitsDeStatusIII()
        self.bitAla = BitsDeAlarma()
        self.validateBcc = Bcc()
        self.bytLamp = ByteDeLamparas()
        self.fecha = Fecha()
        self.bytFun = ByteDeFuncion()

    def respuestaConsultaGrupoExtendido(self, trm):

        if (self.validateBcc.isValidBcc(trm, 12, 58)):

            res = {15: self.bytSta.byteDeStatus(trm[15])}
            res.update({13: trm[13]})
            res.update({14: trm[14]})
            res.update({16: self.bitStaI.bitsDeStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsDeStatusII(trm[17])})
            res.update({18: self.bitAla.bitsDeAlarma(trm[18])})
            res.update({19: self.bitStaIII.bitsDeStatusIII(trm[19])})

            res.update({20: self.bytLamp.byteDeLamparas(trm[20],
                                                        {'hi': 2, 'lo': 1})})
            res.update({21: self.bytLamp.byteDeLamparas(trm[21],
                                                        {'hi': 4, 'lo': 3})})
            res.update({22: self.bytLamp.byteDeLamparas(trm[22],
                                                        {'hi': 6, 'lo': 5})})
            res.update({23: self.bytLamp.byteDeLamparas(trm[23],
                                                        {'hi': 8, 'lo': 7})}
                       )
            res.update({24: self.bytLamp.byteDeLamparas(trm[24],
                                                        {'hi': 10, 'lo': 9})}
                       )
            res.update({25: self.bytLamp.byteDeLamparas(trm[25],
                                                        {'hi': 12, 'lo': 11})}
                       )
            res.update({26: self.bytLamp.byteDeLamparas(trm[26],
                                                        {'hi': 14, 'lo': 13})}
                       )
            res.update({27: self.bytLamp.byteDeLamparas(trm[27],
                                                        {'hi': 16, 'lo': 15})}
                       )

            res.update({28: self.fecha.fecha(trm[28], trm[29], trm[30], trm[31],
                                             trm[32], trm[33], trm[34])})

            res.update({'desfasaje': self._joinNibblesCuad(trm[52], trm[53])})
            res.update({'tiempoReal2': self._joinNibblesCuad(trm[44], trm[45])})
            res.update(
                {'tiempoPrescripto2': self._joinNibblesCuad(trm[48], trm[49])})

            res.update({35: self.helpers.hexToDec(trm[35])})
            res.update({36: self.helpers.hexToDec(trm[36])})
            res.update({37: self.bytSta.byteDeStatus(trm[37])})
            res.update({38: self.helpers.hexToDec(trm[38])})
            res.update({39: self.helpers.hexToDec(trm[39])})

            res.update({42: self.bytSta.byteDeStatus(trm[42])})

            res.update({43: self.helpers.hexToDec(trm[43])})

            res.update({54: self.bytFun.byteDeFuncion(trm[54])})


            r = {'respuestaConsultaGrupoExtendido': res}
            return r
        else:
            return []

    def _joinNibbles(self, hex1, hex2):
        a = self.helpers.getNibbles(hex1)
        b = self.helpers.getNibbles(hex2)

        hexNum = '{0}{1}'.format(a['hi'], b['lo'])
        return self.helpers.hexToDec(hexNum)

    def _joinNibblesCuad(self, hex1, hex2):
        n = (self.helpers.hexToDec(hex1) * 256) + self.helpers.hexToDec(hex2)
        return n

# {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'C8', 10: '00', 11: '36', 12: '00', 13: '0B', 14: 'B8', 15: '01', 16: '14', 17: '00', 18: '20', 19: '00', 20: '99', 21: '99', 22: 'DD', 23: 'DD', 24: 'DD', 25: 'DD', 26: 'DD', 27: 'DD', 28: '16', 29: '04', 30: '23', 31: '19', 32: '21', 33: '36', 34: '07', 35: '00', 36: '01', 37: '01', 38: '02', 39: '02', 40: '00', 41: '00', 42: '01', 43: '0A', 44: '00', 45: '16', 46: '00', 47: '00', 48: '00', 49: '28', 50: '00', 51: '00', 52: '00', 53: '00', 54: '00', 55: '00', 56: '00', 57: '00', 58: '8B'}
