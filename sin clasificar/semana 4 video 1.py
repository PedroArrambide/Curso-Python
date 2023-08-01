valor = 5
cadena = f"la suma entre 5 y 10 es {valor +10}"
print(cadena)

valor = 5
cadena = " la suma entre {} y 10 es {}".format(valor, valor+10)
print(cadena)

num = 5
while num>0:
    print(f"{num}")
    num-=1
    print ("DIMOS UNA VUELTA AL BUCLE!")

i = 0 
while i < 6:
    i+=1
    if i == 3:
        continue 
    print(i)

n = 0 
while n <10:
    n+=1
    if n == 2:
        continue
    print("n vale ",n)
print("Consulta 2 ")
n = 0 
while n <10:
    n+=1
    if n == 2:
        pass
    print("n vale ",n)

i = 0 
while i <6:
    i+=1 
    if i == 3:
        break
    print (i)

chance = 1

while chance<= 3:
    txt = input("Escribe la palabra SI: ")
    if txt == "SI":
        print("Ok lo lograste en el intento ",chance)
        break
    chance +=1
else: 
    print ("Has agotado tus tres intentos")
