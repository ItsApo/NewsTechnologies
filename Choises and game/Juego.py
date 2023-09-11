import random

vidas = 5
puntos = 0

while vidas > 0:
    num = random.randint(0, 9)
    
    if num == 0:
        vidas -= 1
    else:
        puntos += 1

    print("Vidas:", vidas)
    print("Puntos:", puntos)

print("Juego Terminado")
