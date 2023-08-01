divisas = {'Dolar':'$', 'Euro':'€', 'Libra':'£'}
divisa_a_utilizar = input('¿que divisa desea utilizar?')
informacion = divisas.get(divisa_a_utilizar.capitalize(), 'La divisa ingresada no se encuentra disponible')
print(informacion)