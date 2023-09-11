# Declaración de listas
nombres = ["Pepito", "Andres", "Juan", "Maria", "Pedro"]
edades = [25, 19, 21, 33, 40]
estaturas = [1.80, 1.65, 1.74, 1.66, 1.54]
casados = [False, False, False, True, True]
usuario = ["Pepito", 25, 1.80, False]

# Obtener la longitud de una lista con len()
longitud_edades = len(edades)
print(longitud_edades)

# Verificar el tipo de datos de las listas con type()
print(type(nombres))
print(type(edades))
print(type(estaturas))
print(type(casados))
print(type(usuario))

# Slicing - obtener elementos de una lista mediante rangos
print(usuario[0:3])
print(nombres[1:3])
print(nombres[:3])
print(nombres[1:])
print(nombres[:-1])
print(nombres[:4])
print(nombres[-4:-1])
print(nombres[1:4])

# Verificar si un elemento existe en una lista con "in"
if "Pepito" in nombres:
    print("El nombre está en la lista")
else:
    print("No se encontró el nombre buscado")

# Modificar elementos en una lista
usuario[0] = "Luis"
nombres[0:3] = ["Manuel", "Jorge", "Andrea"]
print(nombres)

# Insertar elementos en una posición específica
nombres.insert(0, "Pepito")
print(nombres)

# Agregar elementos al final de la lista con append()
nombres.append("Laura")
print(nombres)

# Extender una lista con otra lista
nombres2 = ["Ricardo", "Erre"]
nombres.extend(nombres2)
print(nombres)

# Eliminar elementos de una lista
nombres.remove("Erre")
print(nombres)

nombres.pop(4)
print(nombres)

del nombres[1]
print(nombres)

# Vaciar una lista sin eliminarla completamente
nombres.clear()

# Recorrer una lista con un bucle for
for edad in edades:
    print(edad)

# Iterar sobre los índices de una lista
for i in range(len(estaturas)):
    print(estaturas[i])

# List comprehension para imprimir elementos
[print(x) for x in edades]

# Iterar con un bucle while
i = 0
while i < len(usuario):
    print(usuario[i])
    i += 1

# Enumerar elementos en una lista
for i, edad in enumerate(edades):
    print(i, edad)