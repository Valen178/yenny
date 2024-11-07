import tkinter as tk
from LibroVentana import open_book_crud
from CategoriaVentana import open_category_crud
from VentaVentana import open_sales_crud

def open_main_window():
    root = tk.Tk()
    ancho_ventana = 600
    alto_ventana = 400
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.title("Yenny")
    #root.geometry("400x300")
    root.configure(bg="#f8f8f8")

    main_label = tk.Label(root, text="Yenny", font=("Times New Roman", 35, "bold italic"), bg="#f8f8f8")
    main_label.pack(pady=20)

    btn_libros = tk.Button(root, text="Libros", width=25, command=lambda: open_book_crud(root, open_main_window), font=("Arial", 15), bg="#034033", fg="#F8F8F8",activebackground= "#022f25", activeforeground="#F8F8F8")
    btn_libros.pack(pady=5)

    btn_categorias = tk.Button(root, text="Categorias", width=25, command=lambda: open_category_crud(root, open_main_window), font=("Arial", 15), bg="#034033", fg="#F8F8F8",activebackground= "#022f25", activeforeground="#F8F8F8")
    btn_categorias.pack(pady=5)

    btn_ventas = tk.Button(root, text="Ventas", width=25, command=lambda: open_sales_crud(root, open_main_window), font=("Arial", 15), bg="#034033", fg="#F8F8F8",activebackground= "#022f25", activeforeground="#eeeeee")
    btn_ventas.pack(pady=5)

    btn_informes = tk.Button(root, text="Informes", width=25, font=("Arial", 15), bg="#034033", fg="#F8F8F8",activebackground= "#022f25", activeforeground="#eeeeee")
    btn_informes.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    open_main_window()