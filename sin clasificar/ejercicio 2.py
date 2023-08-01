Nombre = input('¿Nombre?')
edad = input('¿Edad?')
calle = input('¿Calle y numero?')
Ciudad = input('¿Ciudad?')
datos_de_usuario = {'nombre':Nombre, 'edad':edad, 'calle':calle,'ciudad':Ciudad}
print(datos_de_usuario['nombre'],' tiene ',datos_de_usuario['edad'],' años, y vive en',datos_de_usuario['calle'],datos_de_usuario['ciudad'])