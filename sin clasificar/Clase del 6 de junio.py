nombre = input("¿cual es tu nombre?")
edad = int(input("¿cual es tu edad?"))

cumple_condiciones = (nombre !="****") and (5<edad<20) and (4<= len(nombre)<8) and (edad*3>35)

if cumple_condiciones:
    print ("Se cumplen todas las condiciones")
else:
    print("No se cumplen todas las condiciones")



