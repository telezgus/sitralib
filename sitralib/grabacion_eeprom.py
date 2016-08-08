from sitralib.bitsdealarma import *
from sitralib.bitsdestatusi import *
from sitralib.bitsdestatusii import *
from sitralib.bitsdestatusiii import *
from sitralib.bytedestatus import *
from sitralib.validators.bcc import *


class GrabacionEeprom(object):
    """
    Trama SITAR 0xE2
    Trama de grabación de EEPROM desde CC hacia EC
    #bookmark105
    """

    def __init__(self):
        self.bytSta = ByteDeStatus()
        self.bitStaI = BitsDeStatusI()
        self.bitStaII = BitsDeStatusII()
        self.bitStaIII = BitsDeStatusIII()
        self.bitAla = BitsDeAlarma()
        self.validateBcc = Bcc()

    def grabar(self, trm):
        res = None

        if (self.validateBcc.isValidBcc(trm, 12, 26)):
            res = {'byteDeStatus_a': self.bytSta.byteDeStatus(trm[15])}
            res.update({'numeroDeCruce': [trm[13], trm[14]]})
            res.update(self.bitStaI.bitsDeStatusI(trm[16]))
            res.update(self.bitStaII.bitsDeStatusII(trm[17]))
            res.update(self.bitAla.bitsDeAlarma(trm[18]))
            res.update(self.bitStaIII.bitsDeStatusIII(trm[19]))
            res.update({'statusGrabacion': trm[20]})
            res.update({'posicionActualGrabacionMSB': trm[21]})
            res.update({'posicionActualGrabacionLSB': trm[22]})
            res.update({'posicionFinalMemoriaMSB': trm[23]})
            res.update({'posicionFinalMemoriaLSB': trm[24]})
            res.update({'object': 'GrabacionEeprom'})

        return res
