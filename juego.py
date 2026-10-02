
# 1. Inicio
import random

# 2. Datos del juego 
opciones = ["piedra", "papel", "tijera"]
reglas = ["Piedra vence a tijera", "Tijera vence a papel", "Papel vence a piedra"]
 
# 3. Mostrar reglas
print("Reglas del juego:")
for regla in reglas:
    print(regla)

# 4. Bucle principal (while)
jugar = "si"
while jugar == "si":
 
    # 5. El jugador elige
    jugador = input("\nElige piedra, papel o tijera: ")
    while jugador not in opciones:
        jugador = input("Opción no válida. Elige piedra, papel o tijera: ")
 
    # 6. La computadora elige
    computadora = random.choice(opciones)
    print("La computadora eligió:", computadora)
 
    # 7. Ganador
    if jugador == computadora:
        print("Empate")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print("Gana el jugador")
    else:
        print("Gana la computadora")
 
    # 8. Jugar de nuevo
    jugar = input("\n¿Quieres jugar de nuevo? (si/no): ")

    # 9. Fin 
print("Fin")
 
 