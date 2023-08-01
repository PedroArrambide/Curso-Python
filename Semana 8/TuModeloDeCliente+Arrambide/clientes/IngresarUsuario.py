BD = {}  

def registrar_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    BD[usuario] = contraseña
    print("Se ha registrado con exito")

def iniciar_sesion():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in BD and BD[usuario] == contraseña:
        print("¡Ingreso exitoso!")
    else:
        print("Usuario o contraseña erroneos, Vuelva a intentarlo")

def mostrar_datos():
    print("Los datos almacenado son: ")
    for usuario, contraseña in BD.items():
        print(f"U: {usuario} - P: {contraseña}")

while True:
    print("1. Crear usuario")
    print("2. Inicio de sesión")
    print("3. Ver datos Guardados")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        mostrar_datos()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Ingrese una opción correcta.")

