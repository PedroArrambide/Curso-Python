cant_num = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
suma = 0 

for i in range(cant_num):
    num = input("Ingresa un numero o coloca 'exit':")
    if num.lower () == "exit":
        break
    elif num.isnumeric(): 
        num = int(num)
        suma += num

print("la sume es:", suma)