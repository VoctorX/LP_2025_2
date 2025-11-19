# test/test_productos.py

import unittest
# Importamos la clase a probar desde el paquete src
from src.productos import GestorDeProductos 
import os 
import sqlite3 

class TestGestorDeProductos(unittest.TestCase):
    """
    Clase que contiene las pruebas unitarias para la clase GestorDeProductos.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de CADA prueba. 
        Crea una instancia de GestorDeProductos usando una base de datos en memoria.
        Esto asegura que cada prueba se ejecute con una DB limpia.
        """
        # Usamos ':memory:' para una base de datos temporal en RAM
        print("\nSETUP: Creando GestorDeProductos con DB en memoria.")
        self.gestor = GestorDeProductos(db_name=':memory:')

    def tearDown(self):
        """
        Método que se ejecuta después de CADA prueba.
        Cierra la conexión a la base de datos en memoria.
        """
        print("TEARDOWN: Cerrando conexión.")
        self.gestor.cerrar_conexion()

    # --- Pruebas de CRUD Básicas ---

    def test_01_crear_producto_y_obtener(self):
        """Prueba la creación de un producto y su posterior lectura."""
        print("Ejecutando test_01_crear_producto_y_obtener...")
        
        # C: Crear
        nombre = "Laptop Pro"
        precio = 1200.00
        stock = 5
        
        producto_id = self.gestor.crear_producto(nombre, precio, stock)
        
        self.assertIsInstance(producto_id, int, "El ID retornado debe ser un entero.")
        self.assertTrue(producto_id > 0, "El ID debe ser positivo.")

        # R: Obtener y verificar
        productos = self.gestor.obtener_productos()
        self.assertEqual(len(productos), 1, "Debería haber exactamente 1 producto.")
        
        producto_encontrado = productos[0]
        self.assertEqual(producto_encontrado[1], nombre)
        self.assertEqual(producto_encontrado[2], precio)
        self.assertEqual(producto_encontrado[3], stock)

    def test_02_actualizar_producto(self):
        """Prueba la actualización de precio y stock de un producto existente."""
        print("Ejecutando test_02_actualizar_producto...")
        
        # 1. Preparación: Crear un producto
        initial_id = self.gestor.crear_producto("Tablet Pad", 450.00, 10)
        
        nuevo_precio = 399.99
        nuevo_stock = 3
        
        # U: Actualizar
        resultado = self.gestor.actualizar_producto(
            initial_id, 
            precio=nuevo_precio, 
            stock=nuevo_stock
        )
        
        self.assertTrue(resultado, "La actualización debe ser exitosa.")
        
        # R: Verificar la actualización
        productos = self.gestor.obtener_productos()
        producto_actualizado = productos[0]
        
        self.assertEqual(producto_actualizado[2], nuevo_precio, "El precio no se actualizó correctamente.")
        self.assertEqual(producto_actualizado[3], nuevo_stock, "El stock no se actualizó correctamente.")
        
        # Intentar actualizar un producto que no existe
        resultado_no_existente = self.gestor.actualizar_producto(9999, nombre="Fake")
        self.assertFalse(resultado_no_existente, "Actualizar ID inexistente debe fallar.")

    def test_03_eliminar_producto(self):
        """Prueba la eliminación de un producto."""
        print("Ejecutando test_03_eliminar_producto...")

        # 1. Preparación: Crear dos productos
        id_a_eliminar = self.gestor.crear_producto("Webcam HD", 50.00, 20)
        self.gestor.crear_producto("Micrófono USB", 75.00, 15)
        
        productos_iniciales = self.gestor.obtener_productos()
        self.assertEqual(len(productos_iniciales), 2, "Debería haber 2 productos inicialmente.")

        # D: Eliminar
        resultado = self.gestor.eliminar_producto(id_a_eliminar)
        
        self.assertTrue(resultado, "La eliminación debe ser exitosa.")

        # R: Verificar la eliminación
        productos_finales = self.gestor.obtener_productos()
        self.assertEqual(len(productos_finales), 1, "Debería quedar solo 1 producto.")
        
        # Verificar que el producto restante no sea el eliminado
        self.assertNotEqual(productos_finales[0][0], id_a_eliminar, "El ID eliminado sigue en la DB.")
        
        # Intentar eliminar un producto que no existe
        resultado_no_existente = self.gestor.eliminar_producto(9998)
        self.assertFalse(resultado_no_existente, "Eliminar ID inexistente debe fallar.")

    def test_04_manejo_de_datos_vacios(self):
        """Prueba la lectura de una tabla vacía."""
        print("Ejecutando test_04_manejo_de_datos_vacios...")
        
        productos = self.gestor.obtener_productos()
        self.assertIsInstance(productos, list)
        self.assertEqual(len(productos), 0, "La tabla debe estar vacía al inicio.")

    # --- Nuevas Pruebas ---

    def test_05_obtener_producto_por_id(self):
        """Prueba la obtención de un producto específico por su ID."""
        print("Ejecutando test_05_obtener_producto_por_id...")

        # 1. Preparación: Crear dos productos para asegurar el filtro
        id_a = self.gestor.crear_producto("Producto A", 10.0, 5)
        self.gestor.crear_producto("Producto B", 20.0, 10)

        # Obtener el primer producto
        producto_a = self.gestor.obtener_producto_por_id(id_a)
        
        self.assertIsNotNone(producto_a, "Debe encontrar el producto con el ID existente.")
        self.assertEqual(producto_a[0], id_a, "El ID debe coincidir.")
        self.assertEqual(producto_a[1], "Producto A", "El nombre debe coincidir.")
        
        # Probar ID no existente
        producto_z = self.gestor.obtener_producto_por_id(9999)
        self.assertIsNone(producto_z, "Debe retornar None para un ID inexistente.")


    def test_06_actualizar_sin_campos_a_cambiar(self):
        """Prueba llamar a actualizar_producto sin proporcionar nombre, precio ni stock."""
        print("Ejecutando test_06_actualizar_sin_campos_a_cambiar...")

        # 1. Preparación: Crear un producto
        initial_id = self.gestor.crear_producto("Dummy", 1.00, 1)
        
        # Llamar a la función sin pasar parámetros opcionales
        resultado = self.gestor.actualizar_producto(initial_id)
        
        # La función debe retornar False si no hay campos para actualizar
        self.assertFalse(resultado, "Debe fallar (retornar False) si no se pasan campos de actualización.")
        
        # Asegúrate de que los datos NO hayan cambiado
        producto = self.gestor.obtener_productos()[0]
        self.assertEqual(producto[2], 1.00, "El precio no debe haber sido modificado.")
        self.assertEqual(producto[3], 1, "El stock no debe haber sido modificado.")


# Esto permite que las pruebas se ejecuten cuando corres el archivo directamente
if __name__ == '__main__':
    unittest.main()