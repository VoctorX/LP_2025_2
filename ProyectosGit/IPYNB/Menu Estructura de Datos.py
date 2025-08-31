# -*- coding: utf-8  -*-
""""
===============================================================
|                 Estructura de datos(Ed) simple - Menu                   |
===============================================================

Este programa es un menu de estructuras de datos con una logica de datos

Autor: Victor Cordoba
Fecha: 2025-08-31

"""

# Crear un bucle infinito para mostrar el menu hasta que el usuario decida salir
while True:

    print("\n==Mostrar Menu==")
    print("1.Ejemplo de listas con aplicacion en notas")
    print("2.Ejemplo de tuplas con la misma logica de notas")
    print("3.Ejemplo de diccionario con la misma logica de notas")
    print("4.Ejemplo de conjuntos con la misma logica de notas")
    print("5.Salir")

    # Solicitar al usuario que elija u8na opcion del menu
    op=input("Selecciones una de las opciones (1-5): ")

    # ====OPeraciones====
    notas = []

    if op == "1": # Ejemplo con listas
        n=int(input("¿Cuantas notas desea registrar?: "))
        for i in range(n):
            valor=float(input(f"Ingrese el monto de la nota {i+1}: "))
            notas.append(valor)

        print("\nNotas: ", notas)
        print("Promedio: ", sum(notas) / len(notas))
        input("\nPresione Enter para continuar... ")
    
    elif op == "2": # Ejemplo con tuplas
        notas = (3.8, 5, 4.6, 4.3)
        print("Notas:", notas)
        input("\nPresione Enter para continuar... ")
        print("1. Promedio \n2. Mayor nota \n3. Menor Nota")
        tup=int(input("¿Que deseas hacer con dichas nochas?: "))
        if tup==1:
            print(f"Promedio: {sum(notas) / len(notas)}")
        elif tup==2:
            print(f"Mayor Nota: {max(notas)}")
        elif tup==3:
            print(f"Menor Nota: {min(notas)}")
        input("\nPresione Enter para continuar... ")
    
    elif op == "3": # Ejemplo con diccionarios
        estudiantes = {"Victor": [4, 5], "Sara": [3.5, 4], "Sofia": [4.5, 4.2], "Andres": [2.4, 3.8] }
        print("Notas de Estudiantes:", estudiantes)
        input("\nPresione Enter para continuar... ")
        print("1. Promedio de todos los estudiantes \n2. Promedio de un estudiante en especifico")
        dic=int(input("¿Que deseas hacer con dichas nochas?: "))
        if dic==1:
            for estudiante, notas in estudiantes.items():
                promedio = sum(notas) / len(notas)
                print(f"{estudiante}: {promedio:.2f}")
        elif dic==2:
            nombre = input("Ingresa el nombre del estudiante: ")
            if nombre in estudiantes:
                notas = estudiantes[nombre]
                promedio = sum(notas) / len(notas)
                print(f"{nombre} tiene un promedio de {promedio:.2f}")
        input("\nPresione Enter para continuar... ")
    
    elif op == "4":  # Ejemplo con conjuntos
        notas = set()
        cantidad= int(input("¿Cuántas notas desea registrar?: "))
        for i in range(n):
            valor = float(input(f"Ingrese la nota {i+1}: "))
            notas.add(valor)  
        
        print("\nNotas únicas:", notas)
        
        print("\n1. Promedio \n2. Mayor nota \n3. Menor nota")
        op_set = int(input("¿Qué deseas hacer con las notas?: "))
        
        if op_set == 1:
            print(f"Promedio: {sum(notas)/len(notas):.2f}")
        elif op_set == 2:
            print(f"Mayor nota: {max(notas)}")
        elif op_set == 3:
            print(f"Menor nota: {min(notas)}")
        else:
            print("Opción no válida")
        input("\nPresione Enter para continuar...")

    elif op == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")
    
    
    #Se agrega una pausa para que el usuario pueda ver el resuldado antes de continuar
        input("\nPresione Enter para continuar... ")