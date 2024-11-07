class Libro:
    def __init__(self, isbn, titulo, categoria, descripcion, autor,  precio, stock ):
        self.isbn = isbn
        self.titulo = titulo
        self.categoria = categoria
        self.descripcion = descripcion
        self.autor = autor
        self.precio = precio
        self.stock = stock
    
    def disminuirStock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -=  cantidad
        else:
            print("No hay suficiente stock")
    
    def agregarStock(self, cantidad):
        self.stock += cantidad
    
    def modificarIsbn(self,nuevo_isbn):
        self.isbn = nuevo_isbn
    
    def modificarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def modificarCategoria(self, nueva_categoria):
        if self.categoria:
            self.categoria.eliminarLibro(self)
        nueva_categoria.agregarLibro(self)
    
    def modificarDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
    
    def modificarAutor(self, nuevo_autor):
        self.autor = nuevo_autor
    
    def modificarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio

    def modificarStock(self, nuevo_stock):
        self.stock = nuevo_stock

    def __str__(self):
        if self.categoria:
            categoria_nombre = self.categoria.nombre
        else:
            categoria_nombre = "Sin Categoría"
        return (f"{self.titulo} - {self.autor},Categoría: {categoria_nombre}, Decripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}")
