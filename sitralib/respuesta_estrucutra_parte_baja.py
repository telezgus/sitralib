from sitralib.bits_alarma import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_status import *
from sitralib.validators.bcc import *


class RespuestaEstrucutraParteBaja(object):
    """
    0xCE
    Respuesta Envío de estructura (parte baja)
    """

    def __init__(self):
        self.bytSta = ByteStatus()
        self.bitStaI = BitsStatusI()
        self.bitStaII = BitsStatusII()
        self.bitStaIII = BitsStatusIII()
        self.bitAla = BitsAlarma()
        self.validateBcc = Bcc()

    def respuesta(self, trm):
        res = None

        if (self.validateBcc.isValidBcc(trm, 12, 20)):
            res = {'byte_status_a': self.bytSta.byteDeStatus(trm[15])}
            res.update({'numero_cruce': [trm[13], trm[14]]})
            res.update(self.bitStaI.bitsDeStatusI(trm[16]))
            res.update(self.bitStaII.bitsDeStatusII(trm[17]))
            res.update(self.bitAla.bitsDeAlarma(trm[18]))
            res.update(self.bitStaIII.bitsDeStatusIII(trm[19]))
            res.update({'object': 'RespuestaEstrucutraParteBaja'})

        return res
