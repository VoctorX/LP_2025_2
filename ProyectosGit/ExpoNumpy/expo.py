import numpy as np

print("=== SISV - Distancias entre accidentes con coordenadas reales ===")

# Entrada de coordenadas reales (latitud y longitud)
acc1_lat = float(input("Ingrese la LATITUD del Accidente 1: "))
acc1_lon = float(input("Ingrese la LONGITUD del Accidente 1: "))
print("============")
acc2_lat = float(input("Ingrese la LATITUD del Accidente 2: "))
acc2_lon = float(input("Ingrese la LONGITUD del Accidente 2: "))
print("============")
acc3_lat = float(input("Ingrese la LATITUD del Accidente 3: "))
acc3_lon = float(input("Ingrese la LONGITUD del Accidente 3: "))

# Calcular distancias euclidianas directamente sobre lat/lon
d12 = np.sqrt((acc1_lat - acc2_lat)**2 + (acc1_lon - acc2_lon)**2)
d13 = np.sqrt((acc1_lat - acc3_lat)**2 + (acc1_lon - acc3_lon)**2)
d23 = np.sqrt((acc2_lat - acc3_lat)**2 + (acc2_lon - acc3_lon)**2)

print("\n--- Resultados ---")
print("Distancia entre Accidente 1 y 2:", round(d12, 6), "grados")
print("Distancia entre Accidente 1 y 3:", round(d13, 6), "grados")
print("Distancia entre Accidente 2 y 3:", round(d23, 6), "grados")

# Determinar cuáles están más cercanos
min_dist = min(d12, d13, d23)

if min_dist == d12:
    print("👉 Los accidentes más cercanos son el 1 y el 2")
elif min_dist == d13:
    print("👉 Los accidentes más cercanos son el 1 y el 3")
else:
    print("👉 Los accidentes más cercanos son el 2 y el 3")
