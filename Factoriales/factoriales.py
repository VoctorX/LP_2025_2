num=int(input("Digite un numero para ver su factorial: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"El factorial de '{num}' es: {factorial}")