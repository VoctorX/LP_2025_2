import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("CRUD Hoja de Vida")
root.geometry("800x600")

# Frame para contener widgets
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Configurar evento
def guardar_datos():
    print("Guardando información...")

# Botón con comando asociado
btn_guardar = tk.Button(frame, text="Guardar", 
                        command=guardar_datos)
btn_guardar.pack(pady=10)

# Iniciar aplicación
root.mainloop()
