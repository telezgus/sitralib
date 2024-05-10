# -*- coding: utf-8 -*-
from sitralib.helpers.funciones import Helpers
from sitralib.validators.bcc import Bcc


class ConsultaEstadoExtendido:
  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):
    """Crea la trama de consulta de estado extendido.

    Arguments:
      **kwargs {dict} -- Diccionario con valores para generar la trama.

    Returns:
      [string] -- Trama de estado extendido



    >>> ConsultaEstadoExtendido().create(crs_numero=3000, grp_id_num=30, esclavo=5)
    '00 00 00 00 FF 00 05 1E 64 00 0B 8B 0B B8 38'

    >>> ConsultaEstadoExtendido().create(crs_numero=3000, grp_id_num=30)
    '00 00 00 00 FF 00 00 1E 64 00 0B 8E 0B B8 3D'

    >>> ConsultaEstadoExtendido().create(crs_numero='3000', grp_id_num='30')
    '00 00 00 00 FF 00 00 1E 64 00 0B 8E 0B B8 3D'

    >>> ConsultaEstadoExtendido().create()
    Traceback (most recent call last):
     ...
    KeyError: 'crs_numero'

    >>> ConsultaEstadoExtendido().create(crs_numero=3000)
    Traceback (most recent call last):
     ...
    KeyError: 'grp_id_num'


    """
    numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

    trama = {
      1: '00',
      2: '00',
      3: '00',
      4: '00',
      5: 'FF',
      6: '00',
      7: self.helpers.intToHexString(kwargs.get('esclavo', 0)), # Esclavo
      8: self.helpers.intToHexString(kwargs['grp_id_num']),
      9: '64',  # Codigo según Protocolo
      10: '00',
      11: '0B',
      12: '00',  # BCC intermedio
      13: numeroControlador[:-2],
      14: numeroControlador[-2:],
      15: '00',  # BCC
    }

    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None


if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
