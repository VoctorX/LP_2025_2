# -*- coding: utf-8  -*-
""""
===============================================================
|                 Calculadora Simple - Menu                   |
===============================================================

Este programa us en una calculadora qcon un menu interactivo que permite realizar operaciones basicas como suma, resta, multiplicacion, division.

Autor: Victor Cordoba
Fecha: 2025-08-13

"""

# Crear un bucle infinito para mostrar el menu hasta que el usuario decida salir
while True:
    num1=float(input("\nIngrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: ")) 

    print("\n==Mostrar Menu==")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")

    # Solicitar al usuario que elija u8na opcion del menu
    op=input("Selecciones una de las opciones (1-5): ")

    # ====OPeraciones====

    #OpcioN 1: Sumar
    if op== '1':
        resultado=num1+num2
        print(f"La suma de {num1} y {num2} es: {resultado}")

    #OpcioN 2: Restar
    elif op == '2':
        resultado=num1-num2
        print(f"La resta de {num1} y {num2} es: {resultado}")    

    #OpcioN 3: Multi
    elif op == '3':
        resultado=num1*num2
        print(f"La mutlplicacion de {num1} y {num2} es: {resultado}")      

    #OpcioN 4: Division
    elif op == '4':
        resultado=num1/num2
        print(f"La division de {num1} y {num2} es: {resultado}")

    #OpcioN 5: Salir
    elif op == '5':
        print("Hasta luego....")
        break
    
    #Casp por defecto: OP invalida
    else:
        print("\n=========\nOpcion invalida. Intenta denuevo de 1 al 5")

    #Se agrega una pausa para que el usuario pueda ver el resuldado antes de continuar
        input("\nPresione Enter para continuar... ")