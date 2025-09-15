import tkinter as tk
from tkinter import messagebox

# --------------------------
# Funciones de la aplicación
# --------------------------

def agregar_dato():
    """Agrega el texto del campo de entrada a la lista."""
    dato = entrada.get().strip()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor ingrese un dato antes de agregar.")

def limpiar_datos():
    """Limpia la lista y el campo de entrada."""
    lista_datos.delete(0, tk.END)
    entrada.delete(0, tk.END)

# --------------------------
# Configuración de la ventana
# --------------------------

ventana = tk.Tk()
ventana.title("Registro de Datos - GUI Básica")
ventana.geometry("400x350")
ventana.resizable(False, False)

# --------------------------
# Componentes de la interfaz
# --------------------------

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(ventana, width=40, font=("Arial", 11))
entrada.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", width=15, command=agregar_dato, bg="#4CAF50", fg="white")
boton_agregar.pack(pady=5)

# Etiqueta para la lista
etiqueta_lista = tk.Label(ventana, text="Lista de datos ingresados:", font=("Arial", 12))
etiqueta_lista.pack(pady=10)

# Listbox para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10, font=("Arial", 10))
lista_datos.pack(pady=5)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", width=15, command=limpiar_datos, bg="#f44336", fg="white")
boton_limpiar.pack(pady=10)

# --------------------------
# Ejecutar la aplicación
# --------------------------

ventana.mainloop()