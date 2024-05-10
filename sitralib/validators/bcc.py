# -*- coding: utf-8 -*-
"""Validacion

12 es la posición de la primer validación. Los XOR sumados desde el
primer número hasta el valor previo a la posición 12, deben dar como 
resultado el valor expresado en la posición 12.

Y la suma desde la posición a la ante-ultima debe dar el resultado 
expresado en el valor final.
"""
from sitralib.helpers.funciones import Helpers
from sitralib.helpers.ordenar_trama import OrdenarTrama


class Bcc:
  POSICION_BCC_INTERMEDIO = 12

  def __init__(self):
    self.helpers = Helpers()

  def trama_to_type(self, trama):
    if type(trama) == str:
      ordenar = OrdenarTrama()
      return ordenar.ordenarTrama(trama)

    return trama


  def isValidBcc(self, trama, *args):

    trama = self.trama_to_type(trama)

    bcc1 = self.POSICION_BCC_INTERMEDIO
    bcc2 = self.__posicion_bcc2(trama)

    b1 = self.validateBccIntermadio(trama)
    b2 = self.validateBccFinal(trama, bcc2)

    if bcc1 and bcc2 in trama.keys():
      if self.helpers.hexToDec(trama[bcc1]) == self.helpers\
          .hexToDec(b1) and self.helpers\
          .hexToDec(trama[bcc2]) == self.helpers.hexToDec(b2):
        return True

    return False


  def validateBccIntermadio(self, trama, *args):
    bcc1 = 0
    for i in trama:
      if i == self.POSICION_BCC_INTERMEDIO:
        break
      else:
        bcc1 = bcc1 ^ self.helpers.hexToDec(trama[i])

    return self.helpers.intToHexString(bcc1)


  def validateBccFinal(self, trama, *args):

    bcc_final_position = self.__posicion_bcc2(trama)

    bcc2 = 0
    # al len de la trama hay que sumarle 4 por los 00 hasta FF,
    # luego al range se le suma 1 porque los key comienzan en 0
    for i in range(self.POSICION_BCC_INTERMEDIO, (len(trama) + 5)):

      try:
        if i == bcc_final_position: break
        bcc2 = bcc2 ^ self.helpers.hexToDec(trama[i])
      except KeyError:
        return None

    return self.helpers.intToHexString(bcc2)


  def consolidate(self, trama):
    """Valida que la trama cumpla con la validación de BCC y filtra los
    números que no pertenecen a la trama.
    """
    trama = self.trama_to_type(trama)

    bcc1 = self.validateBccIntermadio(trama)
    trama[self.POSICION_BCC_INTERMEDIO] = bcc1

    bcc2 = self.validateBccFinal(trama)
    trama[self.__posicion_bcc2(trama)] = bcc2

    if self.isValidBcc(trama):
      # Remuevo elementos que no pertenecen a la trama.
      return {i:trama[i] for i in trama if i <= self.__posicion_bcc2(trama)}

    return False


  def __posicion_bcc2(self, trama):
    """Retorna el indice para la posicion del bcc2 en la trama
    :param trama: dict
    :return: integer
    """
    # Cuento el comienzo del diccionario y le resto 1, porque el
    # valor (segun protocolo), inicia en cero.
    return 5 + (self.__longitud_total(trama) - 1)


  def __longitud_total(self, trama):
    """
    Obtengo la posicion para el bcc2
    :param trama:
    :return: integer
    """
    if 10 and 11 in trama:
      return int(trama[10] + trama[11], 16)

    return 0


if __name__ == "__main__":
  trama1 = '00 00 00 00 FF 00 00 1E 64 00 0B 8E 07 84 0D 44 77 22'
  # trama1 = '00 00 00 00 FF 00 00 1E 64 00 0B 8E 07 85 0D'
  trama1 = "00 00 00 00 FF 00 00 01 69 00 F6 61 0B B8 00 04 41 00 00 00 00 00 00 01 00 00 00 00 04 41 00 00 00 00 00 00 00 00 00 00 00 02 21 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 01 14 00 00 00 00 00 00 00 00 00 00 00 01 19 00 00 00 00 00 00 00 00 00 00 00 01 11 00 00 00 00 00 00 00 00 00 00 00 43 31 00 00 00 00 00 00 05 00 00 00 FF A9 32 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 EE"

  # Necesito procesar la trama para convertirla en Diccionario
  separator = '-'*80
  t = '00 00 00 00 FF 00 00 01 61 00 0C 93 0B B9 02 23 88 AA DD EE'
  t = '0 0 0 0 FF 0 0 1 E0 0 21 3F B B6 0 94 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 FF 17'
  a = Bcc()
  trama = a.trama_to_type(t)
  print('BCC intermedio ', a.validateBccIntermadio(trama))
  print('BCC final', a.validateBccFinal(trama))

  b = a.isValidBcc(t)
  print(separator)
  print(b)
  print(separator)
  print(a.consolidate(t))
  print(separator)
  print(a.consolidate(trama1))
  print(separator)
  print(a.isValidBcc(trama1))
