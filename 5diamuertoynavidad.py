#Calcule los días que faltan para día de muertos y navidad
from datetime import date #me permite manejar fechas
año=int(input("Ingrese año: "))
mes=int(input("Ingrese mes: "))
dia=int(input("Ingrese dia: "))

dia_muerto=date(2024,11,2)
dia_navidad=date(2024,12,24)
fecha_actual=date(año,mes,dia)

dif_muertos=dia_muerto-fecha_actual
print("Días faltan para día de muertos: ", dif_muertos)

dif_navidad=dia_navidad-fecha_actual
print("Días faltan para navidad: ", dif_navidad)
