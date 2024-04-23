#Calcule el incremento salarial de una persona: Si su salario es menor a 15mil el incremento será del 20% y si es mayor a 
#15mil el incremento será del 15%
salario=float(input("Ingrese el salario: "))
if salario <= 15000:
    aumento=(salario*20)/100
    print("El aumento del salario corresponde al 20%, el valor es: ", aumento)
else:
    aumento=(salario*15)/100
    print("El aumento del salario corresponde al 15%, el valor es: ", aumento)