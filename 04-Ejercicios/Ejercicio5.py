import random


print("Bienvenido a Piedra, Papel o Tijera")
opcion1 = input("Escribe el objeto que quieres sacar: ")

if opcion1.lower() == "piedra" or opcion1.lower() == "papel" or opcion1.lower() == "tijera":
    opciones = ["piedra", "papel", "tijera"]
    eleccion = random.choice(opciones)
    print(eleccion)
    if opcion1.lower() == eleccion:
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS EMPATADO")
    elif (opcion1.lower() == "piedra" and eleccion == "tijera") or (opcion1.lower() == "papel" and eleccion == "piedra") or (opcion1.lower() == "tijera" and eleccion == "papel"):
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS GANADO")
    else:
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS PERDIDO")
else:
    print("No ha introducido ningún vaor válido")
