import tkinter as tk
from tkinter import messagebox

# Diccionario de usuarios y contraseñas
usuarios = {"Victor": "1234", "Ana": "abcd"}

def login():
    user = entry_user.get()
    clave = entry_pass.get()
    if user in usuarios and usuarios[user] == clave:
        messagebox.showinfo("Login", "¡Acceso permitido!")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x150")

# Usuario
tk.Label(ventana, text="Usuario:").pack()
entry_user = tk.Entry(ventana)
entry_user.pack()

# Contraseña
tk.Label(ventana, text="Contraseña:").pack()
entry_pass = tk.Entry(ventana, show="*")
entry_pass.pack()

# Botón login
tk.Button(ventana, text="Ingresar", command=login).pack(pady=10)

ventana.mainloop()
