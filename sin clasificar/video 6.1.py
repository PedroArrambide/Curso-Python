
while(True):
    try:
        a =float(input("ingrese un numero: "))
        b =float(input("ingrese otro numero: "))
        print(a+b)
    except:
        print("no se ha intorducido un numero")
    else:
        print("se ha realizado correctamente la suma")
        break
    finally:
        print ("FIn del bucle")


def dividir (a,b):
    try:
        return a/b
    except Exception as error:
        return f"El error encontrado es del tipo {Exception}"

def mostrar_menu():
    print("----- MENU -----")
    print("1. Soy un string -4 ")
    print("2. 4/0")
    print("3. mostrando codigo")
    print("4. quiero ser numero")
    print("-----------------")
def mostrar_tipo_error(opcion):
    if opcion == 1:
        try:
            resultado = "Soy un string" - 4
        except TypeError as error:
            print("El tipo de error es: ", type(error).__name__)
    elif opcion == 2:
        try:
            resultado = 4/0
        except TypeError as error:
            print("El tipo de error es: ", type(error).__name__)
    elif opcion == 3:
        try:
            print ("mostrando codigo")
        except TypeError as error:
            print("El tipo de error es: ", type(error).__name__)
    elif opcion == 4:
        try:
            resultado = int ("quiero ser un numero ")
        except ValueError as error:
            print("El tipo de error es: ", type(error).__name__)


print('''Menu
----------------------
1. 'Soy un string' - 4
2. 4/0
3. prnt('Mostrando codigo')
4. int('Quiero ser un numero')
''')
opcion = input('Ingrese opcion: ')
try:
  if opcion == '1':
      'Soy un string' - 4
  elif opcion == '2':
    4/0
  elif opcion == '3':
    prnt('Mostrando codigo')
  elif opcion == '4':
    int('Quiero ser un numero')
  else:
    print('Seleccionaste una opcion inexistente.')
except Exception as e:
  print('El tipo de error es', type(e).__name__)

print("""menu
    ------------
    1. Soy un string
    2. 4/0
    3. prnt (mostrarndo un codigo)
    4. int(quiero ser un entero)""")
opcion = input( "ingrese una opcion:")
try:
    if opcion == 1:
        "Soy un string" - 4
    elif opcion == 2:
        4/0
    elif opcion == 3:
        prnt("mostrando codigo")
    elif opcion == 4:
        int("quiero ser numero")
    else:
        print("seleccionaste una opcion invalida")
except Exception as e:
    print ("el tipo de error es", type(e).__name__)