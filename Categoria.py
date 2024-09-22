class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.lista_libros = []

    def modificarIdCategoria(self, nuevo_id):
        self.id_categoria = nuevo_id

    def modificarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def agregarLibro(self,libro):
        if libro not in self.lista_libros:
            self.lista_libros.append(libro)
            libro.categoria = self
        else:
            print(f"el libro: {libro.titulo} no se puede agregar a la categoría {self.nombre} porque ya está en una categoría")
    
    def eliminarLibro(self,libro):
        if libro in self.lista_libros:
            self.lista_libros.remove(libro)
            libro.categoria = None
        else:
            print(f"el libro: {libro.titulo} no se puede eliminar a la categoría {self.nombre} porque no está en esta categoría")
    
    def listarLibros(self):
        if self.lista_libros:
            print(f"Los libros de la categoría {self.nombre}")
            for libro in self.lista_libros:
                print(f"Titulo {libro.titulo}")
        else:
            print(f"No hay libros en la categoría {self.nombre}")
    
    def __str__(self):
        return f"Categoría: {self.nombre} (ID: {self.id_categoria})"
