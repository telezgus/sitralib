from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.validators.bcc import *


class RespuestaAgendAnual(object):
    """
    0xDA
    Respuesta Envío de agenda anual
    #bookmark95
    """

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
            res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
            res.update(
                {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])})
            res.update(self.bitStaI.bitsStatusI(trm[16]))
            res.update(self.bitStaII.bitsStatusII(trm[17]))
            res.update(self.bitAla.bitsAlarma(trm[18]))
            res.update(self.bitStaIII.bitsStatusIII(trm[19]))
            res.update({'object': 'RespuestaAgendAnual'})

        return res
