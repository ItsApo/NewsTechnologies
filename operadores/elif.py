while True:
    pay = float(input("Ingrese el valor de su pago: "))

    service = int(input("Desea incluir el servicio? Yes = 1 / No = 0"))

    if service == 1:
        print("El valor total a pagar es de ", pay + (pay * 0.1))
    elif service == 0: print("El valor total es de ",pay)
    else: print("Ingrese una opcion valida")