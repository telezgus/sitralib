from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.validators.bcc import *


class RespuestaPreajustes(object):
    """
    0xD4
    Trama de respuesta de envio de preajustes
    """

    def __init__(self):
        self.bytSta = ByteDeStatus()
        self.bitStaI = BitsDeStatusI()
        self.bitStaII = BitsDeStatusII()
        self.bitStaIII = BitsDeStatusIII()
        self.bitAla = BitsDeAlarma()
        self.validateBcc = Bcc()

    def respuesta(self, trm):
        res = None

        if (self.validateBcc.isValidBcc(trm, 12, 20)):
            res = {'byteDeStatus_a': self.bytSta.byteDeStatus(trm[15])}
            res.update({'numeroDeCruce': [trm[13], trm[14]]})
            res.update(self.bitStaI.bitsDeStatusI(trm[16]))
            res.update(self.bitStaII.bitsDeStatusII(trm[17]))
            res.update(self.bitAla.bitsDeAlarma(trm[18]))
            res.update(self.bitStaIII.bitsDeStatusIII(trm[19]))
            res.update({'object': 'RespuestaPreajustes'})

        return res
