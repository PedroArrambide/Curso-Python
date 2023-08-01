cantidad_numeros = int(input("Ingrese la cantidad de numroes que dea introducir: "))

numeros =[]
for _ in range(cantidad_numeros):
    numero = float(input("ingresse un numero: "))
    numeros.append(numero)

suma = sum (numeros)
media_aritmetrica = suma / cantidad_numeros 
print ("La media aritmetica de ls numreos ingresados es: ", media_aritmetrica)