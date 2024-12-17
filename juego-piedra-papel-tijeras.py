def jugar():
#1. Pedimos los nombres a los jugadores
    nombre1 = input("Jugador 1, ¿Cómo te llamas? ")
    nombre2 = input("Jugador 2, ¿Cómo te llamas? ")

    while True: 
        #2. Pedimos a los jugadores que elijan y formateamos el input para que no sea case-sensitive
        jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ").lower()
        jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ").lower()

        #3. Verificamos las condiciones para la victoria
        condicion1 = (jugador1 == "piedra" and jugador2 == "tijeras")
        condicion2 = (jugador1 == "tijeras" and jugador2 == "papel")
        condicion3 = (jugador1 == "papel" and jugador2 == "piedra")
        
        # 4. Determinamos el resultado
        if jugador1 == jugador2:
            print("¡Es un empate!")
        elif condicion1 or condicion2  or condicion3:
            print(f"¡Ha ganado {nombre1}!")
        else:
            print(f"¡Ha ganado {nombre2}!")
        
        # 5. Preguntamos si quieren jugar de nuevo
        otra_ronda = input("¿Quieren jugar otra vez? (si/no): ").lower()
        if otra_ronda != "si":
            print("¡Gracias por jugar!")
            break

# Llamamos la función nuevamente para que re-inicie el juego
    
jugar()