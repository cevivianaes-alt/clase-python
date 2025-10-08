persona = {"Nombre": "Viviana", "Edad": 21, "Ciudad": "Guayaquil"}
print("Diccionario Inicial:", persona)

print("Edad: ", persona.get("edad"))

persona["Profesion"] = "Ingeniero"
print("Persona con profecion: ", persona)

print("Clave", persona.keys()) #claves
print("Valores", persona.values()) #valores

persona["Ciudad"] = "Quito"
print("Ciudad modificada", persona)
