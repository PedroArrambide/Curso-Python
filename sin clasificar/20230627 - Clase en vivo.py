def suma (a,b):
    resultado = (a+b)
    return resultado
print(suma(2,3))

def welcome (ciudad):
    return f"bienvenido a la ciudad {ciudad}!"
nombre_ciudad = input("Coloca el nombre de la ciudad: ")

print(welcome(nombre_ciudad))

"primer ejercicio"

def promedio (numeros):
    suma = sum(numeros)
    media = suma / len(numeros)
    return media 
muestra = [2,3,4,5]
media_resultado = promedio(muestra)
print ("La media de la muestra es: ", media_resultado)

"usuando arg"

def promedio (*args):
    lista = list(args)
    suma = sum(lista)
    media = suma / len(lista)
    return media 
media_resultado = promedio(2,3,4,5,6,7)
print ("La media de la muestra es: ", media_resultado)

"segundo ejercicio"

def es_multiplo (nun1,nun2):
    if nun1 % nun2 == 0 or nun2 % nun1 == 0:
        return print("Al menos uno de los dos es multiplo")
    else:
        return print("ninguno es multiplo") 
nun1 = int(input("ingres el primer numero: "))
nun2 = int(input("ingres el segundo numero: "))

print(es_multiplo(nun1,nun2))

def es_multiplo (nun1,nun2):
    if nun1 % nun2 == 0:
        return f"{nun1} es multiplo de {nun2}"
    elif nun2 % nun1 == 0:
        return f"{nun2} es multiplo de {nun1}"
    else:
        return print("ninguno es multiplo") 
nun1 = int(input("ingres el primer numero: "))
nun2 = int(input("ingres el segundo numero: "))

print(es_multiplo(nun1,nun2))

"ejercicio anio bisiesto"
def anio_bisiesto (anio):
    if anio.isnumeric():
        anio = int(anio)
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            return f"{anio} es bisiesto"
        else :
            return f"{anio} no es bisiesto"
    else:
        return f"{anio} no es un año"
anio_ingresar = input("ingresa un anio: ")
print(anio_bisiesto (anio_ingresar))

def separar_lista(lista):
    lista_pares=[]
    lista_impares=[]

    for num in lista:
        if num % 2 ==0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
    lista_pares.sort()
    lista_impares.sort()
    return  lista_pares , lista_impares

numeros = [4,8,2,32,45,87,65,2156,2,6,8454,5651,6487,5165,5465,5232]
pares, impares = separar_lista(numeros)
print ("lista de numeros pares: ", pares)
print ("lista de numeros impares: ", impares)

def conversor(*args):
    if len(args) == 1:
        milimetros = args[0]
        centimetros = args[0] / 10
        metros = args[0] /1000
        return milimetros, centimetros, metros
    elif len(args) == 3:
        milimetros = args[0]
        centimetros = args[1]
        metros = args[2]
        return milimetros, centimetros, metros
    else:
        return "Solo funciona con 3 argumentos"
print(conversor(1000))
print(conversor(2,30,5))