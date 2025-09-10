import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF
import os
import webbrowser


class HojaDeVidaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hoja de Vida Interactiva")
        self.root.geometry("800x600")

        # Diccionarios y listas para almacenar datos
        self.datos_personales = {}
        self.experiencia = []
        self.educacion = []

        # Crear interfaz principal
        self.crear_menu()
        self.crear_frames()

    # ============================
    # MENÚ PRINCIPAL
    # ============================
    def crear_menu(self):
        menubar = tk.Menu(self.root)

        # Menú Archivo
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        archivo_menu.add_command(label="Guardar", command=self.guardar)
        archivo_menu.add_command(label="Exportar PDF",
                                 command=self.exportar_pdf)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Menú Editar
        editar_menu = tk.Menu(menubar, tearoff=0)
        editar_menu.add_command(
            label="Añadir Experiencia", command=self.add_experiencia)
        editar_menu.add_command(label="Añadir Educación",
                                command=self.add_educacion)
        editar_menu.add_command(
            label="Editar Información", command=self.editar)
        menubar.add_cascade(label="Editar", menu=editar_menu)

        self.root.config(menu=menubar)

    # ============================
    # FRAMES PRINCIPALES
    # ============================
    def crear_frames(self):
        self.main_frame = tk.Frame(self.root, bg="#eaeaea")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame: información personal
        self.frame_personal = tk.Frame(self.main_frame, bg="#f3f3df")
        self.frame_personal.pack(fill=tk.BOTH, expand=True)

        # Frame: experiencia
        self.frame_experiencia = tk.Frame(self.main_frame, bg="#e5f5e5")
        self.frame_experiencia.pack(fill=tk.BOTH, expand=True)
        self.frame_experiencia.pack_forget()

        # Frame: educación
        self.frame_educacion = tk.Frame(self.main_frame, bg="#dfe5f3")
        self.frame_educacion.pack(fill=tk.BOTH, expand=True)
        self.frame_educacion.pack_forget()

        # Añadir widgets
        self.crear_widgets_personal()
        self.crear_widgets_experiencia()
        self.crear_widgets_educacion()

    # ============================
    # WIDGETS DE SECCIONES
    # ============================
    def crear_widgets_personal(self):
        tk.Label(self.frame_personal, text="Información Personal",
                 font=("Arial", 14, "bold")).pack(pady=10)

        form = tk.Frame(self.frame_personal, bg="#f3f3df")
        form.pack(pady=10)

        tk.Label(form, text="Nombre:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre_entry = tk.Entry(form, width=30)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(form, text="Email:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = tk.Entry(form, width=30)
        self.email_entry.grid(row=1, column=1)

        tk.Label(form, text="Teléfono:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e")
        self.telefono_entry = tk.Entry(form, width=30)
        self.telefono_entry.grid(row=2, column=1)

        tk.Button(self.frame_personal, text="Guardar Información",
                  command=self.agregar_personal).pack(pady=10)
        tk.Button(self.frame_personal, text="Mostrar Información",
                  command=self.mostrar_personal).pack()

    def crear_widgets_experiencia(self):
        tk.Label(self.frame_experiencia, text="Experiencia Laboral",
                 font=("Arial", 14, "bold")).pack(pady=10)

        form = tk.Frame(self.frame_experiencia, bg="#e5f5e5")
        form.pack(pady=10)

        tk.Label(form, text="Cargo:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e")
        self.cargo_entry = tk.Entry(form, width=30)
        self.cargo_entry.grid(row=0, column=1)

        tk.Label(form, text="Empresa:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e")
        self.empresa_entry = tk.Entry(form, width=30)
        self.empresa_entry.grid(row=1, column=1)

        tk.Label(form, text="Año:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e")
        self.año_entry = tk.Entry(form, width=30)
        self.año_entry.grid(row=2, column=1)

        tk.Button(self.frame_experiencia, text="Guardar Experiencia",
                  command=self.add_experiencia).pack(pady=10)

    def crear_widgets_educacion(self):
        tk.Label(self.frame_educacion, text="Educación",
                 font=("Arial", 14, "bold")).pack(pady=10)

        form = tk.Frame(self.frame_educacion, bg="#dfe5f3")
        form.pack(pady=10)

        tk.Label(form, text="Título:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e")
        self.titulo_entry = tk.Entry(form, width=30)
        self.titulo_entry.grid(row=0, column=1)

        tk.Label(form, text="Institución:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e")
        self.institucion_entry = tk.Entry(form, width=30)
        self.institucion_entry.grid(row=1, column=1)

        tk.Label(form, text="Año:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e")
        self.año_educacion_entry = tk.Entry(form, width=30)
        self.año_educacion_entry.grid(row=2, column=1)

        tk.Button(self.frame_educacion, text="Guardar Educación",
                  command=self.add_educacion).pack(pady=10)

    # ============================
    # CRUD DE INFORMACIÓN PERSONAL
    # ============================
    def agregar_personal(self):
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if not nombre or not email or not telefono:
            messagebox.showwarning(
                "Advertencia", "Nombre, Email y Teléfono son obligatorios")
            return

        self.datos_personales = {"nombre": nombre,
                                 "email": email, "telefono": telefono}
        messagebox.showinfo("Éxito", "Datos guardados correctamente")

    def mostrar_personal(self):
        if self.datos_personales:
            info = (f"Nombre: {self.datos_personales['nombre']}\n"
                    f"Email: {self.datos_personales['email']}\n"
                    f"Teléfono: {self.datos_personales['telefono']}")
            messagebox.showinfo("Información Personal", info)
        else:
            messagebox.showwarning(
                "Información", "No hay datos personales guardados")

    def actualizar_personal(self):
        if not self.datos_personales:
            messagebox.showwarning(
                "Advertencia", "No hay datos para actualizar")
            return
        self.agregar_personal()

    # ============================
    # PDF EXPORT
    # ============================
    def exportar_pdf(self):
        if not self.datos_personales:
            messagebox.showwarning("Advertencia", "No hay datos para exportar")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Título
        pdf.cell(200, 10, txt="HOJA DE VIDA", ln=1, align="C")

        # Datos personales
        pdf.cell(200, 10, txt="INFORMACIÓN PERSONAL", ln=1, align="L")
        pdf.cell(
            200, 10, txt=f"Nombre: {self.datos_personales['nombre']}", ln=1, align="L")
        pdf.cell(
            200, 10, txt=f"Email: {self.datos_personales['email']}", ln=1, align="L")
        pdf.cell(
            200, 10, txt=f"Teléfono: {self.datos_personales['telefono']}", ln=1, align="L")

        archivo_pdf = "hoja_vida.pdf"
        pdf.output(archivo_pdf)

        webbrowser.open(archivo_pdf)
        messagebox.showinfo("Éxito", f"PDF generado: {archivo_pdf}")

    # ============================
    # OTRAS FUNCIONES
    # ============================
    def nuevo(self):
        self.datos_personales.clear()
        self.experiencia.clear()
        self.educacion.clear()
        self.nombre_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        messagebox.showinfo("Nuevo", "Formulario reiniciado")

    def guardar(self):
        messagebox.showinfo("Guardar", "La información ha sido guardada")

    def add_experiencia(self):
        self.mostrar_frame(self.frame_experiencia)

    def add_educacion(self):
        self.mostrar_frame(self.frame_educacion)

    def editar(self):
        self.actualizar_personal()

    def mostrar_frame(self, frame):
        self.frame_personal.pack_forget()
        self.frame_experiencia.pack_forget()
        self.frame_educacion.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)


# ============================
# MAIN
# ============================
if __name__ == "__main__":
    root = tk.Tk()
    app = HojaDeVidaApp(root)
    root.mainloop()
