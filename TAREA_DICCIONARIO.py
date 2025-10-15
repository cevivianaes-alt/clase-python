#ingresar inventario
inventario = {"manzana": 10, "peras": 3, "naranjas": 8}
print(inventario)

#agregar un nuevo producto y cantidad
producto_nuevo = input("Ingrese el nombre del nuevo producto: ")
cantidad_nueva = int(input("Ingrese la cantidad en stock:"))
inventario[producto_nuevo] = cantidad_nueva

# actualizar cantidad de kiwi
producto_actualizar = input("Ingrese el producto que desea actualizar:")
if (producto_actualizar in inventario):
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    inventario[producto_actualizar] = nueva_cantidad
else:
    print("El producto no existe en el inventario")

    print(inventario)

#mostrar todos los productos en stock que sean menor a 5
print("Productos con stock bajo:")
for producto, cantidad in inventario.items():
    if cantidad < 5:
        print(f"{producto}: {cantidad}")
