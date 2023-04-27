Datos_2021 = [1, 2, 3, 4, 5, 6, 7, 100, 91, 110, 900, 21, 33, 32, 2, 4, 8, 10, 13, 13, 16, 15, 1302]

# Creamos dos listas vacías para almacenar los números pares e impares
pares = []
impares = []

# Recorremos la tupla y evaluamos si cada número es par o impar
for num in Datos_2021:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostramos los resultados
print("Números pares:", pares)
print("Números impares:", impares)