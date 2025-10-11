# Lista de números
numeros = [4, 7, 2, 4, 9, 2, 8, 6, 7]

# Eliminar duplicados
numeros_sin_duplicados = list(set(numeros))
print("Lista sin duplicados:", numeros_sin_duplicados)

# Ordenar la lista
numeros_ordenados = sorted(numeros_sin_duplicados)
print("Lista ordenada:", numeros_ordenados)

# Números pares
numeros_pares = [n for n in numeros_ordenados if n % 2 == 0]
print("Números pares:", numeros_pares)
