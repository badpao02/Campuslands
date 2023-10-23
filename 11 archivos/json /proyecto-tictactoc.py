import random

# Función que inicializa los valores del juego
def inicializar_juego():
    juego_en_curso = True
    jugadores = [[input("Jugador 1 es X: "),"X"], [input("Jugador 2 es O: "),"O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return juego_en_curso, jugadores, jugador_actual, tablero

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
    # Código sin cambios

# Función para jugar una partida

def jugar_partida():
    juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()
    while juego_en_curso:
        if tablero_completo(tablero):
            juego_en_curso = False
            print("Fin del juego, no hay ganador")
            break
        
        print("Turno de: " + jugadores[jugador_actual][0])

        print("0 1 2 3")
        coordenadas_vertical = 1
        for linea in tablero:
            print(coordenadas_vertical, linea[0], linea[1], linea[2])
            coordenadas_vertical += 1
        
        coordenada_fila, coordenada_columna = list(map(int, input("Elige primero fila luego columnas: ")))
        
        tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)
        
        if comprobar_ganador(jugadores[jugador_actual], tablero):
            juego_en_curso = False
            print("0 1 2 3")
            coordenadas_vertical = 1
            for linea in tablero:
                print(coordenadas_vertical, linea[0], linea[1], linea[2])
                coordenadas_vertical += 1
            print("Ganador: ",jugadores[jugador_actual][0])
            
            # Registrar ganador
            ganadores.append(jugadores[jugador_actual][0])
            # Registrar perdedor
            perdedores.append(jugadores[1 - jugador_actual][0])

        jugador_actual = 1 if jugador_actual == 0 else 0

# Lista para almacenar ganadores y perdedores
ganadores = []
perdedores = []

# Jugar 5 partidas
for _ in range(5):
    jugar_partida()

# Mostrar resultados
print("\nResultados:")
for i in range(len(ganadores)):
    print(f"Partida {i+1}: Ganador: {ganadores[i]}, Perdedor: {perdedores[i]}")




#https://javierportales.com/cursos/python/juego-3-en-raya-tic-tac-toe/

