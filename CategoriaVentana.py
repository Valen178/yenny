import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

def connect_db():
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS categoria (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL UNIQUE
                    )''')
    conn.commit()
    return conn

def add_category(name_entry, category_list):
    name = name_entry.get()
    if name:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categoria (nombre) VALUES (?)", (name,))
            conn.commit()
            conn.close()
            update_category_list(category_list)
            name_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar categoria: {e}")
    else:
        messagebox.showwarning("Error en el ingreso", "El nombre de la categoria es obligatorio,")

def delete_category(category_list):
    selected = category_list.curselection()
    if selected:
        index = selected[0]
        category_id = category_list.get(index).split(" - ")[0]
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categoria WHERE id = ?", (category_id,))
            conn.commit()
            conn.close()
            update_category_list(category_list)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la categoria: {e}")
    else:
        messagebox.showwarning("Error de selección", "Por favor elija una categoria.")

def update_category(category_list):
    selected = category_list.curselection()
    if selected:
        index = selected[0]
        category_id = category_list.get(index).split(" - ")[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM categoria WHERE id = ?", (category_id,))
        category = cursor.fetchone()
        conn.close()
        
        if category:
            new_name = simpledialog.askstring("Actualizar categoria", "Ingrese el nuevo nombre", initialvalue=category[0])
            
            if new_name:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE categoria SET nombre = ? WHERE id = ?", (new_name, category_id))
                    conn.commit()
                    conn.close()
                    update_category_list(category_list)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo actualizar la categoria: {e}")
            else:
                messagebox.showwarning("Error en el ingreso", "El nombre de la categoria es obligatorio.")
    else:
        messagebox.showwarning("Error de selección", "Por favor elija una categoria.")

def update_category_list(category_list):
    category_list.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM categoria")
    categories = cursor.fetchall()
    conn.close()
    for category in categories:
        category_list.insert(tk.END, f"{category[0]} - {category[1]}")

def open_category_crud(root, open_main_window):
    root.destroy()
    category_window = tk.Toplevel()
    ancho_ventana = 600
    alto_ventana = 500
    x_ventana = category_window.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = category_window.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    category_window.geometry(posicion)
    category_window.title("Gestión de categorias")
    category_window.configure(bg="#f8f8f8")
    # category_window.geometry("400x400")

    tk.Label(category_window, text="Nombre de categoria:", font=("Arial", 14), bg="#f8f8f8").pack(pady=10)
    name_entry = tk.Entry(category_window, width=30, font=("Arial", 14), bg="#e5e5e5", relief="sunken")
    name_entry.pack(pady=5)

    tk.Button(category_window, text="Agregar categoria", width=18, command=lambda: add_category(name_entry, category_list), bg="#d3d3d3", font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)

    category_list = tk.Listbox(category_window, width=40, height=10)
    category_list.pack(pady=10)

    tk.Button(category_window, text="Actualizar categoria seleccionada", command=lambda: update_category(category_list), bg="#d3d3d3",  font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)
    tk.Button(category_window, text="Eliminar categoria seleccionada", command=lambda: delete_category(category_list), bg="#d3d3d3",  font=("Arial", 12),activebackground= "#b5b5b5").pack(pady=5)

    update_category_list(category_list)

    tk.Button(category_window, text="VOLVER",width=10, command=lambda: go_back(category_window, open_main_window), bg="#84001c", fg="#F8F8F8", font=("Arial", 10,"bold"),activebackground= "#6c0017",activeforeground="#eeeeee").pack(pady=10)

def go_back(current_window, open_main_window):
    current_window.destroy()
    open_main_window()