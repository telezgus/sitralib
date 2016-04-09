from sitralib.bitsdealarma import *
from sitralib.bitsdestatusi import *
from sitralib.bitsdestatusii import *
from sitralib.bitsdestatusiii import *
from sitralib.bytedestatus import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaEnvioEstructuraParteAlta(object):
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

        if (self.validateBcc.isValidBcc(trm, 12, 20)):
            res = {15: self.bytSta.byteDeStatus(trm[15])}
            res.update({16: self.bitStaI.bitsDeStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsDeStatusII(trm[17])})
            res.update({18: self.bitStaIII.bitsDeStatusIII(trm[18])})
            res.update({19: self.bitAla.bitsDeAlarma(trm[19])})

            res.update({'params': {'trm': {
                'toArray': trm,
                'toString': ' '.join(trm.values())
            }}})

            r = {'RespuestaEnvioEstructuraParteAlta': res}
        return r
