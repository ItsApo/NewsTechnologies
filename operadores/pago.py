pago = input("Haz realizado el pago? (si o no): ")

if pago == "si":
    serv = input("Desea incluir el servicio? (si o no): ")
    if serv == "si":
        print("Gracias por comprar")
    elif serv == "no":
        print("Se ha rechazado su compra")
    else:
        print("Ha ocurrido un error en la compra")
elif pago == "no":
    pago = input("Deseas hacer un pedido? (si o no): ")
    if pago == "si":
        serv = input("Desea incluir el servicio? (si o no): ")
        if serv == "si":
            print("Gracias por comprar")
        elif serv == "no":
                print("Se ha rechazado su compra")
        else:
                print("Ha ocurrido un error en la compra")
else:
    print("Ha ocurrido un error, ingresa una opcion valdida")
    