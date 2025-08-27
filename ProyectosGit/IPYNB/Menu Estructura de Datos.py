# -*- coding: utf-8  -*-
""""
===============================================================
|                 Estructura de datos(Ed) simple - Menu                   |
===============================================================

Este programa es un menu de estructuras de datos donde se da un ejemplo

Autor: Victor Cordoba
Fecha: 2025-08-13

"""

# Crear un bucle infinito para mostrar el menu hasta que el usuario decida salir
while True:

    print("\n==Mostrar Menu==")
    print("1.Ejemplo de listas con aplicacion en notas")
    print("2.Ejemplo de duplas con la misma logica de notas")
    print("3.Ejemplo de diccionario con la misma logica de notas")
    print("4.Ejemplo de conjuntos con la misma logica de notas")
    print("5.Salir")

    # Solicitar al usuario que elija u8na opcion del menu
    op=input("Selecciones una de las opciones (1-5): ")

    # ====OPeraciones====
    notas = []

    if op == "1": # Ejemplo con listas
        print("\nEjemplo con Listas")
        n=int(input("¿Cuantas notas desea registrar?: "))
        for i in range(n):
            valor=float(input(f"Ingrese el monto de las nota {i+1}: "))
            notas.append(valor)

        print("Notas: ", notas)
        print("Promedio: ", sum(notas) / len(notas))
        input("\nPresione Enter para continuar... ")
    
    elif op == "2": # Ejemplo con tuplas
        print("\nEjemplo con Tuplas")
        notas = (8, 7, 9, 10)
        print("Notas:", notas)
        print("Promedio:", sum(notas) / len(notas))
        input("\nPresione Enter para continuar... ")
    
    elif op == "3":
        # Ejemplo con diccionarios
        print("\nEjemplo con Diccionarios")
        notas = {"Estudiante 1": 8, "Estudiante 2": 7, "Estudiante 3": 9, "Estudiante 4": 10}
        print("Notas:", notas)
        promedio = sum(notas.values()) / len(notas)
        print("Promedio:", promedio)
        input("\nPresione Enter para continuar... ")
    
    elif op == "4":
        # Ejemplo con conjuntos
        print("\nEjemplo con Conjuntos")
        notas = {8, 7, 9, 10}
        print("Notas:", notas)
        print("Promedio:", sum(notas) / len(notas))
        input("\nPresione Enter para continuar... ")
    
    elif op == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")
    
    
    #Se agrega una pausa para que el usuario pueda ver el resuldado antes de continuar
        input("\nPresione Enter para continuar... ")