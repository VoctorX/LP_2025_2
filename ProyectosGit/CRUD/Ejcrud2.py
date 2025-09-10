import tkinter as tk
#Crear ventana principal
root=tk.Tk()
root.title("Mi primera calculadora")
root.geometry("300x200")

#Crear un frame
frame=tk.Frame(root)
#Añadir
label=tk.Label(frame, text="Dentro del frame")
boton=tk.Button(frame, text="Boton")

# Posicionar los elementos dentro del frame
frame.grid(row=0, column=0, pady=10)

#Crear una etiqueta de texto
label=tk.Label(root, text="Hola TKinter", font=("Arial", 16, "bold"), fg="#A02B2B")
label.grid(row=1, column=0, pady=10)

#Crear Boton
button = tk.Button(root, text="CERRAR", command=root.destroy)
button.place(x=125, y=100)
#Iniciar el bucle principal
root.mainloop()