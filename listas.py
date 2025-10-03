numeros = [1, 2, 3, 4, 5]
print("tercer elemento:", numeros [2] )

numeros.append(6)
print("despues de append:", numeros)

numeros.remove(3)
print("despues de remove(3):", numeros)

numeros.sort()
print("Ordenados ascendentes:", numeros)

numeros.sort(reverse=True)
print("Ordenados ascendentes:", numeros)

print("Dos primeros elementos:", numeros[:2])

print("dimension lista:", len(numeros))