#Reciba un año y te responda si es o no es bisiesto.
año=int(input("Ingrese el año: "))

def bisiesto(año):
    if año%4==0 and año%100!=0:
        return True
    elif año%100==0 and año%400==0:
        return True
    else:
        return False
    

if bisiesto(año) == True:
    print("El año ", año, " Es bisiesto")
else:
    print("El año ", año, " NO es bisiesto")
