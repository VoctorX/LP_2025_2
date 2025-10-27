def par(numero):
    if numero % 2 ==0:
        return True
    else:
        return False
numero= int(input("Digita el numero para ver si es par o no: "))
print(par(numero))