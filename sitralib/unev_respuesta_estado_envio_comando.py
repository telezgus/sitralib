# -*- coding: utf-8 -*-
from sitralib.bits_alarma import *
from sitralib.bits_alarma_ii import *
from sitralib.bits_falta import *
from sitralib.bits_status_i import *
from sitralib.bits_status_ii import *
from sitralib.bits_status_iii import *
from sitralib.byte_funcion import *
from sitralib.byte_lamparas import *
from sitralib.byte_status import *
from sitralib.helpers.byte import *
from sitralib.helpers.fecha import *
from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *


class UnevRespuestaEstadoEnvioComando:
    def __init__(self):
        self.helpers = Helpers()
        self.bytSta = ByteStatus()
        self.bitStaI = BitsStatusI()
        self.bitStaII = BitsStatusII()
        self.bitStaIII = BitsStatusIII()
        self.bitAla = BitsAlarma()
        self.bitAlaII = BitsAlarmaII()
        self.validateBcc = Bcc()
        self.bytLamp = ByteLamparas()
        self.fecha = Fecha()
        self.bytFun = ByteFuncion()
        self.bits_falta = BitsFalta()


    def get_falla(self, selector, data):
        falla = dict()

        for falta in data.get(selector, dict()):
            for x in falta:
                if falta[x]['est']['val'] == 1:
                    falla.update(falta)

        return falla


    def get(self, trm):
        if not self.validateBcc.isValidBcc(trm, 12, 90):
            return []



        res = {'byte_status_a': self.bytSta.byteStatus(trm[15])}
        res.update({
            'numero_cruce': self.helpers.hexToDec(trm[13] + trm[14])
        })
        res.update(self.bitStaI.bitsStatusI(trm[16]))
        res.update(self.bitStaII.bitsStatusII(trm[17]))
        res.update(self.bitAla.bitsAlarma(trm[18]))
        res.update(self.bitAlaII.bitsAlarmaII(trm[80]))
        res.update(self.bitStaIII.bitsStatusIII(trm[19]))

        # Lamparas
        byte_de_lamparas = dict()
        byte_de_lamparas.update({'mov1': self.bytLamp.byteLamparas(
            trm[20], hi=2, lo=1, mov=1)})
        byte_de_lamparas.update({'mov2': self.bytLamp.byteLamparas(
            trm[20], hi=2, lo=1, mov=2)})
        byte_de_lamparas.update({'mov3': self.bytLamp.byteLamparas(
            trm[21], hi=4, lo=3, mov=3)})
        byte_de_lamparas.update({'mov4': self.bytLamp.byteLamparas(
            trm[21], hi=4, lo=3, mov=4)})
        byte_de_lamparas.update({'mov5': self.bytLamp.byteLamparas(
            trm[22], hi=6, lo=5, mov=5)})
        byte_de_lamparas.update({'mov6': self.bytLamp.byteLamparas(
            trm[22], hi=6, lo=5, mov=6)})
        byte_de_lamparas.update({'mov7': self.bytLamp.byteLamparas(
            trm[23], hi=8, lo=7, mov=7)})
        byte_de_lamparas.update({'mov8': self.bytLamp.byteLamparas(
            trm[23], hi=8, lo=7, mov=8)})
        byte_de_lamparas.update({'mov9': self.bytLamp.byteLamparas(
            trm[24], hi=10, lo=9, mov=9)})
        byte_de_lamparas.update({'mov10': self.bytLamp.byteLamparas(
            trm[24], hi=10, lo=9, mov=10)})
        byte_de_lamparas.update({'mov11': self.bytLamp.byteLamparas(
            trm[25], hi=12, lo=11, mov=11)})
        byte_de_lamparas.update({'mov12': self.bytLamp.byteLamparas(
            trm[25], hi=12, lo=11, mov=12)})
        byte_de_lamparas.update({'mov13': self.bytLamp.byteLamparas(
            trm[26], hi=14, lo=13, mov=13)})
        byte_de_lamparas.update({'mov14': self.bytLamp.byteLamparas(
            trm[26], hi=14, lo=13, mov=14)})
        byte_de_lamparas.update({'mov15': self.bytLamp.byteLamparas(
            trm[27], hi=16, lo=15, mov=15)})
        byte_de_lamparas.update({'mov16': self.bytLamp.byteLamparas(
            trm[27], hi=16, lo=15, mov=16)})
        res.update({'byte_lamparas': byte_de_lamparas})

        res.update({
            'datetime': self.fecha.fecha(
                year = '20{}'.format(trm[28]),
                month = trm[29],
                day = trm[30],
                hour = trm[31],
                minutes = trm[32],
                seconds = trm[33],
                wday = trm[34])
        })

        res.update({'desfasaje': self._joinNibblesCuad(trm[52], trm[53])})
        res.update({'tiempo_real_2': self._joinNibblesCuad(trm[44], trm[45])})
        res.update({'estructura': self.helpers.hexToDec(trm[35])})
        res.update({'programa_tiempos': self.helpers.hexToDec(trm[36])})
        res.update({'byte_status_b': self.bytSta.byteStatus(trm[37])})
        res.update({'numero_paso': self.helpers.hexToDec(trm[38])})
        res.update({'segundo_paso': self.helpers.hexToDec(trm[39])})
        res.update({'byte_status_c': self.bytSta.byteStatus(trm[42])})
        res.update({'duracion_paso': self.helpers.hexToDec(trm[43])})
        res.update({'duracion_ciclo': self._joinNibblesCuad(trm[48], trm[49])})



        byte_falta = {}
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[58], name="falta_rojo_1",
                                        label="Falta de rojo", prefix="FR01",
                                        start=1))
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[59], name="falta_rojo_2",
                                        label="Falta de rojo", prefix="FR02",
                                        start=9)
        )
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[60], name="falta_amarillo_1",
                                        label="Falta de amarillo", prefix="FA01",
                                        start=1))
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[61], name="falta_amarillo_2",
                                        label="Falta de amarillo", prefix="FA02",
                                        start=9))
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[62], name="falta_verde_1",
                                        label="Falta de verde", prefix="FV01",
                                        start=1))
        byte_falta.update(
            self.bits_falta.bitsFalta(trm[63], name="falta_verde_2",
                                        label="Falta de verde", prefix="FV02",
                                        start=9))

        falla = dict()
        for i in ['falta_rojo_1', 'falta_rojo_2', 'falta_amarillo_1',
                    'falta_amarillo_2', 'falta_verde_1', 'falta_verde_2']:
            n = self.get_falla(i, byte_falta)
            if n:
                falla.update(n)


        byte_conflicto = dict()
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[64], name="conflicto_rojo_1",
                                        label="Conflicto de rojo",
                                        prefix="CR01",
                                        start=1))
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[65], name="conflicto_rojo_2",
                                        label="Conflicto de rojo",
                                        prefix="CR02",
                                        start=9))
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[66], name="conflicto_amarillo_1",
                                        label="Conflicto de amarillo",
                                        prefix="CA01",
                                        start=1))
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[67], name="conflicto_amarillo_2",
                                        label="Conflicto de amarillo",
                                        prefix="CA02",
                                        start=9))
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[68], name="conflicto_verde_1",
                                        label="Conflicto de verde",
                                        prefix="CV01",
                                        start=1))
        byte_conflicto.update(
            self.bits_falta.bitsFalta(trm[69], name="conflicto_verde_2",
                                        label="Conflicto de verde",
                                        prefix="CV02",
                                        start=9))

        conflicto = dict()
        for i in ['conflicto_rojo_1', 'conflicto_amarillo_1', 'conflicto_verde_1',
                    'conflicto_rojo_2', 'conflicto_amarillo_2', 'conflicto_verde_2']:
            n = self.get_falla(i, byte_conflicto)
            if n:
                conflicto.update(n)


        byte_fusible = dict()
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[70], name="fusible_rojo_1",
                                        label="Falta de fusible de rojo",
                                        prefix="FFR01",
                                        start=1))
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[71], name="fusible_rojo_2",
                                        label="Falta de fusible de rojo",
                                        prefix="FFR02",
                                        start=9))
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[72], name="fusible_amarillo_1",
                                        label="Falta de fusible de amarillo",
                                        prefix="FFA01",
                                        start=1))
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[73], name="fusible_amarillo_2",
                                        label="Falta de fusible de amarillo",
                                        prefix="FFA02",
                                        start=9))
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[74], name="fusible_verde_1",
                                        label="Falta de fusible de verde",
                                        prefix="FFV01",
                                        start=1))
        byte_fusible.update(
            self.bits_falta.bitsFalta(trm[75], name="fusible_verde_2",
                                        label="Falta de fusible de verde",
                                        prefix="FFV02",
                                        start=9))


        fusible = dict()
        for i in ['fusible_rojo_1', 'fusible_amarillo_1', 'fusible_verde_1',
                    'fusible_rojo_2', 'fusible_amarillo_2', 'fusible_verde_2']:
            n = self.get_falla(i, byte_fusible)
            if n:
                fusible.update(n)


        byte_detector = dict()
        byte_detector.update(
            self.bits_falta.bitsFalta(trm[76], name="detector_demanda_1",
                                        label="Detector", prefix="D",
                                        start=1, autoincrement=True))
        byte_detector.update(
            self.bits_falta.bitsFalta(trm[77], name="detector_demanda_2",
                                        label="Detector", prefix="D",
                                        start=9, autoincrement=True))
        byte_detector.update(
            self.bits_falta.bitsFalta(trm[78], name="detector_demanda_3",
                                        label="Detector", prefix="D",
                                        start=17, autoincrement=True))
        byte_detector.update(
            self.bits_falta.bitsFalta(trm[79], name="detector_demanda_4",
                                        label="Detector", prefix="D",
                                        start=25, autoincrement=True))


        # TEMPERATURE
        res.update(
            {'temperature': {
                'temp_display': self.helpers.hexToDec(trm[81]),
                'temp_mother': self.helpers.hexToDec(trm[82]),
                'temp_extension_1': self.helpers.hexToDec(trm[83]),
                'temp_extension_2': self.helpers.hexToDec(trm[84]),
                'temp_extension_3': self.helpers.hexToDec(trm[85]),
                'temp_pi_cpu':  self.helpers.hexToDec(trm[86]),
                'temp_pi_gpu': self.helpers.hexToDec(trm[87]),
            }}
        )

        res.update({'byte_falta': falla})
        res.update({'byte_conflicto': conflicto})
        res.update({'byte_falta_fusible': fusible})
        res.update({'byte_detector': byte_detector})
        res.update(self.bytFun.get(trm[54]))
        res.update({'object': 'UnevRespuestaEstadoEnvioComando'})

        return res


    def _joinNibbles(self, hex1, hex2):
        a = self.helpers.getNibbles(hex1)
        b = self.helpers.getNibbles(hex2)

        hexNum = '{0}{1}'.format(a['hi'], b['lo'])
        return self.helpers.hexToDec(hexNum)

    def _joinNibblesCuad(self, hex1, hex2):
        n = (self.helpers.hexToDec(hex1) * 256) + self.helpers.hexToDec(hex2)
        return n


if __name__ == "__main__":
    import pprint as pp
    trama = """FF 00 00 01 C5 00 56 6D 0B BD 00 14 00 20 00 11 00 00 00 00 00 00 00
            21 11 30 14 00 27 03 00 00 00 02 29 00 00 00 48 00 57 00 00 00 78 00
            00 00 2B 00 00 00 00 00 00 00 00 E0 00 00 00 00 00 00 00 00 00 00 1C
            00 00 00 00 00 00 00 1D 1C 00 00 00 00 00 00 00 54"""

    bcc = Bcc()
    obj = UnevRespuestaEstadoEnvioComando()
    retorno = obj.get(bcc.consolidate(trama))
    pp.pprint(retorno)