class Vehiculo:
    def arrancar(self):
        print("el vehiculo ha arrancado")
    def tocar_bocina(sefl):
        print("el vehiculo ha tocado la bocina")

class Auto(Vehiculo):
    def abrir_capot(self):
        print("el chiculo ha abierto el capot")

class Lancha(Vehiculo):
    def __init__(self, motor) :
        self.motor = motor
class Movimientos_embarcacion(Lancha):
    def virar_a_babor(self):
        print("la lancha a virado a babor")
    def virar_a_estribor(self):
        print("la lancha a virado a estribor")

auto = Auto()
auto.abrir_capot()
auto.arrancar()
auto.tocar_bocina()

lancha = Lancha("seehorse")
lancha.arrancar()
lancha.tocar_bocina()
movi = Movimientos_embarcacion("sh")
movi.arrancar()
movi.tocar_bocina()
movi.virar_a_babor()
movi.virar_a_estribor()



