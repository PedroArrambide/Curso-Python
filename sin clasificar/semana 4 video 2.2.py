valor = 5
cadena = f"la suma entre 5 y 10 es {valor + 10}"
print (cadena )

cadena = "la suma entre {} y 10 es {}".format(valor, valor+10)
print (cadena)

mun = 5
while mun>0:
    print(f"{mun}")
    mun-= 1
    print("dimos una vuelta albucle")

"para limpiar un bucle infinito tengo que, apretando ctrl + c"

"continue = nos permite omitir alguan intereaccion actual del bucle por alguna condicion"
i = 0 
while i<6:
    i+=1
    if i == 3:
        continue
    print(i)

"Pass = nos sirve para encontrar errores y nosabemos donde esta el problema. nos permite escribir codigo que no se ejecutara"
n = 0 
while n<10:
    n+=1
    if n == 2:
        continue
    print("n vale ", n)

n = 0 
while n<10:
    n+=1
    if n == 2:
        pass
    print("n vale ", n)

"break = interrumpe la interaccion actual y se sale del bucle para seguir con el codigo "

i = 0
while i <6:
    i+=1
    if i == 3:
        break
    print(i)   

"while else = esta ultima establece una condicion en la salida del codigo while sin que haya un break"

chance = 1
while chance <=3:
    txt = input("escribe la palabra SI: ")
    if txt =="SI":
        print("Ok, lo lograste en el itento ", chance)
        break
    chance +=1
else:
    print("has agotado tus tres intentos")
        


        