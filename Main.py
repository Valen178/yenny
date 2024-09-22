from Venta import Venta
from DetalleVenta import DetalleVenta
from Libro import Libro
from Categoria import Categoria

class Main:
    categoria_fantasia = Categoria(1, "Fantasia")
    categoria_terror = Categoria(2, "Terror")
    categoria_romance = Categoria(3, "Romance")

    libro1 = Libro(1001, "Harry Potter y la Piedra Filosofal", categoria_fantasia, "Harry Potter se ha quedado huérfano y vive en casa de sus abominables tíos y del insoportable primo Dudley. Se siente muy triste y solo, hasta que un buen día recibe una carta que cambiará su vida para siempre. En ella le comunican que ha sido aceptado como alumno en el colegio interno Hogwarts de magia y hechicería.", "J. K. Rowling", 16000, 50)
    
    libro2 = Libro(1002, "Juego de tronos", categoria_fantasia,"Juego de tronos es la historia de la lucha por un trono, el trono de hierro, forjado con las espadas de los enemigos vencidos. Siete son los reinos de Poniente y muchas las casas que se disputarán la corona: los herederos, los exiliados, los despojados y los actuales regentes.", "George R. R. Martin",18000, 15)

    libro3 = Libro(1003, "Percy Jackson Y El Ladron Del Rayo", categoria_fantasia,"Cuenta las aventuras de un chico actual de doce años, Percy Jackson, cuando descubre que es un semidiós; hijo de una mortal y del dios griego, Poseidón. Percy y sus amigos realizan una búsqueda para prevenir una guerra apocalíptica entre los dioses griegos Zeus y Poseidón.", "Rick Riordan",20500, 64)

    libro4 = Libro(1004, "Asylum", categoria_terror,"Para Dan Crawford, el programa de verano para alumnos sobresalientes es una oportunidad única. Sus amigos nunca comprendieron su fascinación por la historia y la ciencia. Pero en el Colegio Preparatorio New Hampshire, esas preferencias están a la orden del día. Al llegar al lugar, se encuentra con que la residencia a la que debía ir ha sido cerrada, por lo cual todos los estudiantes se ven forzados a quedarse en Brookline, lo que solía ser un hospital psiquiátrico.", "Madeleine Roux",12500, 20)

    libro5 = Libro(1005, "Llámame por tu nombre", categoria_romance,"En el verano de 1983, en la campiña italiana, un adolescente establece un vínculo con el carismático asistente de investigación de su padre que les cambia la vida. Ve todo lo que quieras. James Ivory ganó el Óscar a mejor guion adaptado y Timothée Chalamet fue nominado por su actuación.", "André Aciman",17000, 88)

    libro6 = Libro(1006, "Nosotros en la luna", categoria_romance,"Cuando Rhys y Ginger se conocen en las calles de la ciudad de la luz, no imaginan que sus vidas se unirn para siempre, a pesar de la distancia y de que no puedan ser ms diferentes. Ella vive en Londres y a veces se siente tan perdida que se ha olvidado hasta de sus propios sueos", "Alice Kellen" ,15000, 48)

    categoria_fantasia.agregarLibro(libro1)
    categoria_fantasia.agregarLibro(libro2)
    categoria_fantasia.agregarLibro(libro3)
    categoria_terror.agregarLibro(libro4)
    categoria_romance.agregarLibro(libro5)
    categoria_romance.agregarLibro(libro6)

    print(f"Precio del libro {libro1.titulo}: {libro1.precio}")
    libro1.modificarPrecio(10000)
    print(f"Nuevo precio del libro {libro1.titulo}: {libro1.precio}")

    venta1 = Venta(1)
    venta2 = Venta(2)

    venta1.agregarLibro(libro1,2)
    venta1.agregarLibro(libro2, 4)
    venta1.agregarLibro(libro6,1)

    venta2.agregarLibro(libro5,1)
    venta2.agregarLibro(libro4,1)

    print(venta1)
    print(venta2)