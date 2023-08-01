hobbies = []
for i in range(3):
    hobby = input("Ingresa tu hobby favorito: ")
    hobbies.append(hobby)

try:
    with open ("C:/Users/Pedro M. Arrambide/Curso Python/Semana 8/Mishobbiesfavoritos/mishobbiesfavorito.txt.txt", "a") as archivo:
         for hobby in hobbies:
             archivo.write(hobby + "\n")
    print("Los datos se han guardado en el archvio mishobiesfavorito.txt")
except IOError:
    print("Ocurrio un error al intentar guardar los datos en el archivo")    