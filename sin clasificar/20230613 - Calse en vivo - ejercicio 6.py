numeros_impares = list (range(1,101,2))
suma_impares = sum(numeros_impares)
print("la suma de todos los numeros impares del 0 al 100 es: ",suma_impares)
print(numeros_impares)

numeros = [3,4,8,9]

while True:
    numero = int(input("Ingrese un numero entero del 0 al 9"))
    if 0<= numero <=9:
        if numero in numeros:
            print("El numero ", numero, "Se encuentra en la lista.")
            break
        else:
            print("el numero ingresado no es valida. Intentlo nuevamente.")