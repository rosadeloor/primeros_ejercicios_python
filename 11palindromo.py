#Valide si una palabra o frase es palíndromo.
palabra=input("Ingrese una palabra o frase: ")
a = 0
b=len(palabra) - 1

for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
         a += 1
         b -= 1
        else:
         print("Palabra ", palabra, " NO es palindromo")


print("Palabra ", palabra, " SI es palindromo")