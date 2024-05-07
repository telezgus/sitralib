# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class UnemRespuestaForzaduraDesfazaje:
    def __init__(self):
        self.helpers = Helpers()
        self.validateBcc = Bcc()

    def get(self, trm):
        if self.helpers.hexToDec(trm[9]) != '181':
            return None            

        if self.validateBcc.isValidBcc(trm):
            res = {'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])}
            res.update({'object': 'UnemRespuestaForzaduraDesfazaje'})

        return res or None
