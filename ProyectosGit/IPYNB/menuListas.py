# -*- coding: utf-8  -*-
"""
===============================================================
|                 Listas Interactivas- Menu                   |
===============================================================

Este programa usa listas en Python y proporciona un menú interactivo para realizar operaciones básicas con listas, como agregar, eliminar y mostrar elementos.

Autor: Victor Cordoba
Fecha: 2025-08-27

"""
def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL - PRÁCTICA DE LISTAS =====") 
    print("1. Crear lista de ejemplo") #
    print("2. Mostrar lista actual") #
    print("3. Acceder a un elemento por índice") #
    print("4. Acceder a un rango de elementos") #
    print("5. Acceder con índice negativo") #
    print("6. Longitud de la lista (len)") #
    print("7. Buscar posición de un elemento (index)")#
    print("8. Insertar un elemento (insert)")
    print("9. Agregar un elemento al final (append)") #
    print("10. Extender lista con varios elementos (extend)") #
    print("11. Eliminar un elemento (remove)") #
    print("12. Contar ocurrencias de un elemento (count)") #
    print("13. Invertir lista (reverse)") #
    print("14. Ordenar lista (sort)") #
    print("15. Eliminar por índice y mostrar (pop)") #
    print("0. Salir")
    print("=============================================")

    return input("Seleccione una opción (0-15): ")

# Lista global inicial vacía
listas = {}
while True:
    op = mostrar_menu()

    #Opcion 1: Crear lista
    if op == '1':
        nombre = input("Ponle un nombre a tu lista (ejemplo: lista1, frutas, etc.): ")
        listas[nombre] = []   # crea lista vacía con ese nombre

        print(f"Ingresa los elementos para ' {nombre} ' (escribe 'fin' cuando hayas acabado):")
        while True:
            valor = input(": ")
            if valor.lower() == "fin":
                break
            listas[nombre].append(valor)
        input("\nPresione Enter para continuar... ")

    #Opcion 2: Mostrar lista
    elif op == "2":
        nombre=input("Pon el nombre de la lista que deseas buscar: ")
        if nombre in listas:
            print(f"Tu lista '{nombre}' es:", listas[nombre])
        else:
            print(f"La lista '{nombre}' no existe.")
        input("\nPresione Enter para continuar... ")

    #Opcion 3: Acceder a un elemento por índice
    elif op == "3":
        while True:
            nombre=input("Pon el nombre de la lista en la que deseas buscar un indice: ")
            if nombre in listas:
                index=int(input("Digita el indice que desea buscar: "))
                print(f"En el indice {index} esta el elemento '{listas[nombre][index]}' en la lista")
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")
                break   

    #Opcion 4: Acceder a un rango de elementos
    elif op == '4':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas ver un rango de elementos: ")
            if nombre in listas:
                inicio=int(input("Posicion inicial para el rango: "))
                fin=int(input("Posicion final para el rango: "))
                print(f"Elementos del rango {inicio} a {fin}: {listas[nombre][inicio:fin]}")
                input("\nPresione Enter para continuar... ")   
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 5: Acceder con índice negativo
    elif op == '5':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas acceder con indice negativo: ")
            if nombre in listas:
                indice=int(input("Pon el indice (negativo) al cual deseas acceder de dicha lista: "))
                print(f"El valor del indice {indice} es: {listas[nombre][indice]}")
                input("\nPresione Enter para continuar... ")   
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 6:  Longitud de la lista
    elif op == '6':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas ver la longitud: ")
            if nombre in listas:
                print(len(listas[nombre]))
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break
    
    #Opcion 7: Buscar posición de un elemento
    elif op == "7":
        while True:
            nombre=input("Pon el nombre de la lista en la que deseas buscar la posicion de un elemento: ")
            if nombre in listas:
                valor=input("Digita el elemento que desea buscar: ")
                if valor in listas[nombre]:
                    print(f"El elemento {valor} esta en la posicion {listas[nombre].index(valor)}")
                    input("\nPresione Enter para continuar... ")
                    break
                else:
                    print(f"El elemento  {valor}  no se ha encontrado en la lista {nombre}")
                    input("\nPresione Enter para continuar... ")
                    break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")
                break           

    #Opcion 8: Insertar un elemento 
    elif op == '8':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas ordenar: ")
            if nombre in listas:
                valor=input("Digita el elemento que deseas añadir: ")
                posicion=int(input("Digita la posicion en la que deseas añadir dicho elemento: "))
                listas[nombre].insert(posicion, valor)
                print(f"Lista actualizada: {listas[nombre]}")
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break


    #Opcion 9: Agregar un elemento al final 
    elif op == '9':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas añadir algo al final: ")
            if nombre in listas:
                valor=input("Digita el elemento que desear añadir al final de la lista: ")
                listas[nombre].append(valor)
                print(f"Lista actualizada: {listas[nombre]}")
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 10: Extender lista con varios elementos
    elif op == '10':
        while True:
            nombre=input("Pon el nombre de la lista que deseas extender con varios elementos: ")
            if nombre in listas:
                print("Ingresa los elementos que deseas añadir (escribe 'fin' cuando hayas acabado):")
                listaSumar = []
                while True:
                    valor = input(": ")
                    if valor.lower() == "fin":
                        break
                    listaSumar.append(valor)
                listas[nombre].extend(listaSumar)
                print(f"Lista actualizada: {listas[nombre]}")
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 11: Eliminar un elemento 
    elif op == '11':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas borrar un elemento: ")
            if nombre in listas:
                elim=input("Escibre el elemento que desear borrar de la lista actual: ")
                if elim in listas[nombre]:
                    listas[nombre].remove(elim)
                    print(f"Se ha borrado '{elim}' de la lista: {listas[nombre]}")
                    input("\nPresione Enter para continuar... ")
                    break
                else:
                    print(f"El elemento  {elim}  no se ha encontrado en la lista {nombre}")
                    input("\nPresione Enter para continuar... ")
                    break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 12: Contar ocurrencias de un elemento 
    elif op == '12':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas contar ocurrencias de un elemento: ")
            if nombre in listas:
                valor=input("Escibre el elemento que desea contar de la lista actual: ")
                if valor in listas[nombre]:
                    print(f"El elemento '{valor}' ha estado en la lista {listas[nombre].count(valor)} veces")
                    input("\nPresione Enter para continuar... ")
                    break
                else:
                    print(f"El elemento '{valor}'  no se ha encontrado en la lista {nombre}")
                    input("\nPresione Enter para continuar... ")
                    break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 13: Invertir lista
    elif op == '13':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas invertir: ")
            if nombre in listas:
                listas[nombre].reverse()
                print(listas[nombre])
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 14: Ordenar lista 
    elif op == '14':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas ordenar: ")
            if nombre in listas:
                tipoSort=input("Deseas ordenarlo de forma creciente (Digita 1) o decreciente (Digita 2): ")
                
                if tipoSort== '1':
                    listas[nombre].sort()
                    print(f"Lista actualizada: {listas[nombre]}")
                    input("\nPresione Enter para continuar... ")
                    break
                elif tipoSort=='2':
                    listas[nombre].sort(reverse=True)
                    print(f"Lista actualizada: {listas[nombre]}")
                    input("\nPresione Enter para continuar... ")
                    break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 15: Eliminar por índice y mostrar
    elif op == '15':
        while True:
            nombre=input("Pon el nombre de la lista de la cual deseas borrar un elemento por indice: ")
            if nombre in listas:
                elim=int(input("Escibre el elemento que desear borrar de la lista actual: "))
                listas[nombre].pop(elim)
                print(f"Se ha borrado la posicion '{elim}' de la lista \nLista actualizada: {listas[nombre]}")
                input("\nPresione Enter para continuar... ")
                break
            else:
                print("\nDicha lista aun no existe")
                input("\nPresione Enter para continuar... ")     
                break

    #Opcion 0: Salir
    elif op == '0':
        print("\nHasta luego....")
        break

    #Caso por defecto: OP invalida
    else:
        print("\n=========\nOpcion invalida. Intenta de nuevo de 0 al 15")
    #Se agrega una pausa para que el usuario pueda ver el resuldado antes de continuar
        input("\nPresione Enter para continuar... ")

