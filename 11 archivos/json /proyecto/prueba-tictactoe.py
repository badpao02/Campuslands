import random
import time

# Función que incializa los valores del juego
def inicializar_juego():
    print("\n\n1. escriba los nombres de los participantes ")
    juego_en_curso = True
    jugadores = [[input("Jugador 1 es X: "),"X"], [input("Jugador 2 es O: "),"O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-","-","-"],
               ["-","-","-"],
               ["-","-","-"]]
    movimientos = 0
    tiempo_inicio = time.time()  # Registra el tiempo al inicio del juego
    return juego_en_curso, jugadores, jugador_actual, tablero, movimientos, tiempo_inicio

# Actualiza el tablero con la acción del jugador actual
def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    while tablero_actual[coordenada_fila - 1][coordenada_columna - 1] != '-':
        print("¡Casilla ocupada! Elige otra posición.")
        coordenada_fila, coordenada_columna = list(map(int, input("Elige primero fila luego columnas: ")))
    
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual

# Comprueba si el tablero está completo, devuelve True o False
def tablero_completo(tablero_actual):
    for linea in tablero_actual:
        for celda in linea:
            if celda == '-':
                return False
    return True

# Comprueba si ha ganado el jugador actual, devuelve True o False
def comprobar_ganador(jugador, tablero_actual):

    # Comprobar por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    # Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    # Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    ganador = True
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

juego_en_curso, jugadores, jugador_actual, tablero, movimientos, tiempo_inicio = inicializar_juego()

while juego_en_curso:
    if tablero_completo(tablero):
        juego_en_curso = False
        print("Fin del juego, empate")
        break
    
    print("Turno de: " + jugadores[jugador_actual][0])

    print("0 1 2 3")
    coordenadas_vertical = 1
    for linea in tablero:
        print(coordenadas_vertical, linea[0], linea[1], linea[2])
        coordenadas_vertical += 1
    
    coordenada_fila, coordenada_columna = list(map(int, input("Elige primero fila luego columnas: ")))
    
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)
    movimientos += 1  # Incrementa los movimientos

    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
        tiempo_fin = time.time()  # Registra el tiempo al final del juego
        tiempo_transcurrido = tiempo_fin - tiempo_inicio
        print("0 1 2 3")
        coordenadas_vertical = 1
        for linea in tablero:
            print(coordenadas_vertical, linea[0], linea[1], linea[2])
            coordenadas_vertical += 1
        print("Ganador: ",jugadores[jugador_actual][0])
        print(f"El juego duró {tiempo_transcurrido:.2f} segundos y se realizaron {movimientos} movimientos.")
    
    jugador_actual = 1 if jugador_actual == 0 else 0
