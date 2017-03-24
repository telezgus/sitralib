from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class RespuestaEnvioEstructuraParteAlta(object):
    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteStatus()
        self.bitStaI = BitsStatusI()
        self.bitStaII = BitsStatusII()
        self.bitStaIII = BitsStatusIII()
        self.bitAla = BitsAlarma()
        self.validateBcc = Bcc()

    def respuesta(self, trm):
        res = None

        if (self.validateBcc.isValidBcc(trm, 12, 20)):
            res = {15: self.bytSta.byteStatus(trm[15])}
            res.update({16: self.bitStaI.bitsStatusI(trm[16])})
            res.update({17: self.bitStaII.bitsStatusII(trm[17])})
            res.update({18: self.bitStaIII.bitsStatusIII(trm[18])})
            res.update({19: self.bitAla.bitsAlarma(trm[19])})

            res.update({
                'params': {'trm': {
                    'to_array': trm, 'to_string': ' '.join(trm.values())
                }
                }})
            res.update({'object': 'RespuestaEnvioEstructuraParteAlta'})

        return res
