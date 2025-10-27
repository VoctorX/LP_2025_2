def calcular(nacimiento):
    actual=2025
    edad=actual-nacimiento
    return edad

nacimiento = int(input("Digite el año en que naciste: "))
print(calcular(nacimiento))