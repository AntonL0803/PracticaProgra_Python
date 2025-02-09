import random


numero = random.randint(1, 100)

numeroJugador = 0
contador = 0

while numeroJugador != numero:

    numeroJugador = int(input("Introduce un numero: "))
    
    
    if numeroJugador < numero:
        print("El numero es mayor")
    elif numeroJugador > numero:
        print("El numero es menor")
    else:
        print("Has acertado el numero")
        print("Has necesitado " + contador + " intentos.")
    contador += 1