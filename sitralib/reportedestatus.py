import sys


class ReporteDeStatus(object):
    def validar(self, trama):
        if not trama:
            return {}

        byteDeStatus = self.__obtenerByteDeStatus(trama)
        bitsDeStatusI = self.__obtenerBitsDeStatusI(trama)
        bitsDeAlarmas = self.__obtenerBitsDeAlarmas(trama)
        crsIdNum = self.__obtenerNumeroCruce(trama)

        if trama:
            t = {'est': self.__estadoIndicador({'estado': bitsDeStatusI})}

            if bitsDeStatusI['AP']['est']['val'] == None or int(bitsDeStatusI['TIT']['est']['val']) == 1:
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
            alertas.update({'byteDeStatus': self.__setAlertasByteDeStatus(byteDeStatus)})
            alertas.update({'bitsDeStatusI': self.__setAlertasBitsDeStatusI(bitsDeStatusI)})
            alertas.update({'bitsDeAlarma': self.__setAlertasBitsDeAlarmas(bitsDeAlarmas)})
            t['crsIdNum'] = crsIdNum
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
        if 'respuestaEnvioComando' in trama:
            return trama['respuestaEnvioComando'][16]['bitsDeStatusI']
        elif 'respuestaConsultaGrupoExtendido' in trama:
            return trama['respuestaConsultaGrupoExtendido'][16]['bitsDeStatusI']
        else:
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
        if 'respuestaEnvioComando' in trama:
            return trama['respuestaEnvioComando'][15]['byteDeStatus']
        elif 'respuestaConsultaGrupoExtendido' in trama:
            return trama['respuestaConsultaGrupoExtendido'][15]['byteDeStatus']
        else:
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
        '''
        if 'respuestaEnvioComando' in trama:
            return {
                13: trama['respuestaEnvioComando'][13],
                14: trama['respuestaEnvioComando'][14],
            }
        elif 'respuestaConsultaGrupoExtendido' in trama:
            return {
                13: trama['respuestaConsultaGrupoExtendido'][13],
                14: trama['respuestaConsultaGrupoExtendido'][14],
            }
        else:
            return {}



    def __obtenerBitsDeAlarmas(self, trama):
        '''
        Evalua la trama C8 ó C9 y obtiene la colección de datos para
        los bits de alarmas
        '''
        if 'respuestaEnvioComando' in trama:
            return trama['respuestaEnvioComando'][18]['bitsDeAlarma']
        elif 'respuestaConsultaGrupoExtendido' in trama:
            return trama['respuestaConsultaGrupoExtendido'][18]['bitsDeAlarma']
        else:
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
