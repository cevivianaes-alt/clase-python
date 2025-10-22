#es un conjunto de elementos unicos, es mutable  
frutas = { "manzana", "pera", "naranja", "manzana"}
print(frutas)

#print(frutas [0]) esto no se hae en un conjunto 

numeros = set ({1, 2, 3, 3, 4})
print(numeros)

#agregar elemento y remover
numeros.add(5)
print(numeros)

numeros.remove(2)

#es un set, no se guia por indice
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

#union sin repeticion
print("Union: ", a | b )
#elemntos que se intersectan
print("Interseccion: ", a & b)
#elementos que estan en a y no estan en b 
print("Diferencia: ", a - b)
#elementos que estan en a o en b pero no en son ambos 
print("Diferencia simetrica: ", a ^ b)

