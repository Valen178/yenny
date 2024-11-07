import tkinter as tk
from LibroVentana import open_book_crud
from CategoriaVentana import open_category_crud
from VentaVentana import open_sales_crud

def open_main_window():
    root = tk.Tk()
    ancho_ventana = 400
    alto_ventana = 300
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.title("Yenny")
    #root.geometry("400x300")

    main_label = tk.Label(root, text="Yenny", font=("Helvetica", 16))
    main_label.pack(pady=20)

    btn_libros = tk.Button(root, text="Libros", width=20, command=lambda: open_book_crud(root, open_main_window))
    btn_libros.pack(pady=5)

    btn_categorias = tk.Button(root, text="Categorias", width=20, command=lambda: open_category_crud(root, open_main_window))
    btn_categorias.pack(pady=5)

    btn_ventas = tk.Button(root, text="Ventas", width=20, command=lambda: open_sales_crud(root, open_main_window))
    btn_ventas.pack(pady=5)

    btn_informes = tk.Button(root, text="Informes", width=20)
    btn_informes.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    open_main_window()