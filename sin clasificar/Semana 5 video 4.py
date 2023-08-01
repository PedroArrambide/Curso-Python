"funciones recursivas y funciones integradas"
def cuenta_regresiva(numero):
    print(numero)
    numero -=1
    if numero>0:
        cuenta_regresiva(numero)
    else: 
        print("despegue!!!")
    print("fin de la funcion", numero)

cuenta_regresiva(10)