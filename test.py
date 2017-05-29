import random
import time
import socketIO_client
#s = socketIO_client.SocketIO('10.226.186.253', 3000)


INICIAL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SEGUNDO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BASE_HASH = hash(''.join(str(e) for e in INICIAL))
MOVS_INICIALES = [19, 26, 37, 44]

def get_possible_moves(tablero_lineal, player_id):
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    #print tablero_lineal
    board = convert_to_square(tablero_lineal)
    #print board
    #revisar si el tablero es el inicial


    movs = []
    # revisar movimientos hacia arriba
    for i in range(8):
        #print movs
        for j in range(8):
            # se revisa todo el tablero
            # para cada ficha que tenemos hay que considerar
            # sus posibles movimientos (8)
            #print i,j
            actual = board[i][j]

            if actual == player_id:
                # ARRIBA
                if i > 0:
                    pos_actual = i - 1
                    while pos_actual > -1:
                        sig_ficha = board[pos_actual][j]

                        if sig_ficha < 1:
                            if pos_actual < i-1:
                                #print 'hay tiro arriba'
                                movs.append((pos_actual, j))
                            pos_actual = -1
                        elif sig_ficha == oponente:
                            pos_actual = pos_actual - 1
                        else:
                            #print 'fichas del mismo en {}{}'.format(i, pos_actual)
                            pos_actual = -1

                #ABAJO
                if i < 7:
                    pos_actual = i + 1
                    while pos_actual < 8:
                        sig_ficha = board[pos_actual][j]

                        if sig_ficha < 1:
                            if pos_actual > i+1:
                                #print 'hay tiro abajo'
                                movs.append((pos_actual, j))
                            pos_actual = 8
                        elif sig_ficha == oponente:
                            pos_actual = pos_actual + 1
                        else:
                            #print 'abajo igual'
                            pos_actual = 8

                # DIAGONAL ARRIBA-IZQUIERDA
                if i > 0 and j > 0:
                    fila = i - 1
                    columna = j - 1
                    while fila > -1 and columna >= 0:
                        sig_ficha = board[fila][columna]

                        if sig_ficha < 1:
                            if fila < i-1:
                                #print 'hay tiro dARI'
                                movs.append((fila, columna))
                            fila = -1
                        elif sig_ficha == oponente:
                            fila = fila - 1
                            columna = columna - 1
                        else:
                            #print 'DAI- igual'
                            fila = -1

                # DIAGONAL ARRIBA-DERECHA
                if i > 0 and j < 7:
                    fila = i - 1
                    columna = j + 1
                    while fila > -1 and columna < 8:
                        sig_ficha = board[fila][columna]

                        if sig_ficha < 1:
                            if fila < i-1 and columna > j+1:
                                #print 'hay tiro dARD'
                                movs.append((fila, columna))
                            fila = -1
                        elif sig_ficha == oponente:
                            fila = fila - 1
                            columna = columna + 1
                        else:
                            #print 'DAD- igual'
                            fila = -1

                #DIAGONAL ABAJO-IZQUIERDA
                if i < 7 and j:
                    fila = i + 1
                    columna = j - 1
                    while fila < 8 and columna > -1:
                        sig_ficha = board[fila][columna]

                        if sig_ficha < 1:
                            if fila > i+1 and columna < j-1:
                                #print 'hay tiro dABI'
                                movs.append((fila, columna))
                            columna = -1
                        elif sig_ficha == oponente:
                            fila = fila + 1
                            columna = columna - 1
                        else:
                            #print 'DAbI- igual'
                            columna = -1
                #DIAGONAL ABAJO-DERECHA
                if i < 7 and j < 7:
                    fila = i + 1
                    columna = j + 1
                    while fila < 8 and columna < 8:
                        sig_ficha = board[fila][columna]

                        if sig_ficha < 1:
                            if fila > i+1:
                                #print 'hay tiro dAbD'
                                movs.append((fila, columna))
                            fila = 8
                        elif sig_ficha == oponente:
                            fila = fila + 1
                            columna = columna + 1
                        else:
                            #print 'DAbD- igual'
                            fila = 8

                #IZQUIERDA
                if j > 0:
                    columna = j - 1
                    while columna > -1:
                        sig_ficha = board[i][columna]

                        if sig_ficha < 1:
                            movs.append((i, columna))
                            if columna < j-1:
                                pass
                                #print 'hay tiro izq'
                               
                            columna = -1
                        elif sig_ficha == oponente:
                            columna = columna - 1
                        else:
                            columna = -1

                #DERECHA
                if j < 7:
                    columna = j + 1
                    while columna < 8:
                        sig_ficha = board[i][columna]

                        if sig_ficha < 1:
                            if columna > j+1:
                                #print 'hay tiro der'
                                movs.append((i, columna))
                            columna = 8
                        elif sig_ficha == oponente:
                           # print columna
                            columna = columna + 1
                        else:
                            columna = 8


    #print 'YA TERMINADO'
    return movs   

def convert_to_square(board):
    tablero = []
    for i in range(8):
        tablero.append(board[0:8])
        del board[0:8]
    return tablero


def minimax(state, turn, alpha, beta):
    #revisar si el juego ya esta finalizado
    if 0 not in state:
        pass
    pass

def min_play():
    pass

def max_play():
    pass
"""
gtt = convert_to_square(list(INICIAL))
#print INICIAL
#gtt[2][3] = 5
#gtt[3][2] = 5
#gtt[4][5] = 5
#gtt[5][4] = 5
for el in gtt:
    print el, '\n'

alg = get_possible_moves(INICIAL, 1)
print alg
print alg[0][0]*8 + alg[0][1]
"""
TID = 12
#192.168.1.111 samuel
s = socketIO_client.SocketIO('192.168.0.100', 3000)
s.connect()
s.emit('signin', {'user_name': "chiroy", 'tournament_id': TID, 'user_role': 'player'})

def onok():
    print 'exito en el signin'

def elready(data):
    t2 = data['board'][:]
    pos_tiros = get_possible_moves(data['board'], data['player_turn_id'])
    #print pos_tiros
    if len(pos_tiros) < 1:
        print 'no hay tiros validos'
        print data['player_turn_id']
        print t2
        raw_input('seguir\n')
        tiro = random.randint(0, 63)
    else:
        rand = random.randint(0, len(pos_tiros)-1)
        tiro = pos_tiros[rand][0]*8 + pos_tiros[rand][1]
    s.emit('play', {'tournament_id': TID, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id'], 'movement': tiro})
    #print tiro
    #print data

def elfinish(data):
    s.emit('player_ready', {'tournament_id': TID, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id']})
    print 'terminado ', data['game_id']


s.on('ok_signin', onok)
s.on('ready', elready)
s.on('finish', elfinish)

s.wait()


