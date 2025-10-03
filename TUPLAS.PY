ciudades = ("Quito", "Guayaquil", "Cuenca")
print("Segunda Ciudad:", ciudades[1])

try:
    ciudades[0] = "Ambato"
except TypeError as e:
    print("Error:", e)

ciudades_listas = list(ciudades)
ciudades_listas.append("Ambato")
ciudades = tuple(ciudades_listas)
print("Nueva tupla:", ciudades)
 