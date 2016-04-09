from sitralib.validators.bcc import *
from sitralib.bitsdealarma import *
from sitralib.bitsdestatusi import *
from sitralib.bitsdestatusii import *
from sitralib.bitsdestatusiii import *
from sitralib.bytedestatus import *
from sitralib.helpers.funciones import *


class RespuestaEnvioComando(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteDeStatus()
        self.bitStaI = BitsDeStatusI()
        self.bitStaII = BitsDeStatusII()
        self.bitStaIII = BitsDeStatusIII()
        self.bitAla = BitsDeAlarma()
        self.validateBcc = Bcc()

    def respuestaEnvioComando(self, trm):
        res = None
        r = {}

        if (self.validateBcc.isValidBcc(trm, 12, 20)):
            res = {15: self.bytSta.byteDeStatus(trm[15])}
            res.update({13: trm[13]})
            res.update({14: trm[14]})
            res.update({16: self.bitStaI.bitsDeStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsDeStatusII(trm[17])})
            res.update({18: self.bitAla.bitsDeAlarma(trm[18])})
            res.update({19: self.bitStaIII.bitsDeStatusIII(trm[19])})
            r = {'respuestaEnvioComando': res}
        return r
