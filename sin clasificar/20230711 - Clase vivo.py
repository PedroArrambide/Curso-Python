class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo 

auto1 =  Auto("Toyota","Corolla")

print("Marca: ", auto1.marca)
print("Modelo: ", auto1.modelo)

"Ejemplo en vivo trabaando con el Drawl0"

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 

    def imprimir(self):
        print ("Nombre del alumno: ", self.nombre ) 
        print ("Nota del alumno:" , self.nota )

    def resultado(self):
        if self.nota >=6:
            print("aprobado")
        else:
            print ("desaprobado")
alumno1 = Alumno("juan",9)
alumno2 = Alumno("Pedro",5)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()

class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado.")

    def tocar_bocina(self):
        print("El vehículo ha tocado la bocina.")

class Auto(Vehiculo):
    def abrir_capot(self):
        print("Se ha abierto el capot del auto.")

class Lancha(Vehiculo):
    def __init__(self, nombre_motor):
        self.nombre_motor = nombre_motor

class MovimientosEmbarcacion(Lancha):
    def virar_a_estribor(self):
        print("La embarcación ha virado a estribor.")

    def virar_a_babor(self):
        print("La embarcación ha virado a babor.")

# Crear un objeto de la clase Auto y llamar a los métodos
auto = Auto()
auto.arrancar()
auto.tocar_bocina()
auto.abrir_capot()

print()  # Separador de línea

# Crear un objeto de la clase Lancha y mostrar el nombre del motor
lancha = Lancha("Motor Lancha")
print("Nombre del motor de la lancha:", lancha.nombre_motor)

print()  # Separador de línea

# Crear un objeto de la clase MovimientosEmbarcacion y llamar a los métodos
embarcacion = MovimientosEmbarcacion("Motor Embarcación")
embarcacion.arrancar()
embarcacion.tocar_bocina()
embarcacion.virar_a_estribor()
embarcacion.virar_a_babor()


