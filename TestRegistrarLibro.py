import sqlite3
import unittest
import tkinter as tk
from LibroVentana import add_book, connect_db


class TestRegistrarLibro(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        precio FLOAT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        categoria_id INTEGER,
                        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
                    )''')
        self.conn.commit()
        
        self.title_entry = tk.Entry()
        self.author_entry = tk.Entry()
        self.price_entry = tk.Entry()
        self.quantity_entry = tk.Entry()
        self.category_entry = tk.Entry()
        self.book_list = tk.Listbox()

        self.title_entry.insert(0, "Libro Test")
        self.author_entry.insert(0, "Autor Test")
        self.price_entry.insert(0, "10000")
        self.quantity_entry.insert(0, "10")
        self.category_entry.insert(0, "1")

        
    def test_verificar_si_existe_libro(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE titulo = ?", ("Libro Test",))
        book = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(book, "El libro no se insertó correctamente en la base de datos.")
    
    def test_verificar_si_el_titulo_es_correcto(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE titulo = ?", ("Libro Test",))
        book = cursor.fetchone()
        conn.close()
        self.assertEqual(book[1], "Libro Test")  
    
    def test_verificar_si_el_autor_es_correcto(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE autor = ?", ("Autor Test",))
        book = cursor.fetchone()
        conn.close()
        self.assertEqual(book[2], "Autor Test")
    
    def test_verificar_si_el_precio_es_correcto(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE precio = ?", (10000,))
        book = cursor.fetchone()
        conn.close()
        self.assertEqual(book[3], 10000)
    
    def test_verificar_si_el_stock_es_correcto(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE cantidad = ?", (10,))
        book = cursor.fetchone()
        conn.close()
        self.assertEqual(book[4], 10)
    
    def test_verificar_si_la_categoria_es_correcta(self):
        add_book(self.title_entry, self.author_entry, self.price_entry, self.quantity_entry, self.category_entry, self.book_list)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE categoria_id = ?", (1,))
        book = cursor.fetchone()
        conn.close()
        self.assertEqual(book[5], 1)
    
    

        
if __name__ == '__main__':
    unittest.main()