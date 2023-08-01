class Televisor:
    def __init__(self, precio_base = 100, color = "blanco", consumo_energetico ="F", peso = 5 ):
        self.precio_base = precio_base
        self.color = self.__comprobar_color(color)
        self.consumo_energetico = self.__comprobar_consumor_energetico(consumo_energetico)
        self.peso = peso 

    def __comprobar_consumor_energetico(sefl, consumo):
        letras_validas =  ["A","B","C","D","E","F"]
        if consumo.upper() in letras_validas:
            return consumo.upper
        else:
            return "F"
        
    def __comprobar_color(self, color):
        listado_de_colores = ["azul","rojo","gris","blanco","negro"]
        if color.lower() in listado_de_colores:
            return color.lower
        else:
            return "blanco"
        
    def __calcular_precio_tamano (self):
        if self.peso <20:
            return 10
        elif self.peso <50:
            return 50
        elif self.peso <80:
            return 80
        else:
            return 100
        
    def __calcular_precio_letra (self):
          precio_consumo = {"A":100, "B":80,"C":60,"D":50,"E":30,"F":10}
          return precio_consumo[self.consumo_energetico]
    
    def precio_final(self):
        precio_tamano = self.__calcular_precio_tamano()
        precio_letra = self.__calcular_precio_letra()
        return self.precio_base + precio_letra + precio_tamano
  
    def total_a_pagar (televisores):
      total_pagar = 0 
      for televisor in televisores:
        total_pagar += televisor.precio_final
      return total_pagar

televisores=[
      Televisor(250,"rojo","E",10),
      Televisor(143,"negro","C",13),
      Televisor(54,"gris","A",7),
      Televisor(300,"violeta","B",23)]

print("el total a pagar por los televisores es de: ")