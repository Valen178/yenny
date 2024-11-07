class DetalleVenta:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad
        self.precio_unitario = libro.precio

    def calcularTotalDetalle(self):
        return self.precio_unitario * self.cantidad

    def __str__(self):
        return f"Libro: {self.libro.titulo}, Cantidad: {self.cantidad}, Precio Unitario: {self.precio_unitario}, Total: {self.calcularTotalDetalle()}"