# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class UnemConsultaForzaduraCiclo:
    """
    Forzadura de ciclo
    0x4D — Consulta del SITRA al módulo UNE M
    """
    def __init__(self):
        self.helpers = Helpers()
        self.bcc = Bcc()

    def create(self, **kwargs):
        numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

        trama = {
            1: '00',
            2: '00',
            3: '00',
            4: '00',
            5: 'FF',
            6: '00',
            7: '00',
            8: self.helpers.intToHexString(kwargs['grp_id_num']),
            9: '4D', # Codigo según Protocolo
            10: '00',
            11: '0C',
            12: '00', # BCC intermedio
            13: numeroControlador[:-2],
            14: numeroControlador[-2:],
            15: self.helpers.intToHexString(kwargs['valor']), # Valor ciclo a forzar
            16: '00', # BCC2
        }

        trama_consolidada = self.bcc.consolidate(trama)
        if trama_consolidada:
            return ' '.join(trama_consolidada.values())
        return None


if __name__ == "__main__":
    import random
    o = UnemConsultaForzaduraCiclo()
    i = 0
    while i < 100000:
        numero = random.randint(1000, 9000)
        grupo = random.randint(1, 99)
        plan = random.randint(0, 255)
        print(numero, grupo, plan)
        a = o.create(crs_numero=numero, grp_id_num=grupo, valor=plan)
        print(a)
        
        i += 1