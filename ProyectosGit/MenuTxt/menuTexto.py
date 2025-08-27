# -*- coding: utf-8  -*-
""""
===============================================================
|                 Text Changer- Menu                   |
===============================================================

Este programa es un cambiador de texto que permite modificar el formato del texto ingresado por el usuario.

Autor: Victor Cordoba
Fecha: 2025-08-25

"""

while True:
    texto=str(input("\nIngrese el texto que desea convertir: "))

    print("\n==Mostrar Menu==")
    print("1.Primera Letra en Mayuscula")
    print("2.Primeras Letras en Mayuscula")
    print("3.Todo en Minuscula")
    print("4.Todo en Mayuscula")
    print("5.Salir")

    # Solicitar al usuario que elija u8na opcion del menu
    op=input("Selecciones una de las opciones (1-5): ")

    # ====OPeraciones====

    #OpcioN 1: Primera Letra en Mayuscula
    if op== '1':
        resultado= texto.capitalize()
        print(f"Tu nuevo texto: {resultado}")

    #OpcioN 2: Primeras letras en Mayusculas
    elif op == '2':
        resultado= texto.title()
        print(f"Tu nuevo texto: {resultado}")


    #OpcioN 3: Todo Minuscula
    elif op == '3':
        resultado= texto.lower()
        print(f"Tu nuevo texto: {resultado}")

    #OpcioN 4: Todo Mayuscula
    elif op == '4':
        resultado= texto.upper()
        print(f"Tu nuevo texto: {resultado}")

    #OpcioN 5: Salir
    elif op == '5':
        print("Hasta luego....")
        break
    
    #Casp por defecto: OP invalida
    else:
        print("\n=========\nOpcion invalida. Intenta denuevo de 1 al 5")

    #Se agrega una pausa para que el usuario pueda ver el resuldado antes de continuar
        input("\nPresione Enter para continuar... ")