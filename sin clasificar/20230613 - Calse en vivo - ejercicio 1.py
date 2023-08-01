a= float(input("ingrese el primer numero: "))
b= float(input("ingrese el segundo numero: "))
while True: 
    print("\nMENU:")
    print("1. Mostrar la suma de los dos numeros: ") 
    print("2. Mostrar la resta de los dos numeros: ")
    print("3. Mostrar la multiplicacion de los dos numeros: ")  
    print("4. Salir del programa")
    opcion_elegida = int(input("¿que opicon elegís? "))

    if opcion_elegida==1:
        print("\n",a," + ",b," = ",a+b)
    elif opcion_elegida == 2:
        print("\n",a," - ",b," = ",a-b)
    elif opcion_elegida == 3:
        print("\n",a," * ",b," = ",a*b)
    elif opcion_elegida == 4:
        print("salir del programa")
        break
    else:
        print("Opcion no valida. Por favor, seleciono un aopcion valida (1-4).")
        print("------------------------------------\n")

