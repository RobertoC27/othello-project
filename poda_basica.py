import random
import time
import socketIO_client

TID = 12
SAMUEL = '192.168.1.111'
LOCAL = '192.168.43.179'


INICIAL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SEGUNDO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BASE_HASH = hash(''.join(str(e) for e in INICIAL))
MOVS_INICIALES = [19, 26, 37, 44]

MASINF = 5000
MENINF = -5000

def convert_to_square(board):
    tablero = []
    for i in range(8):
        tablero.append(board[0:8])
        del board[0:8]
    return tablero

def get_possible_moves(board, player_id):
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    #revisar si el tablero es el inicial


    movs = []

    for posicion in range(len(board)):
        pieza = board[posicion]
        if pieza == player_id:
            #print posicion
            #print board
            #print len(board)
            #arriba
            if posicion > 7: #la primera fila no se revisa para arriba
                pos_actual = posicion - 8

                while pos_actual > -1:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1: # es un espacio vacio
                        if pos_actual < posicion-8:
                            movs.append(pos_actual)
                        pos_actual = -1
                    elif sig_ficha == oponente:
                        pos_actual -= 8
                    else:
                        pos_actual = -1


            # diagonal arriba izquierda
            if posicion > 7 and posicion%8 > 0: # el modulo nos dice posicion en la fila
                pos_actual = posicion - 9
                fila = pos_actual/8
                columna = pos_actual%8
                while fila > -1 and columna >= 0:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual < posicion-9:
                            movs.append(pos_actual)
                        fila = -1
                    elif sig_ficha == oponente:
                        fila = fila - 1
                        columna = columna - 1
                        pos_actual = pos_actual -9
                    else:
                        fila = -1


            # diagonal arriba derecha
            if posicion > 7 and posicion%8 < 7:
                pos_actual = posicion -7
                fila = pos_actual/8
                columna = pos_actual%8
                while fila > -1 and columna < 8:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual < posicion-7:
                            movs.append(pos_actual)
                        fila = -1
                    elif sig_ficha == oponente:
                        fila = fila - 1
                        columna = columna + 1
                        pos_actual = pos_actual - 7
                    else:
                        fila = -1

            # izquierda
            if posicion%8 > 0:
                pos_actual = posicion - 1
                stopper = posicion - posicion%8
                while pos_actual > stopper-1:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual < posicion-1:
                            movs.append(pos_actual)
                        pos_actual = stopper-1
                    elif sig_ficha == oponente:
                        pos_actual -= 1
                    else:
                        pos_actual = stopper-1

            #derecha
            if posicion%8 < 7:
                #print posicion
                pos_actual = posicion + 1
                stopper = posicion + (8 - (posicion%8))
                while pos_actual < stopper:
                    #print pos_actual
                    #print '--'
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual > posicion+1:
                            movs.append(pos_actual)
                        pos_actual = stopper+1
                    elif sig_ficha == oponente:
                        pos_actual += 1
                    else:
                        pos_actual = stopper+1

            #abajo
            if posicion/8 < 7:
                pos_actual = posicion + 8
                while pos_actual < 64:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual > posicion+8:
                            movs.append(pos_actual)
                        pos_actual = 64
                    elif sig_ficha == oponente:
                        pos_actual += 8
                    else:
                        pos_actual = 64

            # diagonal abajo izquierda
            if posicion/8 < 7 and posicion%8 > 0:
                pos_actual = posicion + 7
                fila = pos_actual/8
                columna = pos_actual%8
                while fila < 8 and columna > -1:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual > posicion+7:
                            movs.append(pos_actual)
                        columna = -1
                    elif sig_ficha == oponente:
                        fila = fila + 1
                        columna = columna - 1
                        pos_actual = pos_actual + 7
                    else:
                        columna = -1


            # diagonal abajo derecha
            if posicion/8 < 7 and posicion%8 < 7:
                pos_actual = posicion + 9
                fila = pos_actual/8
                columna = pos_actual%8
                while fila < 8 and columna < 8:
                    sig_ficha = board[pos_actual]
                    if sig_ficha < 1:
                        if pos_actual > posicion+9:
                            movs.append(pos_actual)
                        fila = 8
                    elif sig_ficha == oponente:
                        fila = fila + 1
                        columna = columna + 1
                        pos_actual = pos_actual + 9
                    else:
                        #print 'DAbD- igual'
                        fila = 8



    return list(set(movs))
def minimax2(board, player_id, tipo, alpha, current_depth, beta):
    """
    :param board: array que representa el tablero
    :param tipo: booleano true->max; false->min
    :param alpha: depth max a revisar del arbol
    :param beta: valor encontrado en los hermanos
    """
    #revisar si el juego ya esta finalizado
    if 0 not in board:
        return board_score(board, player_id)
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    n_board = board[:]

    # ya tengo el maximo nivel revisado
    if current_depth == alpha:
        return board_score(board, player_id)
    # quiero maximizar el score del siguiente turno
    if tipo:
        best_score = MENINF
        ps_moves = get_possible_moves(n_board, player_id)
        best_move = 0
        for move in ps_moves:
            #aplicar las heuristicas de control para el tablero actual
            n_board = apply_move(n_board, move, player_id)
            new_score = minimax2(n_board,oponente,False,alpha,current_depth+1,beta)
            if new_score > best_score:
                best_score = new_score
                best_move = move
        return best_score
    # quiero minimizar el score del siguiente turno
    else:
        best_score = MASINF
        best_move = 0
        ps_moves = get_possible_moves(n_board, player_id)
        for move in ps_moves:
            n_board = apply_move(n_board, move, player_id)
            best_score = min(best_score, minimax2(n_board, oponente, True, alpha, current_depth+1, beta))
        

def num_fichas(board, player_id):
    """
    devuelve el numero de fichas de un jugador
    """
    total = 0
    for pieza in board:
        if pieza == player_id:
            total += 1
    return total

def esquinas_capturadas(board, player_id):
    """
    devuelve cuantas de las esquinas del tablero
    el jugador tiene en su poder
    """
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    total = 0
    total2 = 0
    if board[0] == player_id:
        total += 1
    elif board[0] == oponente:
        total2 += 1
    if board[7] == player_id:
        total += 1
    elif board[7] == oponente:
        total2 += 1
    if board[56] == player_id:
        total += 1
    elif board[56] == oponente:
        total2 += 1
    if board[63] == player_id:
        total += 1
    elif board[63] == oponente:
        total2 += 1
    return total, total2

def min_play(board, player_id, curr_depth, max_depht, best_max, best_min):
    """
    encuentra la mejor jugada con el tablero actual para el jugador
    que quiere minimizar el score de su oponente
    :param board: array del tablero
    :param player_id: id del jugador que va a maximizar
    :param curr_depth: nivel de recursion actual
    :param max_depth: nivel maximo de recursion
    """
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    best_score = MASINF
    pos_moves = get_possible_moves(board, player_id)
    best_move = 0
    for move in pos_moves:
        new_board = apply_move(board, move, player_id)
        results = minimax(new_board, oponente, False, curr_depth+1, max_depht, best_max, best_min)
        best_score = results[0]
        best_max = results[1]
        best_min = results[2]
        if best_score < best_min:
            best_move = move
            best_min = best_score
        if best_min < best_max:
            break
    if curr_depth < 1:
        return best_move
    else:
        return best_score, best_max, best_min

def max_play(board, player_id, curr_depth, max_depht, best_max, best_min):
    """
    encuentra la mejor jugada con el tablero actual para el jugador
    que quiere maximizar el score de su oponente
    :param board: array del tablero
    :param player_id: id del jugador que va a maximizar
    :param curr_depth: nivel de recursion actual
    :param max_depth: nivel maximo de recursion
    """
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    best_score = MENINF
    pos_moves = get_possible_moves(board, player_id)
    best_move = 0
    for move in pos_moves:
        new_board = apply_move(board, move, player_id)
        results = minimax(new_board, oponente, False, curr_depth+1, max_depht, best_max, best_min)
        best_score = results[0]
        best_max = results[1]
        best_min = results[2]
        #new_score = new_score + heuristicas(new_board, player_id)
        if best_score > best_max:
            best_move = move
            best_max = best_score
        if best_min < best_max:
            break
    if curr_depth < 1:
        return best_move
    else:
        return best_score, best_max, best_min



def minimax(board, player_id, jugada, curr_depth, max_depht, best_max=MENINF, best_min=MASINF):
    """
    algoritmo de IA
    """
    if 0 not in board: # juego terminado
        return board_score(board, player_id), best_max, best_min

    if curr_depth == max_depht: #maxima recursion alcanzada
        return  board_score(board, player_id), best_max, best_min

    if jugada:
        return max_play(board[:], player_id, curr_depth, max_depht, best_max, best_min)
    else:
        return min_play(board[:], player_id, curr_depth, max_depht, best_max, best_min)

def board_score(board, player_id):
    """
    funcion que pone calcula el punteo del tablero
    """
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    
    # numero de piezas en el tablero
    total = 0
    total2 = 0
    for pieza in board:
        if pieza == player_id:
            total += 1
        elif pieza == oponente:
            total2 +=1
    if total > total2:
        piezas = (100.0 * total)/float(total + total2)
    elif total2 > total:
        piezas = -(100.0 * total2)/float(total + total2)
    else:
        piezas = 0

    # mobilidad
    if (random.random()) > 0.6:
        mis_movs = len(get_possible_moves(board, player_id))
        sus_movs = len(get_possible_moves(board, oponente))
        if mis_movs > sus_movs:
            mobi = (100.0 * mis_movs)/float(mis_movs + sus_movs)
        elif sus_movs > mis_movs:
            mobi = -(100.0 * sus_movs)/float(mis_movs + sus_movs)
        else:
            mobi = 0
    else:
        mobi = 0

    # esquinas obtenidas
    total = 0
    total2 = 0
    if board[0] == player_id:
        total += 1
    elif board[0] == oponente:
        total2 += 1
    if board[7] == player_id:
        total += 1
    elif board[7] == oponente:
        total2 += 1
    if board[56] == player_id:
        total += 1
    elif board[56] == oponente:
        total2 += 1
    if board[63] == player_id:
        total += 1
    elif board[63] == oponente:
        total2 += 1
    esquinas = 25*(total - total2)

    if (random.random()) > 0.5:
        piezas = 0


    return piezas + mobi + esquinas


def apply_move(board, piece, player_id):
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1

    n_board = board[:]
    tiro = piece
    cont_arr = 0
    cont_aba = 0
    cont_izq = 0
    cont_der = 0
    cont_darrizq = 0
    cont_darrder = 0
    cont_dabaizq = 0
    cont_dabader = 0
    # revisar fichas hacia arriba
    n_board[tiro] = player_id
    if tiro > 7: #la primera fila no se revisa para arriba
        pos_actual = tiro - 8
        while pos_actual > -1:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1: # es un espacio vacio
                pos_actual = -1
                cont_arr = 0
            elif sig_ficha == oponente:
                cont_arr += 1
                pos_actual -= 8
            else:
                pos_actual = -1
        for i in range(cont_arr):
            n_board[tiro - 8*(i+1)] = player_id

    # diagonal arriba izquierda
    if tiro > 7 and tiro%8 > 0: # el modulo nos dice posicion en la fila
        pos_actual = tiro - 9
        while pos_actual%8 > 0:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 0
                cont_darrizq = 0
            elif sig_ficha == oponente:
                cont_darrizq += 1
                pos_actual -= 9
            else:
                pos_actual = 0
        for i in range(cont_darrizq):
            n_board[tiro - 9*(i+1)] = player_id

    # diagonal arriba derecha
    if tiro > 7 and tiro%8 < 7:
        pos_actual = tiro -7
        while pos_actual%8 < 7:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 7
                cont_darrder = 0
            elif sig_ficha == oponente:
                cont_darrder += 1
                pos_actual -= 7
            else:
                pos_actual = 7
        for i in range(cont_darrder):
            n_board[tiro - 7*(i+1)] = player_id

    # izquierda
    if tiro%8 > 0:
        pos_actual = tiro - 1
        while pos_actual%8 > 0:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 0
                cont_izq = 0
            elif sig_ficha == oponente:
                cont_izq += 1
                pos_actual -= 1
            else:
                pos_actual = 0
        for i in range(cont_izq):
            n_board[tiro - (i+1)] = player_id

    #derecha
    if tiro%8 < 7:
        pos_actual = tiro + 1
        while pos_actual%8 < 7:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 7
                cont_der = 0
            elif sig_ficha == oponente:
                cont_der += 1
                pos_actual += 1
            else:
                pos_actual = 7
        for i in range(cont_der):
            n_board[tiro + (i+1)] = player_id

    #abajo
    if tiro/8 < 7:
        pos_actual = tiro + 8
        while pos_actual < 56:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 56
                cont_aba = 0
            elif sig_ficha == oponente:
                cont_aba += 1
                pos_actual += 8
            else:
                pos_actual = 56
        for i in range(cont_aba):
            n_board[tiro + 8*(i+1)] = player_id

    # diagonal abajo izquierda
    if tiro/8 < 7 and tiro%8 > 0:
        pos_actual = tiro + 7
        while pos_actual%8 > 0 and pos_actual/8 < 7:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                pos_actual = 0
                cont_dabaizq = 0
            elif sig_ficha == oponente:
                cont_dabaizq += 1
                pos_actual += 7
            else:
                pos_actual = 0

        for i in range(cont_dabaizq):
            n_board[tiro + 7*(i+1)] = player_id

    # diagonal abajo derecha
    if tiro/8 < 7 and tiro%8 < 7:
        pos_actual = tiro + 9
        while pos_actual%8 < 7 and pos_actual/8 < 7:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                cont_dabader = 0
                pos_actual = 7
            elif sig_ficha == oponente:
                cont_dabader += 1
                pos_actual += 9
            else:
                pos_actual = 7

        for i in range(cont_dabader):
            n_board[tiro + 9*(i+1)] = player_id

    return n_board


s = socketIO_client.SocketIO(LOCAL, 3000)
s.connect()
s.emit('signin', {'user_name': "poda_bas", 'tournament_id': TID, 'user_role': 'player'})

def onok():
    """
    cuando el signing es exitoso para el torneo
    """
    print 'exito en el signin'

def elready(data):
    """
    funcion que manda el siguiente tiro
    """
    tiro_t = minimax(data['board'], data['player_turn_id'], True, 0, 7)
    s.emit('play', {'tournament_id': TID, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id'], 'movement': tiro_t})


def elfinish(data):
    """
    funcion que pone en espera para el siguiente juego
    """
    my_id = data['player_turn_id']
    g_id = data['game_id']
    if 'winner_turn_id' in data:
        if data['winner_turn_id'] == my_id:
            print 'has ganado'
        else:
            print 'has perdido'
    s.emit('player_ready', {'tournament_id': TID, 'player_turn_id': my_id, 'game_id': g_id})
    print 'terminado ', data['game_id']


s.on('ok_signin', onok)
s.on('ready', elready)
s.on('finish', elfinish)

s.wait()
