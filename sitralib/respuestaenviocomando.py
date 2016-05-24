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
            res = {'byteDeStatus_a': self.bytSta.byteDeStatus(trm[15])}
            res.update({'numeroDeCruce': [trm[13], trm[14]]})
            res.update(self.bitStaI.bitsDeStatusI(trm[16]))
            res.update(self.bitStaII.bitsDeStatusII(trm[17]))
            res.update(self.bitAla.bitsDeAlarma(trm[18]))
            res.update(self.bitStaIII.bitsDeStatusIII(trm[19]))
            res.update({'object': 'respuestaEnvioComando'})

        return res


if __name__ == '__main__':
    trm = {5: 'FF', 6: '00', 7: '00', 8: '01', 9: 'C9', 10: '00', 11: '10',
           12: '27', 13: '0B', 14: 'B8', 15: '01', 16: '14', 17: '00', 18: '20',
           19: '00', 20: 'A1'}
    obj = RespuestaEnvioComando()
    retorno = obj.respuestaEnvioComando(trm)
    #

    import pprint

    pp = pprint
    pp.pprint(retorno)
