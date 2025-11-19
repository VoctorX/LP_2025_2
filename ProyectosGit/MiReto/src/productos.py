# src/productos.py

import sqlite3

class GestorDeProductos:
    """
    Gestiona la conexión a la base de datos SQLite y las operaciones CRUD 
    (Crear, Leer, Actualizar, Borrar) para la tabla de productos.
    """
    def __init__(self, db_name='productos.db'):
        """
        Inicializa el gestor, establece la conexión y asegura que la tabla exista.
        """
        self.db_name = db_name
        self.conexion = None
        self.cursor = None
        self._conectar()
        self._crear_tabla()

    def _conectar(self):
        """Establece la conexión a la base de datos SQLite."""
        try:
            self.conexion = sqlite3.connect(self.db_name)
            self.cursor = self.conexion.cursor()
            # print(f"Conexión a la base de datos '{self.db_name}' establecida.")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def _crear_tabla(self):
        """Crea la tabla 'productos' si no existe."""
        query = """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """
        try:
            self.cursor.execute(query)
            self.conexion.commit()
            # print("Tabla 'productos' verificada/creada.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    # --- Funciones CRUD ---

    def crear_producto(self, nombre, precio, stock):
        """Inserta un nuevo producto en la base de datos."""
        query = "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)"
        try:
            self.cursor.execute(query, (nombre, precio, stock))
            self.conexion.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"❌ Error al crear producto: {e}")
            return None

    def obtener_productos(self):
        """Recupera todos los productos de la base de datos."""
        query = "SELECT id, nombre, precio, stock FROM productos"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener productos: {e}")
            return []

    def obtener_producto_por_id(self, producto_id):
        """Recupera un solo producto por su ID."""
        query = "SELECT id, nombre, precio, stock FROM productos WHERE id = ?"
        try:
            self.cursor.execute(query, (producto_id,))
            return self.cursor.fetchone()  # Usar fetchone() para un solo resultado
        except sqlite3.Error as e:
            print(f"❌ Error al obtener producto por ID: {e}")
            return None

    def actualizar_producto(self, producto_id, nombre=None, precio=None, stock=None):
        """Actualiza el nombre, precio o stock de un producto por su ID."""
        campos_a_actualizar = []
        valores = []

        if nombre is not None:
            campos_a_actualizar.append("nombre = ?")
            valores.append(nombre)
        if precio is not None:
            campos_a_actualizar.append("precio = ?")
            valores.append(precio)
        if stock is not None:
            campos_a_actualizar.append("stock = ?")
            valores.append(stock)

        if not campos_a_actualizar:
            # print("⚠️ No se proporcionaron campos para actualizar.") # Se evita el print en la lógica central
            return False

        query = f"UPDATE productos SET {', '.join(campos_a_actualizar)} WHERE id = ?"
        valores.append(producto_id)

        try:
            self.cursor.execute(query, tuple(valores))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar producto: {e}")
            return False

    def eliminar_producto(self, producto_id):
        """Elimina un producto de la base de datos por su ID."""
        query = "DELETE FROM productos WHERE id = ?"
        try:
            self.cursor.execute(query, (producto_id,))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar producto: {e}")
            return False

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion:
            self.conexion.close()
            # print(f"Conexión a '{self.db_name}' cerrada.")