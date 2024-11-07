import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

def connect_db():
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        precio FLOAT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        categoria_id INTEGER,
                        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
                    )''')
    conn.commit()
    return conn

def add_book(title_entry, author_entry, price_entry, quantity_entry, category_entry, book_list):
    title = title_entry.get()
    author = author_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    category_id = category_entry.get()
    
    if title and author and price and quantity and category_id:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO libros (titulo, autor, precio, cantidad, categoria_id) VALUES (?, ?, ?, ?, ?)", (title, author, float(price), int(quantity), int(category_id)))
            conn.commit()
            conn.close()
            update_book_list(book_list)
            title_entry.delete(0, tk.END)
            author_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar libro: {e}")
    else:
        messagebox.showwarning("Error en el ingreso", "Todos los campos son obligatorios.")

def delete_book(book_list):
    selected = book_list.curselection()
    if selected:
        index = selected[0]
        book_id = book_list.get(index).split(" - ")[0]
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM libros WHERE id = ?", (book_id,))
            conn.commit()
            conn.close()
            update_book_list(book_list)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el libro: {e}")
    else:
        messagebox.showwarning("Error de selección", "Seleccione un libro para eliminar.")

def update_book(book_list):
    selected = book_list.curselection()
    if selected:
        index = selected[0]
        book_id = book_list.get(index).split(" - ")[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT titulo, autor, precio, cantidad, categoria_id FROM libros WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        
        if book:
            new_title = simpledialog.askstring("Actualizar libro", "Ingresar nuevo titulo:", initialvalue=book[0])
            new_author = simpledialog.askstring("Actualizar libro", "Ingresar nuevo autor:", initialvalue=book[1])
            new_price = simpledialog.askfloat("Actualizar libro", "Ingresar nuevo precio:", initialvalue=book[2])
            new_quantity = simpledialog.askinteger("Actualizar libro", "Ingresar nueva cantidad:", initialvalue=book[3])
            new_category_id = simpledialog.askinteger("Actualizar libro", "Ingresar nuevo ID de categoria:", initialvalue=book[4])
            
            if new_title and new_author and new_price and new_quantity and new_category_id:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE libros SET titulo = ?, autor = ?, precio = ?, cantidad = ?, categoria_id = ? WHERE id = ?",
                        (new_title, new_author, new_price, new_quantity, new_category_id, book_id)
                    )
                    conn.commit()
                    conn.close()
                    update_book_list(book_list)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo actualizar el libro: {e}")
            else:
                messagebox.showwarning("Error en el ingreso", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Error de selección", "Por favor seleccione un libro para actualizar")

def update_book_list(book_list):
    book_list.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, precio, cantidad, categoria_id FROM libros")
    books = cursor.fetchall()
    conn.close()
    for book in books:
        book_list.insert(tk.END, f"{book[0]} - {book[1]} de {book[2]}, ${book[3]}, Stock: {book[4]}, ID categoria: {book[5]}")

def open_book_crud(root, open_main_window):
    root.destroy()
    book_window = tk.Toplevel()
    ancho_ventana = 600
    alto_ventana = 750
    x_ventana = book_window.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = book_window.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    book_window.geometry(posicion)
    book_window.title("Gestión de libros")
    book_window.configure(bg="#f8f8f8")
    # book_window.geometry("400x700")

    tk.Label(book_window, text="Titulo:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
    title_entry = tk.Entry(book_window, width=30, font=("Arial", 12), bg="#e5e5e5")
    title_entry.pack(pady=5)

    tk.Label(book_window, text="Autor:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
    author_entry = tk.Entry(book_window, width=30, font=("Arial", 12), bg="#e5e5e5")
    author_entry.pack(pady=5)

    tk.Label(book_window, text="Precio:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
    price_entry = tk.Entry(book_window, width=30, font=("Arial", 12), bg="#e5e5e5")
    price_entry.pack(pady=5)

    tk.Label(book_window, text="Cantidad:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
    quantity_entry = tk.Entry(book_window, width=30, font=("Arial", 12), bg="#e5e5e5")
    quantity_entry.pack(pady=5)

    tk.Label(book_window, text="ID de categoria:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
    category_entry = tk.Entry(book_window, width=30, font=("Arial", 12), bg="#e5e5e5")
    category_entry.pack(pady=5)

    tk.Button(book_window, text="Agregar libro", command=lambda: add_book(title_entry, author_entry, price_entry, quantity_entry, category_entry, book_list), bg="#d3d3d3",  font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)

    book_list = tk.Listbox(book_window, width=90, height=10)
    book_list.pack(pady=5)

    tk.Button(book_window, text="Actualizar libro seleccionado", command=lambda: update_book(book_list), bg="#d3d3d3",  font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)
    tk.Button(book_window, text="Eliminar libro seleccionado", command=lambda: delete_book(book_list), bg="#d3d3d3",  font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)

    update_book_list(book_list)

    tk.Button(book_window, text="VOLVER",width=10, command=lambda: go_back(book_window, open_main_window), bg="#84001c", fg="#F8F8F8", font=("Arial", 10,"bold"),activebackground= "#6c0017",activeforeground="#eeeeee").pack(pady=10)

def go_back(current_window, open_main_window):
    current_window.destroy()
    open_main_window()