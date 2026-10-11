# Piedra, Papel o Tijera en Python

Aplicación de consola desarrollada en Python que permite al usuario jugar al clásico juego "Piedra, Papel o Tijera" contra la computadora.

---

## 📌 Información del Proyecto
* **Autor:** Damian Iza
* **Fecha:** 10/10/2026
* **Objetivo:** Crear una aplicación interactiva que permita al usuario jugar piedra, papel o tijera mediante la programación en Python, aplicando estructuras de control, bucles y manipulación de listas.

---

## 🚀 Explicación del Código y Funcionamiento

El programa se divide en las siguientes etapas principales:

### 1. Importación de Módulos
Se importa el módulo `random`, el cual permite que la computadora seleccione de manera aleatoria su jugada.
```python
import random
```

### 2. Datos del Juego
Se definen las estructuras de datos iniciales:
* `opciones`: Almacena las tres jugadas válidas (`"piedra"`, `"papel"`, `"tijera"`).
* `reglas`: Almacena los textos descriptivos de las reglas del juego.
```python
opciones = ["piedra", "papel", "tijera"]
reglas = ["Piedra vence a tijera", "Tijera vence a papel", "Papel vence a piedra"]
```

### 3. Mostrar Reglas
Se utiliza un bucle `for` para recorrer la lista `reglas` e imprimirlas en pantalla al iniciar la aplicación.
```python
print("Reglas del juego:")
for regla in reglas:
    print(regla)
```

### 4. Bucle Principal (`while`)
Se inicializa la variable `jugar = "si"` para arrancar el bucle principal. El juego continuará ejecutándose siempre que el usuario decida seguir jugando.
```python
jugar = "si"
while jugar == "si":
    # Lógica del juego...
```

### 5. Validación de la Entrada del Jugador
Se solicita la jugada mediante `input()`. Si el usuario ingresa un valor que no se encuentra dentro de la lista `opciones`, un bucle `while` interno volverá a solicitar la entrada hasta que sea válida.
```python
jugador = input("\nElige piedra, papel o tijera: ")
while jugador not in opciones:
    jugador = input("Opción no válida. Elige piedra, papel o tijera: ")
```

### 6. Selección de la Computadora
La computadora utiliza `random.choice()` para escoger una opción al azar de la lista y mostrarla en pantalla.
```python
computadora = random.choice(opciones)
print("La computadora eligió:", computadora)
```

### 7. Determinación del Ganador
Se evalúan los resultados mediante estructuras condicionales:
* **`if`**: Verifica si hay empate (si el jugador y la computadora eligieron lo mismo).
* **`elif`**: Comprueba las reglas de victoria para el jugador utilizando operadores lógicos `and` y `or`.
* **`else`**: Si no se cumple ninguna de las anteriores, gana la computadora.
```python
if jugador == computadora:
    print("Empate")
elif (jugador == "piedra" and computadora == "tijera") or \
     (jugador == "tijera" and computadora == "papel") or \
     (jugador == "papel" and computadora == "piedra"):
    print("Gana el jugador")
else:
    print("Gana la computadora")
```

### 8. Reinicio del Juego
Se pregunta al usuario si desea jugar otra vez. Si la respuesta es `"si"`, el bucle principal se repite; de lo contrario, el ciclo finaliza.
```python
jugar = input("\n¿Quieres jugar de nuevo? (si/no): ")
```

### 9. Finalización
Una vez que el usuario decide no continuar, el bucle se rompe y el programa muestra el mensaje de cierre.
```python
print("Fin")
```

---

## 🛠️ Requisitos
* Tener instalado **Python 3.x** en tu equipo.

## ▶️ Ejecución
Para ejecutar el juego, abre tu terminal o entorno de desarrollo (como VS Code) y corre el siguiente comando:

```bash
python juego.py
```