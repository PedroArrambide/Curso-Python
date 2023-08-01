from clientes import Cliente


cliente1 = Cliente("Matias Serrano", "m.serrano@coder.com.ar", "calle 1 123, Cordoba","3515952666")
cliente2 = Cliente("Pedro Alumno", "pedro.alumno@aprueboseguro.com.ar", "Termino el curso 10, Aprobado","3517565555")
cliente3 = Cliente("Edgardo Ramirez", "estarabien@mesaliobien.com", "ojala queapruebe 10, Classe", "351-59526333")

cliente1.agregar_puntos(50)
cliente1.registrar_compra("Producto 1", 100)

cliente2.agregar_puntos(100)
cliente2.registrar_compra("Producto 2", 50)

cliente1.canjear_puntos(20)
cliente2.canjear_puntos(150)
cliente3.canjear_puntos(10)

cliente3.registrar_compra("Producto 1", 100)
cliente3.registrar_compra("Producto 2", 50)
cliente3.agregar_puntos(300)

print("Información del cliente 1:")
print(cliente1)

print("\nInformación del cliente 2:")
print(cliente2)

print("\nInformación del cliente 3:")
print(cliente3)


