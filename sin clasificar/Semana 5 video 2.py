
def saludar_por_nombre():
    nombre = input("Escribe tu nombre: ")
    saludo = "Hola, {}!. Bienvenido al curso de Python".format(nombre)
    return print(saludo)
saludar_por_nombre()

def lista():
    return[1,2,3,4,5]
print(lista()[1:3])

def test():
    return print("python",20,[1,2,3])
test()

def suma(operando1,operando2):
    return (operando1+operando2)
r=suma(7,5)
print (r)
