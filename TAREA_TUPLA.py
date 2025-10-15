# Tupla de números enteros
numeros = (5, 8, 12, 3, 9, 5, 2)

#valor máximo y mínimo
maximo = max(numeros)
minimo = min(numeros)
print("Valor Máximo: ", maximo )
print("Valor Mínimo: ", minimo )

#Promedio de todos los valores
promedio = sum(numeros) / len(numeros)
print("Promedio:", round(promedio, 2))
#redund(promedio, 2) = redondear a dos dijitos

#verificar si un número ingresado por el usuario está dentro de la tupla
numero_ingresado = int(input("Ingrese un número: "))
if numero_ingresado in numeros:
    print("El número ingresado está en la tupla.")
else:
    print("El numero no esta dentro de la tupla")
