numero = int(input("Ingresar un numero"))
a, b = 0, 1

print("Serie Fibonacci")
for _ in range(numero):
    print(a, end=" ")
    a, b = b, a + b