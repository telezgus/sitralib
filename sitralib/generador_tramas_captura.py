# -*- coding: utf-8 -*-
from sitralib.consulta_agenda_anual_semanal import *
from sitralib.consulta_agenda_diaria import *
from sitralib.consulta_estructura_parte_alta import *
from sitralib.consulta_estructura_parte_baja import *
from sitralib.consulta_funciones import *
from sitralib.consulta_matriz_conflicto import *
from sitralib.consulta_programa_tiempos import *
from sitralib.consulta_agenda_feriados_especial import *
from sitralib.consulta_preajustes import *


class GeneradorTramasCaptura(object):
  def __init__(self, **kwargs):
    self.k = kwargs

  def create(self):
    a = self.__get_estructuras()
    b = self.__get_consulta_catriz_conflicto()
    c = self.__get_consulta_funciones()
    d = self.__get_consulta_programa_tiempos()
    e = self.__get_consulta_agenda_diaria()
    f = self.__get_consulta_agenda_anual_semanal()
    g = self.__get_consulta_agenda_feriados_especial()
    h = self.__get_consulta_preajustes()

    return a + b + c + d + e + f + g + h

  def __get_estructuras(self):
    parte_alta = ConsultaEstructuraParteAlta()
    parte_baja = ConsultaEstructuraParteBaja()

    tramas = list()
    for i in range(3):
      tramas.append(
        parte_alta.create(
          crs_numero=self.k['crs_numero'],
          grp_id_num=self.k['grp_id_num'],
          est_numero=i
        )
      )
      tramas.append(
        parte_baja.create(
          crs_numero=self.k['crs_numero'],
          grp_id_num=self.k['grp_id_num'],
          est_numero=i
        )
      )
    return tramas

  def __get_consulta_catriz_conflicto(self):
    o = ConsultaMatrizConflicto()

    trama = o.create(
      crs_numero=self.k['crs_numero'],
      grp_id_num=self.k['grp_id_num']
    )
    return [trama]

  def __get_consulta_funciones(self):
    o = ConsultaFunciones()
    tramas = list()
    for i in range(33):
      tramas.append(
        o.create(
          crs_numero=self.k['crs_numero'],
          grp_id_num=self.k['grp_id_num']
        )
      )
    return tramas

  def __get_consulta_programa_tiempos(self):
    o = ConsultaProgramaTiempos()
    tramas = list()
    for i in range(16):
      tramas.append(
        o.create(
          crs_numero=self.k['crs_numero'],
          grp_id_num=self.k['grp_id_num'],
          esp_numero=i
        )
      )
    return tramas

  def __get_consulta_agenda_diaria(self):
    o = ConsultaAgendaDriaria()
    tramas = list()
    for i in range(12):
      tramas.append(
        o.create(
          crs_numero=self.k['crs_numero'],
          grp_id_num=self.k['grp_id_num'],
          adi_id_num=i
        )
      )
    return tramas

  def __get_consulta_agenda_anual_semanal(self):
    o = ConsultaAgendaAnualSemanal()

    trama = o.create(
      crs_numero=self.k['crs_numero'],
      grp_id_num=self.k['grp_id_num']
    )
    return [trama]

  def __get_consulta_agenda_feriados_especial(self):
    o = ConsultaAgendaFeriadosEspecial()

    trama = o.create(
      crs_numero=self.k['crs_numero'],
      grp_id_num=self.k['grp_id_num']
    )
    return [trama]

  def __get_consulta_preajustes(self):
    o = ConsultaPreajustes()

    trama = o.create(
      crs_numero=self.k['crs_numero'],
      grp_id_num=self.k['grp_id_num']
    )
    return [trama]


if __name__ == "__main__":
  o = GeneradorTramasCaptura(
    crs_numero=3000,
    grp_id_num=1
  )

  print(o.create())
