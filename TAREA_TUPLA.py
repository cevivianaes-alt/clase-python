# Tupla de números enteros
numeros = (5, 8, 12, 3, 9, 5, 2)

#valor máximo y mínimo
print("Valor Máximo: ", numeros[0])
print("Valor Mínimo: ", numeros[6])

#Promedio de todos los valores
promedio = sum(numeros) / len(numeros)
print("Promedio de todos los valores: ", promedio)

#verificar si un número ingresado por el usuario está dentro de la tupla
numero_ingresado = int(input("Ingrese un número: "))
if numero_ingresado in numeros:
    print("El número ingresado está en la tupla.")

