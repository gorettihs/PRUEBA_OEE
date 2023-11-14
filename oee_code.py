import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
df=pd.read_excel('/content/drive/Shareddrives/M3001C Sistemas y Tecnologías 4.0 (Industria 4.0)/OEE Bonafont/Registro_Excel.xlsx')

# Funciones para calculo de OEE
def cal_disponibilidad(tTotal,tPlan,tnoPlan,tAlist):
  tdis=tTotal-tPlan
  top=tdis-(tnoPlan+tAlist)
  d=top/tdis
  return d

def cal_rendimiento(tTotal,tPlan,tnoPlan,tAlist,prodT,capMaq):
  tdis=tTotal-tPlan
  top=tdis-(tnoPlan+tAlist)
  r=prodT/(top*capMaq)
  return r

def cal_calidad(prodT,proderror):
  c=(prodT-proderror)/prodT
  return c

def cal_oee(d,r,c):
  oee=d*r*c
  return oee

#Tiempo disponible = tiempo de funcionamiento - tiempo detenido planeado
#Tiempo muerto     = tiempo de paradas        + tiempo de alistamientos
#Tiempo operativo  = Tiempo disponible        - Tiempo muerto
#Producción Total
#Producción con desperfectos

#Hay que preguntar:

#capacidad de la máquina (unidades por hora)
#producción total
#producción con desperfectos

#tiempo (en horas) de funcionamiento
#tiempo detenido planeado
#tiempo de paradas
#tiempo de alistamientos


def entrada_de_datos()
  ## Entrada de datos
  tiempo_funcionamiento=float(input("Establezca de cuántas horas fue el turno: "))
  tiempo_detenido_planeado=float(input("¿Cuántas horas estuvo detenida la máquina dentro de lo planeado?: "))

  tiempo_alistamientos=float(input("¿Cuántas horas del turno destinaron a alistamientos (tales como preparar la máquina o ponerse el equipo de protección)?: "))
  paradas_imprevistas=float(input("¿Cuántas horas duraron las paradas imprevistas en el turno?: "))

  machine_capacity=float(input("Indique cuántas unidades produjo la máquina cada hora en el turno de hoy: "))
  total_production=int(input("¿Cuál fue la producción total de unidades que se obtuvo al final del turno?: "))
  desperfectos=int(input("De la producción total en el turno, indique cuántas unidades presentaron desperfectos: "))
  year_hoy=str(input("Escriba el año de los datos que va a registrar: "))
  mes_hoy=str(input("Escriba el número del mes de los datos que va a registrar: "))
  day_hoy=str(input("Escriba el día de los datos que va a registrar: "))
  return tiempo_funcionamiento,tiempo_detenido_planeado,tiempo_alistamientos,paradas_imprevistas,machine_capacity,total_production,desperfectos,year_hoy,mes_hoy,day_hoy
