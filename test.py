import random
import socketIO_client

#s = socketIO_client.SocketIO('10.226.186.253', 3000)
s = socketIO_client.SocketIO('192.168.1.111', 3000)
s.connect()
s.emit('signin', {'user_name': "el-negro-de-whatsapp", 'tournament_id': 12, 'user_role': 'player'})

def onok():
    print 'exito en el signin'

def elready(data):
    tablero = []
    #tiro = input('casilla de tiro')
    for i in range(8):
        tablero.append(data['board'][0:8])
    tiro = random.randint(0,63)
    s.emit('play', {'tournament_id': 12, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id'], 'movement': tiro})
    #print data

def elfinish(data):
    s.emit('player_ready', {'tournament_id': 12, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id']})
    print 'terminado ', data['game_id']

def revisar_valido(board, my_id):
    #hacer algo aqui
    for i in range(8):
        for j in range(8):
            pass


s.on('ok_signin', onok)
s.on('ready', elready)
s.on('finish', elfinish)

s.wait()