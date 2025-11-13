from crud.operations import crear, leer, actualizar, eliminar

def menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Crear contacto")
    print("2. Lista de contactos")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    while True:
        menu()
        option = input("Selecciona una opción: ")
        if option == "1":
            cid = input("ID: ")
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            crear(cid, name, phone)
            print("Contacto creado!")
        elif option == "2":
            contacts = leer()
            for c in contacts:
                print(c)
        elif option == "3":
            cid = input("ID del contacto a actualizar: ")
            name = input("Nuevo nombre (dejar vacío si no cambia): ")
            phone = input("Nuevo teléfono (dejar vacío si no cambia): ")
            if actualizar(cid, name or None, phone or None):
                print("Contacto actualizado.")
            else:
                print("Contacto no encontrado.")
        elif option == "4":
            cid = input("ID del contacto a eliminar: ")
            if eliminar(cid):
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif option == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()