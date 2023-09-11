print("------------------------------")
print("********* PURCHASE ***********")
print("------------------------------")

def obtener_valor_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor, ingrese un número válido.")

compra = obtener_valor_entero("Ingresa Valor de la Compra: ")
cuotas = obtener_valor_entero("Ingresa el Número Cuotas: ")
int_pagar = 1 

montoCuota = compra / cuotas

print("------------------------------")
print("********* PAYMENT ***********")
print("------------------------------")

while int_pagar == 1:
    if cuotas == 0:
        print("Su compra ya ha sido pagada!")
        break
    else:
        cuotas -= 1
        compra -= montoCuota
        print("Cuotas restantes:", cuotas)
        print("Monto restante:", compra)

print("GRACIAS")
