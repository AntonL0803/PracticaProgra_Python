import random


print("Bienvenido a Piedra, Papel o Tijera, lagarto, spock")
opcion1 = input("Escribe el objeto que quieres sacar: ")

if opcion1.lower() == "piedra" or opcion1.lower() == "papel" or opcion1.lower() == "tijera" or opcion1.lower() == "lagarto" or opcion1.lower() == "spock":
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
    eleccion = random.choice(opciones)
    print(eleccion)
    if opcion1.lower() == eleccion:
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS EMPATADO")
    elif (opcion1.lower() == "piedra" and eleccion in ["tijera", "lagarto"]) or (opcion1.lower() == "papel" and eleccion in ["piedra", "spock"]) or (opcion1.lower() == "tijera" and eleccion in ["papel", "lagarto"]) or (opcion1.lower() == "lagarto" and eleccion in ["spock", "papel"]) or (opcion1.lower() == "spock" and eleccion in ["tijera", "piedra"]):
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS GANADO")
    else:
        print("Jugador: " + opcion1 + " Ordenador: " + eleccion + ", HAS PERDIDO")
else:
    print("No ha introducido ningún valor válido")