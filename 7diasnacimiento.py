#Calcule el número de días que alguien ha vivido tomando en cuenta su fecha de nacimiento
from datetime import date #me permite manejar fechas
año_nac=int(input("Ingrese año nacimiento: "))
mes_nac=int(input("Ingrese mes nacimiento: "))
dia_nac=int(input("Ingrese dia nacimiento: "))

año=int(input("Ingrese año actual: "))
mes=int(input("Ingrese mes actual: "))
dia=int(input("Ingrese dia actual: "))

fecha_nac=date(año_nac,mes_nac,dia_nac)
fecha_actual=date(año,mes,dia)

dif_dias=fecha_actual-fecha_nac
print("Días transcurridos desde su nacimiento: ", dif_dias)