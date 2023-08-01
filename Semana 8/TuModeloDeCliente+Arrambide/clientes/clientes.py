

class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.puntos = 0
        self.compras = []  

    def agregar_puntos(self, puntos):
        self.puntos += puntos

    def canjear_puntos(self, puntos):
        if puntos <= self.puntos:
            self.puntos -= puntos
            print(f"{puntos} puntos canjeados.")
        else:
            print("No alcanzan los puntos para canjear.")

    def registrar_compra(self, descripcion, monto): # Registra una compra del cliente con su descripción y monto
        compra = {"descripcion": descripcion, "monto": monto}
        self.compras.append(compra)

    def __str__(self):
        cliente_info = f"Cliente: {self.nombre}\nCorreo: {self.correo}\nDirección: {self.direccion}\nPuntos de fidelidad: {self.puntos}"
        if self.compras:
            compras_info = "\nCompras realizadas:"
            for compra in self.compras:
                compras_info += f"\n- {compra['descripcion']}: ${compra['monto']}"
            return cliente_info + compras_info
        else:
            return cliente_info