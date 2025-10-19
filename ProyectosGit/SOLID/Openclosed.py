from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class Tarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta de credito...")

class Efectivo(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} en efectivo...")

class Paypal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con PayPal...")

class Crypto(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con criptomonedas...")


# Este codigo respeta el principio Open/Closed
# Si quisiéramos agregar otro método, por ejemplo "Nequi",
# solo crearíamos una nueva clase:
# 
# class Nequi(MetodoPago):
#     def pagar(self, monto):
#         print(f"Pagando ${monto} con Nequi...")
# 
# Y luego añadiríamos una nueva opción en el diccionario de métodos,
# SIN modificar las clases existentes.


print("=== Metodos de Pagos ===")
print("1. Tarjeta de credito")
print("2. Efectivo")
print("3. PayPal")
print("4. Criptomonedas")

opcion = input("Selecciona un metodo de pago: ")
monto = float(input("Ingresa el monto a pagar: "))

metodos = {
    "1": Tarjeta(),
    "2": Efectivo(),
    "3": Paypal(),
    "4": Crypto()
}

metodo = metodos.get(opcion)
if metodo:
    metodo.pagar(monto)
else:
    print("Opción invalida.")
