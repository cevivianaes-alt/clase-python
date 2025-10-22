
#def nombre_de_funcion(parametros):
#codigos a ejecutar
#return resultado


def saludar():
    print("hola, bienvenido a Python")
saludar()

#parametros y vslores del retorno
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar (5, 3)
print("La suma es: ", total)

def saludar(nombre = "invitado"):
    print(f"Hola, {nombre}")

saludar("Viviana")
saludar()

#indica donde una variable es accecible en una funcion
def mostrar_numero():
    x = 10 #variable local
    print("Dentro de las funcion:", x)

mostrar_numero()
#print(x) da error porque x es una variable local

#variable global
x = 100

def mostrar():
    print("Dentro de la funcion:", x)

mostrar()
print("Fuera de la funcion:", x)

#cambio de una variable a una funciòn
contador = 0 

def incrementar():
    global contador 
    contador += 1

incrementar()
incrementar()
print("Contador: ", contador)

 


