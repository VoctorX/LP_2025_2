import tkinter as tk
#Crear ventana principal
root=tk.Tk()
root.title("Mi primera calculadora")
root.geometry("300x200")
#Crear una etiqueta de texto
label=tk.Label(root, text="Hola TKinter", font=("Arial", 16))
label.pack(pady=20)

#Crear Boton
button = tk.Button(root, text="CERRAR", command=root.destroy)
button.pack(pady=10)
#Iniciar el bucle principal
root.mainloop()