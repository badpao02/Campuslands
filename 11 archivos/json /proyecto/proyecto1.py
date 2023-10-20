import random
import time
import json

# Cargar información de jugadores
def cargar_info_jugadores():
    try:
        with open('11 archivos/json /proyecto/info_jugadores.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Guardar información de jugadores
def guardar_info_jugadores(info):
    with open('11 archivos/json /proyecto/info_jugadores.json', 'w') as file:
        json.dump(info, file)

# Cargar tabla de calificaciones
def cargar_tabla():
    try:
        with open('tabla_calificaciones.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar tabla de calificaciones
def guardar_tabla(tabla):
    with open('tabla_calificaciones.json', 'w') as file:
        json.dump(tabla, file)

# Comprueba si el tablero está completo, devuelve True o False
def tablero_completo(tablero_actual):
    for linea in tablero_actual:
        for celda in linea:
            if celda == '-':
                return False
    return True

# Actualiza el tablero con la acción del jugador actual
def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    while tablero_actual[coordenada_fila - 1][coordenada_columna - 1] != '-':
        print("¡Casilla ocupada! Elige otra posición.")
        coordenada_fila, coordenada_columna = list(map(int, input("Elige primero fila luego columnas: ")))
    
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual

# Comprueba si ha ganado el jugador actual, devuelve True o False
def comprobar_ganador(jugador, tablero_actual):

    # Comprueba por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    # Comprueba por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    # Comprueba por diagonales
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

# Función que inicializa los valores del juego
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

# (El resto del código permanece igual)

while True:
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
            print("Ganador: ", jugadores[jugador_actual][0])
            print(f"El juego duró {tiempo_transcurrido:.2f} segundos y se realizaron {movimientos} movimientos.")
            
            # Guardar jugador ganador
            tabla_calificaciones = cargar_tabla()
            tabla_calificaciones.append({
                "Nombre": jugadores[jugador_actual][0],
                "Movimientos": movimientos,
                "Tiempo": tiempo_transcurrido
            })
            guardar_tabla(sorted(tabla_calificaciones, key=lambda x: (x["Movimientos"], x["Tiempo"])))

            # Actualizar información de jugadores
            info_jugadores = cargar_info_jugadores()
            jugador_ganador = jugadores[jugador_actual][0]
            if jugador_ganador in info_jugadores:
                info_jugadores[jugador_ganador]["Victorias"] += 1
                info_jugadores[jugador_ganador]["Tiempo Total"] += tiempo_transcurrido
                info_jugadores[jugador_ganador]["Intentos Total"] += movimientos
            else:
                info_jugadores[jugador_ganador] = {
                    "Victorias": 1,
                    "Tiempo Total": tiempo_transcurrido,
                    "Intentos Total": movimientos
                }
            guardar_info_jugadores(info_jugadores)

        jugador_actual = 1 if jugador_actual == 0 else 0

    # Preguntar si quieren jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() != 's':
        break

# Mostrar tabla de clasificaciones
tabla_calificaciones = cargar_tabla()
print("\nTabla de Clasificaciones:")
print("Nombre\tMovimientos\tTiempo")
for jugador in tabla_calificaciones:
    print(f"{jugador['Nombre']}\t{jugador['Movimientos']}\t\t{jugador['Tiempo']:.2f}")

# Mostrar información de jugadores
info_jugadores = cargar_info_jugadores()
print("\nInformación de Jugadores:")
print("Nombre\tVictorias\tTiempo Total\tIntentos Total")
for jugador, info in info_jugadores.items():
    print(f"{jugador}\t{info['Victorias']}\t\t{info['Tiempo Total']:.2f}\t\t{info['Intentos Total']}")





