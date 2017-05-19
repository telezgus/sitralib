# -*- coding: UTF-8 -*-
import socket
import time
import json
import sitralib.referencias as ref
from sitralib.validators.bcc import *
from sitralib.helpers.ordenar_trama import *

EMPTY_PROCESS = {
    'per': 0,
    'cod': '0',
    'nombre': '',
    'datetime': time.strftime('%Y-%m-%dT%H:%M:%S'),
}


class Grabacion(object):
    def __init__(self, **kwargs):
        self.ordenar_trama = OrdenarTrama()
        self.configs = kwargs
        self.validator = Bcc()

    def get(self):
        """
        Ejecuta la captura de datos
        """
        data = dict()
        counter = 0

        for trama in self.configs['tramas']:
            # print(trama)
            counter_while = 0
            while True:
                """
                Envia la trama 'n' candidad de veces intentado concretar la
                comunicacion; si no lo logra, muere mostrando un error.
                """
                print('--- intento', counter_while)
                # código trama de envio
                codigo_trama_envio = self.ordenar_trama.get_codigo_trama(trama)
                print('codigo_trama_envio', codigo_trama_envio)
                # código trama de respuesta
                codigo_trama_verificacion = ref.CONSULTA_RESPUESTA[
                    codigo_trama_envio]
                print('codigo_trama_verificacion', codigo_trama_verificacion)
                trama_respuesta = self.__send_lan(trama)

                ## código trama respuesta
                if 'trama_obtenida' in trama_respuesta:
                    codigo_trama_respuesta = self.ordenar_trama.get_codigo_trama(
                        trama_respuesta['trama_obtenida'])
                else:
                    codigo_trama_respuesta = '00'

                # Validación
                if codigo_trama_respuesta != codigo_trama_verificacion and \
                                counter_while <= self.configs['reintentos']:
                    # La trama esta formada correctamente pero, no es el
                    # código que corresponde a la consulta
                    counter_while += 1
                    continue
                elif trama_respuesta['success'] == 1:
                    # La trama de respuesta es correcta. Corta la ejecución.
                    break
                elif counter_while >= self.configs['reintentos']:
                    # Se superó la cantidad de reintentos
                    message_error = {
                        'status': 4,
                        'description': ref.MENSAJES[8]['mensaje'].format(
                            self.configs['reintentos']
                        ),
                        'success': 0,
                    }
                    return message_error

                counter_while += 1

            # Si hay error finalizo la ejecución
            if trama_respuesta['success'] == 0:
                return trama_respuesta

            # Si no hubiera error collecciono las tramas
            data.update({counter: trama_respuesta['trama_obtenida']})

            codigo = self.ordenar_trama.get_codigo_trama(trama)
            self.__archivoJson(
                crsid=self.configs['crs_id'],
                num=counter,
                cod=codigo,
                total=len(self.configs['tramas'])
            )

            counter += 1

        self.__proceso_finalizado()

        # Retronr una lista con las tramas
        return trama_respuesta
        # return data


    def __send_lan(self, tgm):
        """
        Conexión LAN
        """
        try:
            trama = []
            address = (
                str(self.configs['crs_ip']),
                int(self.configs['prt_puerto'])
            )
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Seteo las condiciones para los timeouts
            codigo = self.ordenar_trama.get_codigo_trama(trama)
            # print('___', codigo, '____')
            if (codigo == '7E'):
                timeout = self.configs['timeout_eeprom']
            else:
                timeout = self.configs['timeout']
            # print('___', timeout, '____')
            sock.settimeout(timeout)
            sock.connect(address)

            for num in tgm.split(): sock.sendall(bytearray.fromhex(num))

            time.sleep(timeout)
            # sock.settimeout(None)

            for x in sock.recv(2048): trama.append(hex(x))
            sock.close()

            tramaProcesada = self.ordenar_trama.ordenarTrama(trama)

            if not self.validator.isValidBcc(tramaProcesada):
                return {
                    'status': 5,
                    'description': ref.MENSAJES[9]['mensaje'],
                    'success': 0,
                    'trama_obtenida': tramaProcesada
                }

            return {
                'description': ref.MENSAJES[10]['mensaje'],
                'success': 1,
                'status': 1,
                'trama_obtenida': tramaProcesada,
            }

        except socket.timeout:
            message = {
                'status': 2,
                'description': ref.MENSAJES[1]['mensaje'],
                'success': 0,
            }
            return message

        except socket.error:
            message = {
                'status': 3,
                'description': ref.MENSAJES[11]['mensaje'],
                'success': 0,
            }
            return message

    def __proceso_finalizado(self):
        """
        Crea un archivo *.json con el porcentaje vacio
        """
        self.__procentaje_proceso(EMPTY_PROCESS)

    def __procentaje_proceso(self, data):
        """
        Crea un archivo *.json con el estado del porcentaje
        """
        try:
            file = open(self.configs['porcentaje'], 'w')
            file.write(json.dumps(data))
            file.close()
        except Exception as e:
            print(e)

    def __archivoJson(self, **kwargs):
        """
        Crea un archivo *.json con el porcentaje creado
        """
        porcentaje = round((kwargs['num'] * 100) / kwargs['total'])

        percent = {
            'datetime': time.strftime('%Y-%m-%dT%H:%M:%S'),
            'crsid': kwargs['crsid'],
            'accion': 'grabacion',
            'per': porcentaje,
            'cod': kwargs['cod'],
            'nombre': ref.CODE_REFERENCES[kwargs['cod']]['humanize']
        }
        self.__procentaje_proceso(percent)


class TramaInvalida(Exception):
    pass


if __name__ == '__main__':
    from sitralib.generador_tramas_grabacion import *

    crs = {'crs_id': 17, 'grp_id_num': 1, 'crs_numero': 3000,
           'prt_puerto': 1000, 'crs_ip': '192.168.11.3', 'programas': [
            {'estructura': 84, 'esp_id': 177, 'esp_id_num': 0,
             'esp_data': '{"espDesfasaje": "0", "espCiclo": "48", "espSup": "0", "espData": ["10", "10", "2", "1", "2", "10", "10", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "5", "5"]}'},
            {'estructura': 84, 'esp_id': 178, 'esp_id_num': 1,
             'esp_data': '{"espDesfasaje": "0", "espCiclo": "459", "espSup": "918", "espData": ["99", "80", "70", "60", "50", "40", "30", "20", "10", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "98", "99"]}'},
            {'estructura': 84, 'esp_id': 179, 'esp_id_num': 2,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 60, "espSup": 120, "espData": [10, 15, 2, 1, 2, 10, 15, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5]}'},
            {'estructura': 84, 'esp_id': 180, 'esp_id_num': 3,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 80, "espSup": 160, "espData": [10, 25, 2, 1, 2, 10, 25, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5]}'},
            {'estructura': 84, 'esp_id': 181, 'esp_id_num': 4,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 182, 'esp_id_num': 5,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 183, 'esp_id_num': 6,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 184, 'esp_id_num': 7,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 185, 'esp_id_num': 8,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 186, 'esp_id_num': 9,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 187, 'esp_id_num': 10,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 188, 'esp_id_num': 11,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 4, "espSup": 8, "espData": [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5]}'},
            {'estructura': 84, 'esp_id': 189, 'esp_id_num': 12,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 190, 'esp_id_num': 13,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 191, 'esp_id_num': 14,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'},
            {'estructura': 84, 'esp_id': 192, 'esp_id_num': 15,
             'esp_data': '{"espDesfasaje": 0, "espCiclo": 0, "espSup": 0, "espData": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'}],
           'movimientos': [{'estructura': 84, 'emo_id': 34, 'emo_id_num': 0,
                            'emo_data': '{"mov-1": ["04", "04", "02", "01", "01", "01", "01", "03", "09", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-2": ["00", "00", "00", "00", "00", "00", "00", "04", "0A", "00", "00", "00", "02", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-3": ["01", "01", "01", "01", "04", "09", "01", "01", "02", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "09", "01"], "mov-4": ["04", "04", "02", "01", "01", "01", "01", "03", "03", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-5": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-6": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-7": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-8": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-9": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-10": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-11": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-12": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-13": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-14": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-15": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-16": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "fun": ["01", "00", "00", "00", "00", "00", "00", "00", "05", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "01"]}'},
                           {'estructura': 84, 'emo_id': 35, 'emo_id_num': 1,
                            'emo_data': '{"mov-1": ["04", "04", "02", "01", "01", "01", "01", "03", "09", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-2": ["00", "00", "00", "00", "00", "00", "00", "04", "0A", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-3": ["01", "01", "01", "01", "04", "09", "01", "01", "02", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "09", "01"], "mov-4": ["04", "04", "02", "01", "01", "01", "01", "03", "03", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-5": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-6": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-7": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-8": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-9": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-10": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-11": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-12": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-13": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-14": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-15": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-16": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "fun": ["01", "00", "00", "00", "00", "00", "00", "00", "05", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "01"]}'},
                           {'estructura': 84, 'emo_id': 36, 'emo_id_num': 2,
                            'emo_data': '{"mov-1": ["04", "04", "02", "01", "01", "01", "01", "03", "09", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-2": ["00", "00", "00", "00", "00", "00", "00", "04", "0A", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-3": ["01", "01", "01", "01", "04", "09", "01", "01", "02", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "09", "01"], "mov-4": ["04", "04", "02", "01", "01", "01", "01", "03", "03", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "0A", "01"], "mov-5": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-6": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-7": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-8": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-9": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-10": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-11": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-12": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-13": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-14": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-15": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "mov-16": ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"], "fun": ["01", "00", "00", "00", "00", "00", "00", "00", "05", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00", "01"]}'}],
           'agendas_diarias': [{'adi_id': 1, 'adi_id_num': 1, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 1,
                                'pla_hex': '01'},
                               {'adi_id': 2, 'adi_id_num': 2, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 1,
                                'pla_hex': '01'},
                               {'adi_id': 2, 'adi_id_num': 2, 'anu_id': 1,
                                'adh_hora': datetime.time(6, 0),
                                'adh_id': datetime.time(6, 0), 'pla_nombre': 3,
                                'pla_hex': '03'},
                               {'adi_id': 2, 'adi_id_num': 2, 'anu_id': 1,
                                'adh_hora': datetime.time(14, 0),
                                'adh_id': datetime.time(14, 0), 'pla_nombre': 4,
                                'pla_hex': '04'},
                               {'adi_id': 2, 'adi_id_num': 2, 'anu_id': 1,
                                'adh_hora': datetime.time(22, 0),
                                'adh_id': datetime.time(22, 0), 'pla_nombre': 2,
                                'pla_hex': '02'},
                               {'adi_id': 3, 'adi_id_num': 3, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 4, 'adi_id_num': 4, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 5, 'adi_id_num': 5, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 6, 'adi_id_num': 6, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 7, 'adi_id_num': 7, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 8, 'adi_id_num': 8, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 9, 'adi_id_num': 9, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 10, 'adi_id_num': 10, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 11, 'adi_id_num': 11, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'},
                               {'adi_id': 12, 'adi_id_num': 12, 'anu_id': 1,
                                'adh_hora': datetime.time(0, 1),
                                'adh_id': datetime.time(0, 1), 'pla_nombre': 0,
                                'pla_hex': '00'}], 'agendas_semanales': [
            {'id': 1, 'anuales': 1, 'ase_id_num': 1,
             'ase_nombre': 'Agenda semanal 1', 'ase_descripcion': None,
             'ase_lunes': 1, 'ase_martes': 1, 'ase_miercoles': 1,
             'ase_jueves': 1, 'ase_viernes': 1, 'ase_sabado': 1,
             'ase_domingo': 1},
            {'id': 2, 'anuales': 1, 'ase_id_num': 2, 'ase_nombre': '',
             'ase_descripcion': '', 'ase_lunes': 1, 'ase_martes': 2,
             'ase_miercoles': 1, 'ase_jueves': 1, 'ase_viernes': 1,
             'ase_sabado': 1, 'ase_domingo': 1}], 'agendas_anuales_semanas': [
            {'ans_id': 1, 'anuales': 1, 'semanales': 1,
             'ans_fecha': datetime.date(2016, 1, 1)}], 'feriados': [
            {'feriadotipo': 1, 'diarias': 10, 'anuales': 1, 'fer_id': 1,
             'fer_nombre': 'Feriado Test',
             'fer_fecha': datetime.date(2017, 2, 16)}], 'especiales': [
            {'feriadotipo': 2, 'diarias': 2, 'anuales': 1, 'fer_id': 3,
             'fer_nombre': 'especial test',
             'fer_fecha': datetime.date(2017, 1, 16)}],
           'reintentos': 14,
           'porcentaje': '/Applications/MAMP/htdocs/bitbucket/sitra/sitra/estructura/static/estructura/data/porcentaje.json',
           'timeout': 0.5,
           'timeout_eeprom': 2}
    o = GeneradorTramasGrabacion(**crs)
    tramas = o.create()

    # Ejecuta el capturador

    c = Grabacion(tramas=tramas, **crs)
    e = c.get()
    print(e)
