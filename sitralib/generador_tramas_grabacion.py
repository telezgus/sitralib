# -*- coding: utf-8 -*-
from sitralib.compila_envio_agenda_anual_semanal import *
from sitralib.compila_envio_agenda_diaria import *
from sitralib.compila_envio_agenda_feriados_especial import *
from sitralib.compila_envio_estructura_parte_alta import *
from sitralib.compila_envio_estructura_parte_baja import *
from sitralib.compila_envio_funciones import *
from sitralib.compila_envio_grabacion_eeprom import *
from sitralib.compila_envio_matriz_conflictos import *
from sitralib.compila_envio_preajustes import *
from sitralib.compila_envio_programa_tiempos import *


class GeneradorTramasGrabacion:
  def __init__(self, **kwargs):
    self.crs_id                  = kwargs['crs_id']
    self.grp_id_num              = kwargs['grp_id_num']
    self.crs_numero              = kwargs['crs_numero']
    self.programas               = kwargs['programas']
    self.movimientos             = kwargs['movimientos']
    self.agendas_diarias         = kwargs['agendas_diarias']
    self.agendas_semanales       = kwargs['agendas_semanales']
    self.agendas_anuales_semanas = kwargs['agendas_anuales_semanas']
    self.feriados                = kwargs['feriados']
    self.especiales              = kwargs['especiales']

  def create(self):
    a = self.__estructuras()
    b = self.__matriz_conflictos()
    c = self.__envio_funciones()
    d = self.__envio_tiempos()
    e = self.__agendas_diarias()
    f = self.__agendas_anuales_semanas()
    g = self.__agendas_feriados_especial()
    h = self.__preajustes()
    i = self.__eeprom()

    return a + b + c + d + e + f + g + h + i

  def __estructuras(self):
    estructuras = list()
    for item in self.movimientos:
      alta = CompilaEnvioEstructuraParteAlta().create(
        crs_numero=self.crs_numero,
        grp_id_num=self.grp_id_num,
        **item
      )
      estructuras.append(alta)

      baja = CompilaEnvioEstructuraParteBaja().create(
        crs_numero=self.crs_numero,
        grp_id_num=self.grp_id_num,
        **item
      )
      estructuras.append(baja)

    return estructuras

  def __preajustes(self):
    trama = CompilaEnvioPreajustes().create(
      crs_numero=self.crs_numero,
      grp_id_num=self.grp_id_num,
      **self.movimientos[0]
    )
    return [trama]

  def __eeprom(self):
    trama = CompilaEnvioGrabacionEeprom().create(
      crs_numero=self.crs_numero,
      grp_id_num=self.grp_id_num,
      **self.movimientos[0]
    )
    return [trama for i in range(18)]

  def __matriz_conflictos(self):
    trama = CompilaEnvioMatrizConflictos().create(
      crs_numero=self.crs_numero,
      grp_id_num=self.grp_id_num,
      **self.movimientos[0]
    )
    return [trama]

  def __envio_tiempos(self):
    tiempos = []
    for item in self.programas:
      tiempos.append(
        CompilaEnvioProgramaTiempos().create(
          crs_numero=self.crs_numero,
          grp_id_num=self.grp_id_num,
          **item
        )
      )

    return tiempos

  def __envio_funciones(self):
    funciones = []
    for numero in range(0, 32):
      fun = CompilaEnvioFunciones().create(
        crs_numero=self.crs_numero,
        grp_id_num=self.grp_id_num,
      )
      funciones.append(fun)

    return funciones

  def __agendas_diarias(self):
    adi = CompilaEnvioAgendaDiaria()

    l = list()
    d = dict()
    #for i in range(1, 13):
    for i in range(12):
      l = []
      for item in self.agendas_diarias:
        if item['adi_id_num'] == i:
          l.append(item)
      d.update({i: l})

    # Creo una trama por agenda y las compilo en un listado
    tramas = list()
    #for i in range(1, 13):
    for i in range(12):
      a = adi.create(
        *d[i],
        crs_numero=self.crs_numero,
        grp_id_num=self.grp_id_num,
        adi_id_num=d[i][0]['adi_id_num']
      )
      tramas.append(a)

    return tramas

  def __agendas_anuales_semanas(self):
    trama = CompilaEnvioAgendaAnualSemanal().create(
      agendas_anuales_semanas=self.agendas_anuales_semanas,
      agendas_semanales=self.agendas_semanales,
      crs_numero=self.crs_numero,
      grp_id_num=self.grp_id_num,
    )
    return [trama]

  def __agendas_feriados_especial(self):
    trama = CompilaEnvioAgendaFeriadosEspecial().create(
      feriados=self.feriados,
      especiales=self.especiales,
      crs_numero=self.crs_numero,
      grp_id_num=self.grp_id_num,
    )
    return [trama]


if __name__ == "__main__":


  o = GeneradorTramasGrabacion()
  o.create()
