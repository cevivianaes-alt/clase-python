#basico
#try: 
#      codigo que puede causar error 
#except:
#      codigo que se ejecuta si ocurre un error

try:
    numero = int(input("Ingrese numero"))
    resultado = 10/numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
#VALUE ERROR
try:
    edad = int(input("Ingrese numero"))
    print("Su edad es:", edad)
except ValueError:
    print("Error: Debe ingresar un numero entero valido") 

#MULTIPLES EXCEPTOS

try: 
    a = int(input("Ingrese numerador"))
    b = int(input("Ingrese denominador"))
    resultado = a/b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError:
    print("Error: Debe ingresar un numero entero valido")

#else y finaly
try:
    numero = int(input("Ingrese numero positivo"))
    if numero < 0:
        raise ValueError("DEBE SER POSITIVO")
except ValueError as e:
    print("Error:", e)
else:
    print("No hubo errores")
finally:
    print("Fin del programa")    
