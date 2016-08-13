import sys


class ReporteEstado(object):
    def validar(self, trama):

        if not trama: return {}
        t = dict()

        byteDeStatus = self.__obtenerByteStatus(trama)
        bitsDeStatusI = self.__obtenerBitsStatusI(trama)
        bitsDeAlarmas = self.__obtenerBitsAlarmas(trama)
        numeroDeCruce = self.__obtenerNumeroCruce(trama)

        if trama:
            t['numero_cruce'] = numeroDeCruce
            t['bits_status_i'] = bitsDeStatusI
            t['est'] = self.__estadoIndicador({'estado': bitsDeStatusI})
            t['vtr'] = self.__vector(bitsDeStatusI)

            # Agrupo las alertas
            alertas = dict()
            alertas.update(
                {'byte_status': self.__setAlertasByteDeStatus(byteDeStatus)})

            alertas.update(
                {'bits_status_i': self.__setAlertasBitsDeStatusI(
                    bitsDeStatusI)})

            alertas.update(
                {'bits_alarma': self.__setAlertasBitsDeAlarmas(bitsDeAlarmas)})

            # Incluyo las alertas en el diccionario de retorno
            t['alertas'] = alertas

            # Si la trama contempla propiedades de evaluación del
            # estado extendido
            if 'byte_lamparas' in trama:
                t.update(self.__prepararTrama(trama))
            return t

        return {}

    def __vector(self, bitsDeStatusI):
        if bitsDeStatusI['AP']['est']['val'] == None or int(
                bitsDeStatusI['TIT']['est']['val']) == 1:
            vector = 12

        elif int(bitsDeStatusI['AP']['est']['val']) == 1:

            if int(bitsDeStatusI['TIT']['est']['val']) == 0:
                vector = self.__estadoVector(
                    {
                        'estado': bitsDeStatusI,
                        'normal': 10,
                        'apagado': 11
                    }
                )
            else:
                vector = 12

        else:
            vector = self.__estadoVector(
                {
                    'estado': bitsDeStatusI,
                    'normal': 8,
                    'apagado': 9
                }
            )
        return vector

    def __prepararTrama(self, trama):
        """
        Remueve los indices innecesarios para mostrar el estado
        :return:
        """
        # trama.pop('byteDeStatus_a')
        trama.pop('byte_status_b')
        trama.pop('byte_status_c')
        trama.pop('bits_status_ii')
        trama.pop('bits_status_iii')
        trama.pop('object')
        trama.pop('bits_alarma')

        return trama

    def __obtenerAlarmas(self, data):
        '''
        Retorna los indices que reportan alarmas en bitsDeStatusI
        '''
        sys.exit(0)

    def __obtenerBitsStatusI(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene la colección de datos para
        los bitsDeStatusI
        '''
        if 'bits_status_i' in trama:
            return trama['bits_status_i']

        return {}

    def __setAlertasBitsDeStatusI(self, trama):
        # Remuevo los indices que no evalúo
        new_trama = dict()
        if trama['PFL']['est']['val'] != 0:
            new_trama['PFL'] = trama['PFL']

        if trama['CP']['est']['val'] != 0:
            new_trama['CP'] = trama['CP']

        if trama['LP']['est']['val'] == 0:
            new_trama['LP'] = trama['LP']

        if trama['AP']['est']['val'] != 0:
            new_trama['AP'] = trama['AP']

        return new_trama

    def __obtenerByteStatus(self, trama):
        if 'byte_status_a' in trama:
            return trama['byte_status_a']

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
        if 'numero_cruce' in trama:
            return trama['numero_cruce']

        return {}

    def __obtenerBitsAlarmas(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene la colección de datos para
        los bits de alarmas
        '''
        if 'bits_alarma' in trama:
            return trama['bits_alarma']

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

    trama2 = {'bitsDeAlarma': {'BT': {'des': 'Baja tensión',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'CV': {'des': 'Conflicto de verde',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'FR': {'des': 'Falta de rojo',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'FV': {'des': 'Falta de verde',
                                      'est': {'des': 'Normal', 'val': 0}},
                               'GPS': {
                                   'des': 'Sistema de posicionamiento global',
                                   'est': {'des': 'Falla', 'val': 1}},
                               'TSUP': {'des': 'Tiempo suplementario de ciclo',
                                        'est': {'des': 'Normal', 'val': 0}}},
              'bitsDeStatusI': {'AP': {'des': 'Apagado',
                                       'est': {'des': 'Normal', 'val': 0}},
                                'C': {'des': 'Centralizado',
                                      'est': {'des': 'Centralizado', 'val': 1}},
                                'CP': {'des': 'Cambio de Plan',
                                       'est': {'des': 'Normal', 'val': 0}},
                                'LP': {'des': 'Llave panel local central',
                                       'est': {'des': 'Central', 'val': 1}},
                                'PFL': {'des': 'Plan forzado local desde CC',
                                        'est': {'des': 'Normal', 'val': 0}},
                                'TD': {'des': 'Tipo de día',
                                       'est': {'des': 'Normal', 'val': 0}},
                                'TIT': {'des': 'Titilante',
                                        'est': {'des': 'Normal', 'val': 0}},
                                'VP': {'des': 'Verde del movimiento 1',
                                       'est': {'des': 'Apagado', 'val': 0}}},
              'bitsDeStatusII': {
                  'AIS': {'des': 'EC aislado de grupo (No acepta '
                                 'comandos grupales)',
                          'est': {'des': 'Normal', 'val': 0}},
                  'SI': {'des': 'EC en secuencia de inicio (intervalos A '
                                '[34] y B [35])',
                         'est': {'des': 'Normal', 'val': 0}}},
              'bitsDeStatusIII': {'D1': {'des': 'Demanda 1',
                                         'est': {'des': 'Desocupada',
                                                 'val': 0}},
                                  'D2': {'des': 'Demanda 2',
                                         'est': {'des': 'Desocupada',
                                                 'val': 0}}},
              'byteDeFuncion': {'NAN': {'est': {'des': 'Ninguna', 'val': 1}}},
              'byteDeLamparas': {'mov1': {'cod': 'rojo-intermitente',
                                          'des': 'Rojo intermitente',
                                          'val': 1},
                                 'mov10': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov11': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov12': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov13': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov14': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov15': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov16': {'cod': 'inexistente',
                                           'des': 'Inexistente',
                                           'val': 1},
                                 'mov2': {'cod': 'rojo-intermitente',
                                          'des': 'Rojo intermitente',
                                          'val': 1},
                                 'mov3': {'cod': 'rojo-intermitente',
                                          'des': 'Rojo intermitente',
                                          'val': 1},
                                 'mov4': {'cod': 'rojo-intermitente',
                                          'des': 'Rojo intermitente',
                                          'val': 1},
                                 'mov5': {'cod': 'inexistente',
                                          'des': 'Inexistente',
                                          'val': 1},
                                 'mov6': {'cod': 'inexistente',
                                          'des': 'Inexistente',
                                          'val': 1},
                                 'mov7': {'cod': 'inexistente',
                                          'des': 'Inexistente',
                                          'val': 1},
                                 'mov8': {'cod': 'inexistente',
                                          'des': 'Inexistente',
                                          'val': 1},
                                 'mov9': {'cod': 'inexistente',
                                          'des': 'Inexistente',
                                          'val': 1}},
              'byteDeStatus_a': {
                  'SIPLA': {'cod': 'SIPLA', 'des': 'Plan', 'val': '1'}},
              'byteDeStatus_b': {
                  'SIPLA': {'cod': 'SIPLA', 'des': 'Plan', 'val': '1'}},
              'byteDeStatus_c': {
                  'SIPLA': {'cod': 'SIPLA', 'des': 'Plan', 'val': '1'}},
              'dateTime': {'day': '23',
                           'hour': '19',
                           'minutes': '21',
                           'month': '04',
                           'seconds': '36',
                           'timestamp': '16-04-23T19:21:36',
                           'wday': 'sábado',
                           'year': '16'},
              'desfasaje': 0,
              'duracionDePaso': 10,
              'estructura': 0,
              'numeroDeCruce': ['0B', 'B8'],
              'numeroDePaso': 2,
              'object': 'respuestaConsultaGrupoExtendido',
              'programaDeTiempos': 1,
              'segundoPaso': 2,
              'tiempoPrescripto2': 40,
              'tiempoReal2': 22}
    obj = ReporteDeStatus()
    r = obj.validar(trama2)
    import pprint

    pp = pprint
    pp.pprint(r)
