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


class RespuestaEstadoEnvioComando(object):
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

    def respuestaEstadoEnvioComando(self, trm):

        if (self.validateBcc.isValidBcc(trm, 12, 90)):

            res = {15: self.bytSta.byteDeStatus(trm[15])}
            res.update({13: trm[13]})
            res.update({14: trm[14]})
            res.update({16: self.bitStaI.bitsDeStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsDeStatusII(trm[17])})
            res.update({18: self.bitAla.bitsDeAlarma(trm[18])})
            res.update({19: self.bitStaIII.bitsDeStatusIII(trm[19])})
            # Lampaas
            res.update({20: self.bytLamp.byteDeLamparas(trm[20], {'hi': 2, 'lo': 1})})
            res.update({21: self.bytLamp.byteDeLamparas(trm[21], {'hi': 4, 'lo': 3})})
            res.update({22: self.bytLamp.byteDeLamparas(trm[22], {'hi': 6, 'lo': 5})})
            res.update({23: self.bytLamp.byteDeLamparas(trm[23], {'hi': 8, 'lo': 7})})
            res.update({24: self.bytLamp.byteDeLamparas(trm[24], {'hi': 10, 'lo': 9})})
            res.update({25: self.bytLamp.byteDeLamparas(trm[25], {'hi': 12, 'lo': 11})})
            res.update({26: self.bytLamp.byteDeLamparas(trm[26], {'hi': 14, 'lo': 13})})
            res.update({27: self.bytLamp.byteDeLamparas(trm[27], {'hi': 16, 'lo': 15})})

            res.update({28: self.fecha.fecha(trm[28], trm[29], trm[30], trm[31], trm[32], trm[33], trm[34])})

            res.update({'desfasaje': self._joinNibblesCuad(trm[52], trm[53])})
            res.update({'tiempoReal2': self._joinNibblesCuad(trm[44], trm[45])})
            res.update({'tiempoPrescripto2': self._joinNibblesCuad(trm[48], trm[49])})

            res.update({35: self.helpers.hexToDec(trm[35])})
            res.update({36: self.helpers.hexToDec(trm[36])})
            res.update({37: self.bytSta.byteDeStatus(trm[37])})
            res.update({38: self.helpers.hexToDec(trm[38])})
            res.update({39: self.helpers.hexToDec(trm[39])})

            res.update({42: self.bytSta.byteDeStatus(trm[42])})

            res.update({43: self.helpers.hexToDec(trm[43])})

            res.update({54: self.bytFun.byteDeFuncion(trm[54])})


            r = {'respuestaEstadoEnvioComando': res}
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
