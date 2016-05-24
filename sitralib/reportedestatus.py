import sys


class ReporteDeStatus(object):
    def validar(self, trama):

        if not trama:
            return {}

        byteDeStatus = self.__obtenerByteDeStatus(trama)
        bitsDeStatusI = self.__obtenerBitsDeStatusI(trama)
        bitsDeAlarmas = self.__obtenerBitsDeAlarmas(trama)
        numeroDeCruce = self.__obtenerNumeroCruce(trama)

        if trama:
            t = {'est': self.__estadoIndicador({'estado': bitsDeStatusI})}

            if bitsDeStatusI['AP']['est']['val'] == None or int(
                    bitsDeStatusI['TIT']['est']['val']) == 1:
                t['vtr'] = 12

            elif int(bitsDeStatusI['AP']['est']['val']) == 1:

                if int(bitsDeStatusI['TIT']['est']['val']) == 0:
                    t['vtr'] = self.__estadoVector(
                        {
                            'estado': bitsDeStatusI,
                            'normal': 10,
                            'apagado': 11
                        }
                    )
                else:
                    t['vtr'] = 12

            else:
                t['vtr'] = self.__estadoVector(
                    {
                        'estado': bitsDeStatusI,
                        'normal': 8,
                        'apagado': 9
                    }
                )

            alertas = {}
            alertas.update(
                {'byteDeStatus': self.__setAlertasByteDeStatus(byteDeStatus)})
            alertas.update({'bitsDeStatusI': self.__setAlertasBitsDeStatusI(
                bitsDeStatusI)})
            alertas.update(
                {'bitsDeAlarma': self.__setAlertasBitsDeAlarmas(bitsDeAlarmas)})
            t['numeroDeCruce'] = numeroDeCruce
            t['alertas'] = alertas
            return t

        return {}

    def __obtenerAlarmas(self, data):
        '''
        Retorna los indices que reportan alarmas en bitsDeStatusI
        '''
        sys.exit(0)

    def __obtenerBitsDeStatusI(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene la colección de datos para
        los bitsDeStatusI
        '''
        if 'bitsDeStatusI' in trama:
            return trama['bitsDeStatusI']

        return {}

    def __setAlertasBitsDeStatusI(self, trama):
        # Remuevo los indices que no evalúo
        trama.pop('VP', None)
        trama.pop('C', None)
        trama.pop('TD', None)
        # trama.pop('LP', None)

        if trama['PFL']['est']['val'] == 0:
            trama.pop('PFL', None)

        if trama['CP']['est']['val'] == 0:
            trama.pop('CP', None)

        if trama['LP']['est']['val'] == 1:
            trama.pop('LP', None)

        if trama['AP']['est']['val'] == 0:
            trama.pop('AP', None)

        if trama['TIT']['est']['val'] == 0:
            trama.pop('TIT', None)

        return trama

    def __obtenerByteDeStatus(self, trama):
        if 'byteDeStatus_a' in trama:
            return trama['byteDeStatus_a']

        return {}

    def __setAlertasByteDeStatus(self, trama):
        # Remuevo los indices que no evalúo
        if 'SIPLA' in trama:
            return {}

        return trama

    def __obtenerNumeroCruce(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene el numero de cruce
        los bitsDeStatusI
        'numeroDeCruce': ['0B', 'B8'],
        '''
        if 'numeroDeCruce' in trama:
            return trama['numeroDeCruce']

        return {}

    def __obtenerBitsDeAlarmas(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene la colección de datos para
        los bits de alarmas
        '''
        if 'bitsDeAlarma' in trama:
            return trama['bitsDeAlarma']

        return {}

    def __setAlertasBitsDeAlarmas(self, trama):
        # Remuevo los indices que no evalúo
        # trama.pop('TSUP', None)
        # trama.pop('BT', None)

        if trama['TSUP']['est']['val'] == 0:
            trama.pop('TSUP', None)

        if trama['BT']['est']['val'] == 0:
            trama.pop('BT', None)

        if trama['FR']['est']['val'] == 0:
            trama.pop('FR', None)

        if trama['CV']['est']['val'] == 0:
            trama.pop('CV', None)

        if trama['FV']['est']['val'] == 0:
            trama.pop('FV', None)

        if trama['GPS']['est']['val'] == 0:
            trama.pop('GPS', None)

        return trama

    def __estadoIndicador(self, data):
        if len(data) > 0:

            if 'estado' in data:
                est = data['estado']
            else:
                est = False

            if int(est['AP']['est']['val']) == 1:
                est = 7  # apagado
            elif int(est['TIT']['est']['val']) == 1:
                est = 4  # titilante
            elif int(est['C']['est']['val']) == 1:
                est = 6  # centralizado
            else:
                est = 5  # local

            return est

        return False

    def __estadoVector(self, opt):

        if len(opt) > 0:

            if 'estado' in opt:
                est = opt['estado']
            else:
                est = False

            if 'normal' in opt:
                normal = opt['normal']
            else:
                normal = False

            if 'apagado' in opt:
                apagado = opt['apagado']
            else:
                apagado = False

            if int(est['VP']['est']['val']) == 1:
                t = normal
            elif int(est['VP']['est']['val']) == 0:
                t = apagado

            return t


if __name__ == "__main__":
    trama = {'byteDeStatus_a': {
        'SIPLA': {'des': 'Plan', 'val': '1', 'cod': 'SIPLA'}},
             'bitsDeStatusII': {'SI': {
                 'des': 'EC en secuencia de inicio (intervalos A [34] y B [35])',
                 'est': {'des': 'Normal', 'val': 0}}, 'AIS': {
                 'des': 'EC aislado de grupo (No acepta comandos grupales)',
                 'est': {'des': 'Normal', 'val': 0}}}, 'bitsDeAlarma': {
            'TSUP': {'des': 'Tiempo suplementario de ciclo',
                     'est': {'des': 'Normal', 'val': 0}},
            'FR': {'des': 'Falta de rojo', 'est': {'des': 'Normal', 'val': 0}},
            'FV': {'des': 'Falta de verde', 'est': {'des': 'Normal', 'val': 0}},
            'CV': {'des': 'Conflicto de verde',
                   'est': {'des': 'Normal', 'val': 0}},
            'GPS': {'des': 'Sistema de posicionamiento global',
                    'est': {'des': 'Falla', 'val': 1}},
            'BT': {'des': 'Baja tensión', 'est': {'des': 'Normal', 'val': 0}}},
             'numeroDeCruce': ['0B', 'B8'], 'bitsDeStatusIII': {
            'D1': {'des': 'Demanda 1', 'est': {'des': 'Desocupada', 'val': 0}},
            'D2': {'des': 'Demanda 2', 'est': {'des': 'Desocupada', 'val': 0}}},
             'bitsDeStatusI': {'VP': {'des': 'Verde del movimiento 1',
                                      'est': {'des': 'Apagado', 'val': 0}},
                               'LP': {'des': 'Llave panel local central',
                                      'est': {'des': 'Central', 'val': 1}},
                               'AP': {'des': 'Apagado',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'PFL': {'des': 'Plan forzado local desde CC',
                                       'est': {'des': 'Normal', 'val': 0}},
                               'TIT': {'des': 'Titilante',
                                       'est': {'des': 'Normal', 'val': 0}},
                               'TD': {'des': 'Tipo de día',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'CP': {'des': 'Cambio de Plan',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'C': {'des': 'Centralizado',
                                     'est': {'des': 'Centralizado', 'val': 1}}}}
    obj = ReporteDeStatus()
    r = obj.validar(trama)

    print(r)
