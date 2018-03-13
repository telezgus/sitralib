from sitralib.helpers.funciones import *
from sitralib.validators.bcc import *
from collections import *
import json


class CompilaEnvioEstructuraParteBaja(object):
  """
  Trama de envío de estructura (parte alta) desde CC hacia EC
  x69
  """

  def __init__(self):
    self.helpers = Helpers()
    self.bcc = Bcc()

  def create(self, **kwargs):

    numeroControlador = self.helpers.intToHexString(kwargs['crs_numero'], 4)

    trama = defaultdict(dict)
    trama[1] = '00'
    trama[2] = '00'
    trama[3] = '00'
    trama[4] = '00'
    trama[5] = 'FF'
    trama[6] = '00'
    trama[7] = '00'
    trama[8] = self.helpers.intToHexString(kwargs['grp_id_num'])
    trama[9] = '6A'  # Codigo según Protocolo
    trama[10] = '00'
    trama[11] = 'F6'
    trama[12] = '00'  # BCC intermedio
    trama[13] = numeroControlador[:-2]
    trama[14] = numeroControlador[-2:]
    trama[15] = self.helpers.intToHexString(kwargs['emo_id_num'])

    intervalos = self.__set_posiciones(**kwargs)
    for i in intervalos:
      trama[i] = intervalos[i]
    trama[250] = '00' # BCC final
    trama_consolidada = self.bcc.consolidate(trama)
    if trama_consolidada:
      return ' '.join(trama_consolidada.values())
    return None

  def __set_posiciones(self, **kwargs):
    clave_inicio = 16
    emo_data = json.loads(kwargs['emo_data'])
    posicion = defaultdict(dict)
    for i in range(18, 36):

      intervalo = self.__set_intervalo(int_valor=i, emo_data=emo_data)
      for dato in intervalo:
        posicion[clave_inicio] = dato
        clave_inicio += 1

    return posicion

  def __set_intervalo(self, **kwargs):
    b = list
    int_valor = kwargs['int_valor']
    data = kwargs['emo_data']
    mov = defaultdict(dict)

    for mov_num in range(1, 17):
      mov[mov_num] = self.helpers.getNibbles(
        data['mov-{0}'.format(mov_num)][int_valor]
      )['lo']

    a = [
      mov[2] + mov[1],
      mov[4] + mov[3],
      mov[6] + mov[5],
      mov[8] + mov[7],
      mov[10] + mov[9],
      mov[12] + mov[11],
      mov[14] + mov[13],
      mov[16] + mov[15]
    ]

    if int_valor >= 34:
      a.append('00')
      a.append('00')
      a.append('00')
      a.append('00')
      a.append('00')
    else:
      a.append(self.helpers.sanitizeHex(data['fun'][int_valor], 2))
      a.append('00')
      a.append('00')
      a.append('00')
      a.append(self.__set_parametro_4(data['fun'][int_valor]))

    return a

  def __set_parametro_4(self, num):
    """
    Setea el parametro 4 como extension.
    :param num: numero hexadecimal
    :return: string
    """
    return 'FF' if int(num, 16) == 5 else '00'
