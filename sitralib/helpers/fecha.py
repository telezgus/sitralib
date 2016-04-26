from sitralib.helpers.funciones import *


class Fecha(object):
    def __init__(self):
        self.helpers = Helpers()

    def fecha(self, year=0, month=0, day=0, hour=0, minutes=0, seconds=0,
              wday=0):
        timestamp = self._normalizarFecha(year, month, day, hour, minutes,
                                          seconds)

        d = {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minutes': minutes,
            'seconds': seconds,
            'timestamp': timestamp,
            'wday': self._dayOfWeek(wday)
        }
        return d

    def _normalizarFecha(self, year=0, month=0, day=0, hour=0, minutes=0,
                         seconds=0):
        dateSeparator = '-'
        timeSeparator = ':'

        dateTime = '{0}{6}{1}{6}{2}T{3}{7}{4}{7}{5}'.format(
            year,
            month, day,
            hour,
            minutes, seconds,
            dateSeparator,
            timeSeparator
        )
        return dateTime

    def _dayOfWeek(self, tmWday):
        wday = self.helpers.hexToDec(tmWday)
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
    b = a.fecha('2015', '05', '09', '06', '29', '00', '01')
    print(b)
