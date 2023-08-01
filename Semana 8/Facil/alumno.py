class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("Nota: ", self.nota)
