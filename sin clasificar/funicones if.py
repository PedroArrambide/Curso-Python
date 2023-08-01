a = 195
b = 50
c = 500
if a>b or a>c:
    print("al menos una es verdadera" )

x = 10
if not x>15:
        print ("False")
a = 5 
b = 5
print("a") if a>b else print ("b") 
print("a")  if a>b else print("=") if a == b else print("b")
numero = 24
if numero > 36 :
        print ("el numero es mayor") 
else:
        print("El numero es pequeño")
x = 15
if x>10:
        print("estamos por encima de 10")
        if x>20:
               print("y tambien por encima de 20")
        else: 
               print("pero no por encima de 20")

a = 15
if a == 4:
    print ("A ES IUGAL A CUATRO")
elif a==5:
       print("es igual a 5")
elif a == 6:
       print ("a es igual a 6")
elif a ==7:
       print ("")
else:
       print("no se cumple la condicion")

expersiones = [not False, not 3==5, 33/3==11 and 5>2, True or False, True *5 == 2.5*2 or 123>=23, 12>7 and True > False]
print (expersiones)
