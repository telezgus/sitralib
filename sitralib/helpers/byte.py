
class Byte(object):
  def __init__(self, number):
    if self.__isstr(number):
      number = self.__strToInt(number)

    if not self.__isByte(number):
      raise Exception("{0} no es un integer".format(number))

    self.number = number

  def __isstr(self, num):
    if type(num) == str:
      return True

  def __strToInt(self, num):
    return int(num, 16)

  def __isInt(self, number):
    if type(number) == int:
      return True

  def __isByte(self, number):
    if self.__isInt(number):
      if len(bin(number)[2:]) <= 8:
        return True

  def __format(self, num, size=8):
    return str(bin(num)[2:].zfill(size))

  def __reverseBynary(self):
    cadena = self.__format(self.number)
    l = list(cadena)
    l.reverse()
    return l

  @property
  def binaryReversed(self):
    return self.__reverseBynary()

  @property
  def binary(self):
    return self.__format(self.number)

  def __highNibble(self):
    return self.number >> 4

  @property
  def highNibble(self):
    return self.__format(self.__highNibble(), 4)

  def __lowNibble(self):
    return self.number & 0x0F  # p0x0F == 15

  @property
  def lowNibble(self):
    return self.__format(self.__lowNibble(), 4)
