# juego de tik tak tok 

import random

import json

#funcion que inicia valores de juego 
def inicializarJuego():
    juegoEnCurso = True
    jugadores = [[input("jugador 1: "), "x"]], [input("jugador 2: "), "o"]
    jugadorActual= random.randint(0,1)
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return juegoEnCurso, jugadores, jugadorActual, tablero

#actualiza el tablero con la accion del jugador actual
def actualizarTablero(jugador, coordenadaFila,coordenadaColumna,tableroActual):
    tableroActual[coordenadaFila -1][coordenadaColumna -1] = jugador[1]
    return tableroActual

#comprueba si el tablero esta completo, devuelve true o false 
def tableroCompleto(tableroActual):
    for linea in tableroActual:
        for celda in linea:
            if celda == '-':
                return False
            
    return True


#comprueba si ha ganado el jugador actual, devuelve True o False


#comprobar por filas 
def comprobarGanador(jugador, tableroActual):
    #comprobar por columnas 
    for i in range(3):
        ganador = True
        for x in range(3):
            if tableroActual[x][i] != jugador[1]:
                ganador = False
                break 
            if ganador: 
                return ganador
        
        #comprobar por diagonales 
        ganador = True
        for x in range(3):
            if tableroActual[i][i] != jugador[1]:
                ganador = False
                break
        
        if ganador:
            return ganador
        
        ganador = True
        for i in range(3):
            if tableroActual[i][3 - 1 -i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
        
        return False
juegoEnCurso, jugadores, jugadorActual, tablero = inicializarJuego()

while juegoEnCurso:
    if tableroCompleto(tablero):
        juegoEnCurso = False
        
        print("Fin del juego, no hay ganador")
        break


    #Nuevo turno
    print("Turno de: " + jugadores[jugadorActual][0])
    
    #Dibujar tablero
    print("0 1 2 3")
    coordenadasVertical = 1
    for linea in tablero:
        print(coordenadasVertical, linea[0], linea[1], linea[2])
        coordenadasVertical += 1

    #Selección de casilla
    coordenadaFila, coordenadaColumna = list(map(int, input("Elige primero fila luego columnas: ")))
    #Actuaizar tablero
    tablero = actualizarTablero(jugadores[jugadorActual], coordenadaFila, coordenadaColumna, tablero)


    #Comprobamos si ha ganado
    if comprobarGanador(jugadores[jugadorActual], tablero):
        juegoEnCurso = False
        
        #Dibujar tablero
        
        print("0 1 2 3")
        coordenadasVertical = 1
        for linea in tablero:
            print(coordenadasVertical, linea[0], linea[1], linea[2])
            coordenadasVertical += 1
        print("Ganador: ",jugadores[jugadorActual][0])

    #Cambio de jugador
    jugadorActual = 1 if jugadorActual == 0 else 0




#https://javierportales.com/cursos/python/juego-3-en-raya-tic-tac-toe/

