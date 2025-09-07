import tkinter as tk
from tkinter import messagebox

# ----- Configuracion del Icono ----
Ruta_del_Logo="ICOcalculadora.ico"
#----- Funciones de la calculadora----

def sumar():
    """
    Obtiene los valores de los campos de entrada, realiza la suma y muestra el resultado
    """
    try:
        #Obtiene los valores de los campos de entrada
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        # Realiza la suma
        resultado=num1 + num2

        #actualizar la etiqueta de  resultado
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

        #Muestra un mensaje
        messagebox.showinfo("Resultado", f"La suma es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")

def restar():
    """
    Obtiene los valores de los campos de entrada, realiza la resta y muestra el resultado
    """
    try:
        #Obtiene los valores de los campos de entrada
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        # Realiza la resta
        resultado=num1 - num2

        #actualizar la etiqueta de  resultado
        etiqueta_resultado.config(text=f"Resultado de la resta es: {resultado}")

        #Muestra un mensaje
        messagebox.showinfo("Resultado", f"La resta es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")

def multi():
    """
    Obtiene los valores de los campos de entrada, realiza la multiplicacion y muestra el resultado
    """
    try:
        #Obtiene los valores de los campos de entrada
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        # Realiza la multiplicacion
        resultado=num1 * num2

        #actualizar la etiqueta de  resultado
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

        #Muestra un mensaje
        messagebox.showinfo("Resultado", f"La multiplicacion es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")

def divi():
    """
    Obtiene los valores de los campos de entrada, realiza la division y muestra el resultado
    """
    try:
        #Obtiene los valores de los campos de entrada
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        # Realiza la division
        if num2==0:
            messagebox.showerror("Error", "No se puede dividir entre cero, intenta con otro numero")
            return
        else:
            resultado=num1 / num2

        #actualizar la etiqueta de  resultado
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

        #Muestra un mensaje
        messagebox.showinfo("Resultado", f"La division es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")        

def potencia():
    """
    Obtiene los valores de los campos de entrada, realiza la potencia y muestra el resultado
    """
    try:
        #Obtiene los valores de los campos de entrada
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        # Realiza la potencia
        resultado=num1 ** num2

        #actualizar la etiqueta de  resultado
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

        #Muestra un mensaje
        messagebox.showinfo("Resultado", f"La potencia es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")

#-----Configuracion de la Interfaz grafica --- 

#----Crear la ventana principal ----

ventana=tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("400x200")

#----Configurar el icono de la ventana----
try:
    ventana.iconbitmap(Ruta_del_Logo)
except tk.TclError:
    #Manejar el error si el archivo del icno no se maneja
    print(f"No se pudo cargar el icono desde la ruta: {Ruta_del_Logo}")

#Crear y colocar los widgets(elementos visuales)
etiqueta_instruccion=tk.Label(
    ventana, text="Ingrese dos numeros para sumar o restar: ")
etiqueta_instruccion.pack(pady=10)

etiqueta_num1=tk.Label(ventana, text="Numero 1: ")
etiqueta_num1.pack()
entry_num1=tk.Entry(ventana)
entry_num1.pack()

etiqueta_num2=tk.Label(ventana, text="Numero 2: ")
etiqueta_num2.pack()
entry_num2=tk.Entry(ventana)
entry_num2.pack()

#Crear un marco para agrupar los botones
frame_botones=tk.Frame(ventana)
frame_botones.pack(pady=10)

#Crear y colocar los botones
botton_sumar=tk.Button(frame_botones, text="Sumar", command=sumar)
botton_sumar.pack(side=tk.LEFT, padx=5)

botton_restar=tk.Button(frame_botones, text="Restar", command=restar)
botton_restar.pack(side=tk.LEFT, padx=5)

botton_multi=tk.Button(frame_botones, text="Multiplicar", command=multi)
botton_multi.pack(side=tk.LEFT, padx=5)

botton_divi=tk.Button(frame_botones, text="Division", command=divi)
botton_divi.pack(side=tk.LEFT, padx=5)

botton_potencia=tk.Button(frame_botones, text="Potencia", command=potencia)
botton_potencia.pack(side=tk.LEFT, padx=5)

#Crea una etiqueta para mostrar el resultado
etiqueta_resultado=tk.Label(ventana, text="El resultado es: ")
etiqueta_resultado.pack(pady=10)

#Iniciar bucle Principal de la ventana
ventana.mainloop()