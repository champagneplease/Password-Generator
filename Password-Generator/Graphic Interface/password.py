
import string
import random
import tkinter as tk
from tkinter import messagebox


def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("La longitud debe ser mayor que 0")
        password = password_generator(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")


# Configurar la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")
root.geometry("400x200")

# Etiqueta y entrada para la longitud de la contraseña
tk.Label(root, text="Longitud de la contraseña:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Botón para generar contraseña
tk.Button(root, text="Generar", command=generate_password).pack(pady=10)

# Campo de salida para la contraseña
tk.Label(root, text="Contraseña generada:").pack(pady=5)
entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

# Iniciar la interfaz
tk.mainloop()
