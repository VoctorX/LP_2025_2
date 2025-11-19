# main.py

# Importamos la clase desde el módulo 'nombre_proyecto' dentro de 'src'
# Si renombras 'nombre_proyecto' a 'gestor', aquí sería 'from src.gestor import GestorDeProductos'
from src.productos import GestorDeProductos 

def ejecutar_ejemplo():
    """
    Función principal que demuestra el uso de la clase GestorDeProductos
    con operaciones CRUD.
    """
    print("--- 🚀 INICIANDO DEMOSTRACIÓN DEL CRUD ---")

    # 1. Inicializar el gestor
    gestor = GestorDeProductos()
    print("-" * 30)

    # 2. Operación C: Crear productos
    print("CREANDO PRODUCTOS...")
    id_monitor = gestor.crear_producto("Monitor 27p", 299.99, 10)
    id_teclado = gestor.crear_producto("Teclado Mecánico", 85.50, 25)
    print("-" * 30)

    # 3. Operación R: Leer (obtener todos)
    print("📋 LISTA INICIAL DE PRODUCTOS:")
    productos = gestor.obtener_productos()
    for p in productos:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]:.2f}, Stock: {p[3]}")
    print("-" * 30)

    # 4. Operación U: Actualizar
    print(f"ACTUALIZANDO Monitor (ID: {id_monitor})...")
    if id_monitor:
        if gestor.actualizar_producto(id_monitor, precio=289.99, stock=8):
             print(f"🔄 Producto con ID {id_monitor} actualizado con éxito.")

    print("-" * 30)

    # 5. Operación D: Eliminar
    print(f"ELIMINANDO Teclado (ID: {id_teclado})...")
    if id_teclado:
        if gestor.eliminar_producto(id_teclado):
            print(f"🗑️ Producto con ID {id_teclado} eliminado con éxito.")
    print("-" * 30)

    # 6. Lectura final
    print("📋 LISTA FINAL DE PRODUCTOS:")
    productos = gestor.obtener_productos()
    for p in productos:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]:.2f}, Stock: {p[3]}")
    
    # 7. Cerrar la conexión
    gestor.cerrar_conexion()
    print("--- ✅ DEMOSTRACIÓN FINALIZADA ---")

if __name__ == "__main__":
    ejecutar_ejemplo()