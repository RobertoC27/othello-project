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




def apply_move(board, piece, player_id):
    if player_id == 1:
        oponente = 2
    else:
        oponente = 1
    n_board = board[:]
    #tiro = piece[0]*8 + piece[1]
    tiro = piece
    cont_arr = 0
    cont_aba = 0
    cont_izq = 0
    cont_der = 0
    cont_darrizq = 0
    cont_darrder = 0
    cont_dabaizq = 0
    cont_dabader = 0
    n_board[tiro] = player_id
    # revisar fichas hacia arriba
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
        while pos_actual%8 > 0:
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
        while pos_actual/8 < 7:
            sig_ficha = board[pos_actual]
            if sig_ficha < 1:
                cont_dabader = 0
                pos_actual = 56
            elif sig_ficha == oponente:
                cont_dabader += 1
                pos_actual += 9
            else:
                pos_actual = 56
        for i in range(cont_dabader):
            n_board[tiro + 9*(i+1)] = player_id

    return n_board




INICIAL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

t1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0, 2
, 2, 2, 2, 1, 1, 2, 0, 2, 2, 2, 1, 1, 1, 2]

t2 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2
, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

t3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 2
, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1]

t4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1
, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 1, 2]

t5 = [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 0, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1]

t6 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2]

var1 = t2
for l1 in convert_to_square(var1[:]):
        print l1
print '---'
print len(get_possible_moves(var1, 2))
for mv in get_possible_moves(var1, 2):
    print mv
    gt = apply_move(var1, mv, 1)
    for l1 in convert_to_square(gt):
        print l1
    print ''



[0, 0, 2, 2, 1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 0, 1, 1, 2, 1, 2, 0, 0, 0, 1, 1, 1, 2, 0, 2, 0, 0, 0
, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0]
41
