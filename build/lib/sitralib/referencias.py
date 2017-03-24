from sitralib.helpers.funciones import Helpers


class Referencias(object):
    referencias = {
        '64': 'Consulta de grupos extendidos',
        '65': 'Envío comando',
        '66': 'fecha y hora',
        '67': 'Consulta de estructura (parte alta)',
        '68': 'Consulta de estructura (parte baja)',
        '69': 'Envío de estructura (parte alta)',
        '6A': 'Envío de estructura (parte baja)',
        '6B': 'Consulta de matriz de conflictos',
        '6C': 'Envío de matriz de conflictos',
        '6D': 'Consulta de funciones',
        '6E': 'Envío de funciones',
        '6F': 'Consulta de preajustes',
        '70': 'Envío de preajustes',
        '71': 'Consulta de programa de tiempos',
        '72': 'Envío de programa de tiempos',
        '73': 'Consulta de agenda feriados y especial',
        '74': 'Envío de agenda feriados y especial',
        '75': 'Consulta de agenda anual',
        '76': 'Envío de agenda anual',
        '77': 'Consulta de agenda diaria',
        '78': 'Envío de agenda diaria',
        '79': 'Consulta de último evento',
        '7A': 'Consulta de eventos',
        '7D': 'Envío de contraseña hardware',
        '7E': 'Envío de grabación EEPROM',
        'C8': 'Respuesta consulta de grupos extendidos',
        'C9': 'Respuesta envío comando',
        'CA': 'Respuesta envío fecha y hora',
        'CB': 'Respuesta consulta de estructura (parte alta)',
        'CC': 'Respuesta consulta de estructura (parte baja)',
        'CD': 'Respuesta envío de estructura (parte alta)',
        'CE': 'Respuesta envío de estructura (parte baja)',
        'CF': 'Respuesta consulta matriz de conflictos',
        'D0': 'Respuesta envío matriz de conflictos',
        'D1': 'Respuesta consulta de funciones',
        'D2': 'Respuesta envío de funciones',
        'D3': 'Respuesta consulta de preajustes',
        'D4': 'Respuesta envío de preajustes',
        'D5': 'Respuesta consulta de programa de tiempos',
        'D6': 'Respuesta envío de programa de tiempos',
        'D7': 'Respuesta consulta de agenda feriados y especial',
        'D8': 'Respuesta envío de agenda feriados y especial',
        'D9': 'Respuesta consulta de agenda anual',
        'DA': 'Respuesta envío de agenda anual',
        'DB': 'Respuesta consulta de agenda diaria',
        'DC': 'Respuesta envío de agenda diaria',
        'DD': 'Respuesta consulta de último evento',
        'DE': 'Respuesta consulta de eventos',
        'E1': 'Respuesta envío de contraseña hardware',
        'E2': 'Respuesta envío de grabación EEPROM',
    }

    def __init__(self):
        self.helpers = Helpers()

    def __exists(self, num):
        """
        Valida si el valor hexadecimal esta dentro de las referencias.
        :param num: string hexadecimal
        :return: boolean
        """
        return True if num in self.referencias else False

    def respuesta(self, num):
        """
        Retorna una respuesta al codigo ofrecido. Error si no es  un
        valor hexadecimal, exitoso si es un valor existente en el diccionario e
        inválido si no existe en el diccionario.
        :param num: string Valor hexadecimal
        :return: string
        """
        codigo = num.strip().upper()
        if not self.helpers.isHex(codigo):
            return "El valor que introdujo no es un número hexadecimal"

        if self.__exists(codigo):
            return self.referencias[codigo]

        return "No hay referencias para el código ingresado"


if __name__ == "__main__":
    ref = Referencias()
    respuesta = ref.respuesta('64')
    print(respuesta)
