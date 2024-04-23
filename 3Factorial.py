#Encuentre el factorial de cualquier número dado
print("Ingrese un número: ")
num = int (input()) #lee numero
fact = 1
for i in range(1, num+1):
    fact*=i
print ("Factorial de ",num, " es: ", fact) #range me permite establecer el rango numero antes
