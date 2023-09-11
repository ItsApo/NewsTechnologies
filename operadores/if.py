# age = int(input("Ingresa tu edad: "))
# height = int(input("Ingresa tu estatura: "))


# if age >= 17 and height >= 150:
#     print("Puedes ingresar a la atracción")
# else:
#     print("Abrite de aqui")

while True:
    age = int(input("Ingresa tu edad (o ingresa -1 para salir): "))
    
    if age == -1:
        print("¡Hasta luego!")
        break
    
    height = int(input("Ingresa tu estatura: "))
    
    if age >= 17 and height >= 150:
        print("Puedes ingresar a la atracción")
    else:
        print("Abrite de aqui")
