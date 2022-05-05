CELDAS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
X, O, BLANCO = 'X', 'O', ' '


def main():
    print('Bienvenido a 4 en raya!')
    tablero_juego = obtenerTableroVacio()  # Crea el tablero vacío de 3 en raya
    jugador_actual, jugador_siguiente = X, O  # X primero, O siguiente

    while True:  # Bucle principal del juego
        # Muestra el tablero en pantalla:
        print(obtenerStrTablero(tablero_juego))

        # pregunta mientras el usuario no introduzca una celda válida
        movimiento = None
        while not esCeldaValida(tablero_juego, movimiento):
            print('')
            print('Cuál es el movimiento de {}? (1-16)'.format(jugador_actual))
            movimiento = input('> ')

        tablero_juego[movimiento] = jugador_actual

        # Comprueba si el juego ha terminado
        if esGanador(tablero_juego, jugador_actual):  # Comprueba si hay ganador
            print(obtenerStrTablero(tablero_juego))
            print('')
            print(jugador_actual + ' ha ganado la partida!')
            break
        elif tableroLleno(tablero_juego):  # Comprueba si hay empate
            print(obtenerStrTablero(tablero_juego))
            print('')
            print('Empate!')
            break

        # Cambio de turno entre jugadores:
        jugador_actual, jugador_siguiente = jugador_siguiente, jugador_actual

    print('Gracias por jugar!')


def obtenerTableroVacio():
    """Crea un tablero vacío para la partida de 3 en raya."""
    # Mapeado : 1|2|3
    #           -+-+-
    #           4|5|6
    #           -+-+-
    #           7|8|9
    tablero = {}
    for celda in CELDAS:
        tablero[celda] = BLANCO  # Todas las celdas del tablero se inicializan a BLANCO
    return tablero


def obtenerStrTablero(tablero):
    """Devuelve el tablero formateado como cadena de texto."""
    return '''
      _________
      |{}|{}|{}|{}|  1  2  3  4
      |-------|
      |{}|{}|{}|{}|  5  6  7  8
      |-------|
      |{}|{}|{}|{}|  9  10 11 12
      |-------|
      |{}|{}|{}|{}|  13 14 15 16
      ---------
      '''.format(tablero['1'], tablero['2'], tablero['3'],
                 tablero['4'], tablero['5'], tablero['6'],
                 tablero['7'], tablero['8'], tablero['9'],
                 tablero['10'], tablero['11'], tablero['12'],
                 tablero['13'], tablero['14'], tablero['15'], tablero['16'])


def esCeldaValida(tablero, celda):
    """Devuelve True si la celda es válida y está en BLANCO."""
    return celda in CELDAS and tablero[celda] == BLANCO


def esGanador(tablero, jugador):
    """Devuelve True si el jugador es ganador."""
    # Se utilizan variables cortas para mejorar la legibilidad
    b, p = tablero, jugador
    # Busca el 3 en raya en las 3 filas, 3 columnas y las 2 diagonales
    return ((b['1'] == b['2'] == b['3'] == b['4'] == p) or  # Horizontal arriba 1
            (b['5'] == b['6'] == b['7'] == b['8'] == p) or  # Horizontal arriba 2
            (b['9'] == b['10'] == b['11'] == b['12'] == p) or  # Horizontal abajo 2
            (b['13'] == b['14'] == b['15'] == b['16'] == p) or  # Horizontal abajo 1
            (b['1'] == b['5'] == b['9'] == b['13'] == p) or  # Vertical izquierda 1
            (b['2'] == b['6'] == b['10'] == b['14'] == p) or  # Vertical izquierda 2
            (b['3'] == b['7'] == b['11'] == b['15'] == p) or  # Vertical derecha 2
            (b['4'] == b['8'] == b['12'] == b['16'] == p) or  # Vertical derecha 1
            (b['4'] == b['7'] == b['10'] == b['13'] == p) or  # Diagonal
            (b['1'] == b['6'] == b['11'] == b['16'] == p))  # Diagonal


def tableroLleno(tablero):
    """Devuelve True si todas las celdas están ocupadas."""
    for celda in CELDAS:
        if tablero[celda] == BLANCO:
            return False  # Hay al menos una celda que no está en blanco por lo que devolvemos False
    return True  # Ningún espacio en BLANCO por lo que se devuelve True


if __name__ == '__main__':
    main()
