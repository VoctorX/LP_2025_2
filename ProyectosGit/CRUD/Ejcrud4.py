import tkinter as tk
from tkinter import ttk, messagebox
import os
 
class HojaVidaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hoja de Vida Interactiva")
        self.root.geometry("800x600")
       
        # Datos almacenados
        self.datos_personales = {}
        self.experiencia = []
        self.educacion = []
 
        # Crear menú
        self.crear_menu()
       
        # Crear frames principales
        self.crear_frames()
 
    def crear_menu(self):
        """Crear el menú de la aplicación."""
        menubar = tk.Menu(self.root)
 
        # Menú Archivo
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        archivo_menu.add_command(label="Guardar", command=self.guardar)
        archivo_menu.add_command(label="Exportar PDF", command=self.exportar_pdf)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
 
        # Menú Editar
        editar_menu = tk.Menu(menubar, tearoff=0)
        editar_menu.add_command(label="Añadir Experiencia", command=self.add_experiencia)
        editar_menu.add_command(label="Añadir Educación", command=self.add_educacion)
        menubar.add_cascade(label="Editar", menu=editar_menu)
 
        self.root.config(menu=menubar)
 
    def crear_frames(self):
        """Crear los frames donde se mostrarán los datos."""
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
       
        # Frame para información personal
        self.frame_personal = tk.Frame(self.main_frame, bg="#e3f2fd")
        self.frame_personal.pack(fill=tk.BOTH, expand=True)
       
        # Frame para experiencia
        self.frame_experiencia = tk.Frame(self.main_frame, bg="#e8f5e9")
        self.frame_experiencia.pack(fill=tk.BOTH, expand=True)
       
        # Frame para educación
        self.frame_educacion = tk.Frame(self.main_frame, bg="#fff3e0")
        self.frame_educacion.pack(fill=tk.BOTH, expand=True)
 
        # Inicialmente ocultamos los frames de experiencia y educación
        self.frame_experiencia.pack_forget()
        self.frame_educacion.pack_forget()
 
        # Añadir widgets a cada frame
        self.crear_widgets_personal()
        self.crear_widgets_experiencia()
        self.crear_widgets_educacion()
 
    def crear_widgets_personal(self):
        """Crear widgets para ingresar la información personal."""
        tk.Label(self.frame_personal, text="Nombre", font=("Arial", 14)).pack(pady=5)
        self.entry_nombre = tk.Entry(self.frame_personal, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)
       
        tk.Label(self.frame_personal, text="Edad", font=("Arial", 14)).pack(pady=5)
        self.entry_edad = tk.Entry(self.frame_personal, font=("Arial", 12))
        self.entry_edad.pack(pady=5)
 
        # Más campos de información personal pueden ser agregados aquí
 
    def crear_widgets_experiencia(self):
        """Crear widgets para ingresar la experiencia laboral."""
        tk.Label(self.frame_experiencia, text="Empresa", font=("Arial", 14)).pack(pady=5)
        self.entry_empresa = tk.Entry(self.frame_experiencia, font=("Arial", 12))
        self.entry_empresa.pack(pady=5)
       
        tk.Label(self.frame_experiencia, text="Cargo", font=("Arial", 14)).pack(pady=5)
        self.entry_cargo = tk.Entry(self.frame_experiencia, font=("Arial", 12))
        self.entry_cargo.pack(pady=5)
 
        # Más campos de experiencia laboral pueden ser agregados aquí
 
    def crear_widgets_educacion(self):
        """Crear widgets para ingresar la educación."""
        tk.Label(self.frame_educacion, text="Institución", font=("Arial", 14)).pack(pady=5)
        self.entry_institucion = tk.Entry(self.frame_educacion, font=("Arial", 12))
        self.entry_institucion.pack(pady=5)
       
        tk.Label(self.frame_educacion, text="Carrera", font=("Arial", 14)).pack(pady=5)
        self.entry_carrera = tk.Entry(self.frame_educacion, font=("Arial", 12))
        self.entry_carrera.pack(pady=5)
 
        # Más campos educativos pueden ser agregados aquí
 
    def nuevo(self):
        """Limpiar los campos para crear un nuevo registro."""
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_empresa.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_institucion.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)
 
        # Ocultar experiencia y educación hasta que se añadan
        self.frame_experiencia.pack_forget()
        self.frame_educacion.pack_forget()
 
    def guardar(self):
        """Guardar la información de la hoja de vida."""
        self.datos_personales['nombre'] = self.entry_nombre.get()
        self.datos_personales['edad'] = self.entry_edad.get()
 
        experiencia = {
            'empresa': self.entry_empresa.get(),
            'cargo': self.entry_cargo.get()
        }
        self.experiencia.append(experiencia)
 
        educacion = {
            'institucion': self.entry_institucion.get(),
            'carrera': self.entry_carrera.get()
        }
        self.educacion.append(educacion)
 
        messagebox.showinfo("Guardado", "Datos guardados correctamente.")
 
    def exportar_pdf(self):
        """Exportar los datos a un archivo PDF (por implementar)."""
        messagebox.showinfo("Exportar", "Función de exportación a PDF no implementada.")
 
    def add_experiencia(self):
        """Mostrar el frame de experiencia laboral."""
        self.frame_personal.pack_forget()
        self.frame_experiencia.pack(fill=tk.BOTH, expand=True)
 
    def add_educacion(self):
        """Mostrar el frame de educación."""
        self.frame_experiencia.pack_forget()
        self.frame_educacion.pack(fill=tk.BOTH, expand=True)
    
    
# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = HojaVidaApp(root)
    root.mainloop()





    