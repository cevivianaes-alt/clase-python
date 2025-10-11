#ingresar inventario
inventario = {"manzana": 10, "peras": 3, "naranjas": 8}
print("Inventario inicial: ", inventario)

#agregar un nuevo producto y cantidad
inventario["kiwi"] = 7
print("Agregar kiwi:", inventario)

# actualizar cantidad de kiwi
inventario["kiwi"] = 9
print("Cantidad actualizada de kiwi:", inventario)

#mostrar todos los productos en stock que sean menor a 5
print("Productos con stock:")
for producto, cantidad in inventario.items():
    if cantidad < 5:
        print(f"{producto}: {cantidad}")
