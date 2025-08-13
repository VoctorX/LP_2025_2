op=1
while op==1:
    num=float(input("Digite un numero: "))
    if (num%2)== 0 :
        print(f"Su numero '{num}' es par")
    else:
        print(f"Su numero '{num}' es impar")
    op=int(input("¿Desea seguir con otro numero? (1.Si)(2.No): "))
print("Gracias por usar el programa")