from parcial.DetalleVenta import DetalleVenta
class Venta:
    def __init__(self, id_venta):
        self.id_venta = id_venta
        self.lista_detalles_venta = []

    def agregarLibro(self, libro, cantidad):
        libro.disminuirStock(cantidad)
        detalle = DetalleVenta(libro, cantidad)
        self.lista_detalles_venta.append(detalle)

    def calcularTotalVenta(self):
        total = 0
        for detalle in self.lista_detalles_venta:
            total += detalle.calcularTotalDetalle()
        return total    
            #return sum(detalle.calcular_total() for detalle in self.detalles)

    def __str__(self):
        detalles_str = ""
        for detalle in self.lista_detalles_venta:
            detalles_str += str(detalle) + "\n"
        total_venta = self.calcularTotalVenta()
        return f"Venta ID: {self.id_venta}\nDetalles:\n{detalles_str}\nTotal Venta:{total_venta}"