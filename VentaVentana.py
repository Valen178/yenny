import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

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

    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        precio_total REAL NOT NULL,
                        fecha TEXT NOT NULL
                    )''')
                    
    cursor.execute('''CREATE TABLE IF NOT EXISTS venta_detalle (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        venta_id INTEGER NOT NULL,
                        libro_id INTEGER NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio_unitario REAL NOT NULL,
                        FOREIGN KEY(venta_id) REFERENCES ventas(id),
                        FOREIGN KEY(libro_id) REFERENCES libros(id)
                    )''')
    conn.commit()
    return conn

def add_to_cart(book_list, quantity_entry, cart_list, cart):
    selected = book_list.curselection()
    if selected:
        index = selected[0]
        book_id, book_title, book_price = book_list.get(index).split(" - ")
        quantity = quantity_entry.get()

        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            subtotal = float(book_price) * quantity
            cart.append((book_id, book_title, quantity, subtotal))
            update_cart_list(cart_list, cart)
            quantity_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error de Entrada", "Por favor ingrese una cantidad válida.")
    else:
        messagebox.showwarning("Error de Selección", "Por favor seleccione un libro para agregar.")

def finalize_sale(cart, cart_list, sales_list):
    if cart:
        total_price = sum(item[3] for item in cart)
        sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            conn = connect_db()
            cursor = conn.cursor()

            for item in cart:
                cursor.execute("SELECT cantidad FROM libros WHERE id = ?", (item[0],))
                stock = cursor.fetchone()
                if stock is None or stock[0] < item[2]:  # sin suficiente stock
                    messagebox.showwarning("Cantidad Insuficiente", f"No hay suficiente stock del libro {item[1]}.")
                    conn.close()
                    return
            
            cursor.execute("INSERT INTO ventas (precio_total, fecha) VALUES (?, ?)", (total_price, sale_date))
            sale_id = cursor.lastrowid

            for item in cart:
                cursor.execute("INSERT INTO venta_detalle (venta_id, libro_id, cantidad, precio_unitario) VALUES (?, ?, ?, ?)", (sale_id, item[0], item[2], item[3]))
                # Actualizacion de stock
                cursor.execute("UPDATE libros SET cantidad = cantidad - ? WHERE id = ?", (item[2], item[0]))

            conn.commit()
            conn.close()

            messagebox.showinfo("Venta Completada", f"Venta registrada exitosamente con un total de: ${total_price:.2f}")
            cart.clear()
            update_cart_list(cart_list, cart)
            update_sales_list(sales_list)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo completar la venta: {e}")
    else:
        messagebox.showwarning("Carrito Vacío", "Por favor agregue artículos al carrito antes de finalizar la venta.")

def update_book_list(book_list):
    book_list.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, precio FROM libros")
    books = cursor.fetchall()
    conn.close()
    for book in books:
        book_list.insert(tk.END, f"{book[0]} - {book[1]} - {book[2]}")

def update_cart_list(cart_list, cart):
    cart_list.delete(0, tk.END)
    for item in cart:
        cart_list.insert(tk.END, f"{item[1]} - Cantidad: {item[2]}, Subtotal: ${item[3]:.2f}")

def update_sales_list(sales_list):
    sales_list.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT ventas.id, ventas.precio_total, ventas.fecha FROM ventas''')
    sales = cursor.fetchall()
    conn.close()
    for sale in sales:
        sales_list.insert(tk.END, f"Venta ID: {sale[0]}, Total: ${sale[1]:.2f}, Fecha: {sale[2]}")

def open_sales_crud(root, open_main_window):
    root.destroy()
    sales_window = tk.Toplevel()

    ancho_ventana = 600
    alto_ventana = 700
    x_ventana = sales_window.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = sales_window.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    sales_window.geometry(posicion)
    
    sales_window.title("Gestión de Ventas")
    # sales_window.geometry("600x700")

    tk.Label(sales_window, text="Seleccione un Libro:").pack(pady=5)
    book_list = tk.Listbox(sales_window, width=60, height=5)
    book_list.pack(pady=10)
    update_book_list(book_list)

    tk.Label(sales_window, text="Cantidad para Agregar:").pack(pady=5)
    quantity_entry = tk.Entry(sales_window, width=8)
    quantity_entry.pack(pady=5)

    tk.Button(sales_window, text="Agregar al Carrito", command=lambda: add_to_cart(book_list, quantity_entry, cart_list, cart)).pack(pady=5)

    cart = []  # Lista de libro seleccionados para la venta
    tk.Label(sales_window, text="Carrito:").pack(pady=10)
    cart_list = tk.Listbox(sales_window, width=60, height=5)
    cart_list.pack(pady=10)

    tk.Button(sales_window, text="Finalizar Venta", command=lambda: finalize_sale(cart, cart_list, sales_list)).pack(pady=10)

    tk.Label(sales_window, text="Registro de Ventas:").pack(pady=10)
    sales_list = tk.Listbox(sales_window, width=60, height=5)
    sales_list.pack(pady=10)
    update_sales_list(sales_list)

    tk.Button(sales_window, text="Volver", command=lambda: go_back(sales_window, open_main_window)).pack(pady=10)

def go_back(current_window, open_main_window):
    current_window.destroy()
    open_main_window()