"For = se utiliza para recorrer los elementos de un objeto iterable y ejecutar un bloque de codigo"
lista = [1,2,3,4,5]
for elemento in lista:
    print("Soy un item de la lista y valgo ", elemento)

lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    print("Soy un valor de la lista y valdo ", num)
    num*=5
    print("Me actualice y ahora valgo ", num)

indice = 0 
numeros = [1,2,3,4,5,7,8,9,10,23]
for numero in numeros:
    numeros[indice]*=5
    indice+=1
print(numeros)

"Enumerate = lectura secuencial de clave valor - indice, valor"

indice = 0 
numeros = [1,2,3,4,5,7,8,9,10,23]
for indice , numero in enumerate (numeros):
    numeros[indice]*=5
print (numeros)

texto = "Hola estoy susando for en python "
for letra in texto:
    print(letra)
texto2 = ""
for letra in texto:
    texto2 = letra*2
print(texto2)

"Range = nos devuelve una secuncia de numeros inmutables range(fin): cantidad de valores fijas, range(inicio, fin) toma la secuencia de inico a fin, range(incio, fin, [paso]) arranc de incio a fin saltando de paso a paso"

for numero in range(10):
    print(numero)

for numero in range(5,10):
    print(numero)
...
for numero in range(1,10,2):
    print(numero)
...

"For - Else = establece un bloque de codigo que se ejecuta cuando se termina el for"

print("inciamos el ejercico de range")
for numero in range(10):
        print(numero)
else: print("Terminamos la cuenta")

print("iniciamos ejercio utilizadno pass, continue y break para reemplzar el while")
for numero in range (10):
    pass
    if numero==2:
        continue
    elif numero == 8:
        break
    else:
        print("El numero es ",numero)