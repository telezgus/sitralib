from sitralib.helpers.funciones import *


class Fecha(object):
    def __init__(self):
        self.helpers = Helpers()

    def fecha(self, **kwargs):
        timestamp = self.__normalizar_fecha(
            year=kwargs["year"],
            month=kwargs["month"],
            day=kwargs["day"],
            hour=kwargs["hour"],
            minutes=kwargs["minutes"],
            seconds=kwargs["seconds"]
        )

        d = {
            'year': kwargs["year"],
            'month': kwargs["month"],
            'day': kwargs["day"],
            'hour': kwargs["hour"],
            'minutes': kwargs["minutes"],
            'seconds': kwargs["seconds"],
            'timestamp': timestamp,
            'wday': self.__day_of_week(kwargs["wday"])
        }
        return d

    def __normalizar_fecha(self, **kwargs):
        date_separator = '-'
        time_separator = ':'

        datetime = '{0}{6}{1}{6}{2}T{3}{7}{4}{7}{5}'.format(
            kwargs["year"],
            kwargs["month"],
            kwargs["day"],
            kwargs["hour"],
            kwargs["minutes"],
            kwargs["seconds"],
            date_separator,
            time_separator
        )
        return datetime

    def __day_of_week(self, tm_wday):
        wday = self.helpers.hexToDec(tm_wday)
        dias = {
            1: 'domingo',
            2: 'lunes',
            3: 'martes',
            4: 'miércoles',
            5: 'jueves',
            6: 'viernes',
            7: 'sábado'
        }
        return dias[wday]


if __name__ == "__main__":
    help_text = """
    Retorna un diccionario con los datos indexados y
    la fecha en formato timestamp (ISO)
    Ejemplo:

        a = Fecha()
        b = a.fecha('2015', '05', '09', '06', '29', '00', '01')
        print(b)
    """
    print(help_text)
    a = Fecha()
    b = a.fecha(
        year='2015',
        month='05',
        day='09',
        hour='06',
        minutes='29',
        seconds='00',
        wday='01'
    )
    print(b)
