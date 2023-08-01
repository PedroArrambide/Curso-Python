class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass
    def caminar(self):
        pass
    def describeme(self):
        print ("soy un animal del tipo", type(self).__name__)
        
class Perro(Animal):
    def hablar(self):
        print("Guau guau")
    def caminar(self):
        print("Cuatro patas")

class Vaca(Animal):
    def hablar(self):
        print("muu")
    def caminar(self):
        print("Cuatro patas")

class Abeja(Animal):
    def hablar(self):
        print("bzz")
    def caminar(self):
        print("Volando")
    def picar(self):
        print("picar")

mivaca = Vaca("mamifero",10)
mibeja = Abeja("Insecto",25)
perro1 = Perro("Mamifero", 2)


perro1.hablar
mivaca.hablar
mibeja.hablar
     



