import socket
import threading
from src import gui
from src import gui_game as gg

server_ip = '127.0.0.1'
server_port = 51742
banned_letters_in_nickname = "`~!@#$%^&*()-=+[]{}\\|;:'\",<.>/? "
status = 0      # 0: before game start, 1: error, 2: game started, 3: end


def alert_connection_error():
    global status

    if status == 1:
        return
    gui.AlertConnectionErrorGui().show()
    status = 1


def select_nickname():
    global my_socket
    global status

    nickname = gui.ChooseNicknameGui(banned_letters=banned_letters_in_nickname).show()
    if not nickname:
        nickname = "$quit"
        status = 1
    try:
        my_socket.send(bytes(nickname, 'utf-8'))
    except ConnectionError:
        alert_connection_error()
        return
    return nickname


def select_room():
    global my_socket
    global status

    try:
        data = my_socket.recv(1024)
    except ConnectionError:
        alert_connection_error()
        return
    room_names = eval(data.decode('utf-8'))
    selected_room = gui.ChooseRoomGui(rooms=room_names).show()
    if not selected_room:
        selected_room = "$quit"
        status = 1
    try:
        my_socket.send(bytes(selected_room, 'utf-8'))
    except ConnectionError:
        alert_connection_error()
        return
    return selected_room


def receive(room, t):
    global my_socket
    global status

    while status == 0:
        try:
            data = my_socket.recv(1024)
        except ConnectionError:
            alert_connection_error()
            return
        if data.decode('utf-8') == "$gameStarted":
            status = 2
        elif data.decode('utf-8') == "$giveHead":
            room.set_head()
            t[0] = True
        elif data.decode('utf-8').split()[0] == "$setMembers":
            room.set_members(eval(' '.join(data.decode('utf-8').split()[1:])))
        else:
            room.add_chat(data.decode('utf-8'))


def receive_in_game(game):
    global my_socket
    global status

    while status == 2:
        try:
            data = my_socket.recv(1024)
        except ConnectionError:
            alert_connection_error()
            return
        code = data.decode('utf-8')
        if code.split()[0] == "$monsterInfo":
            info = eval(' '.join(code.split()[1:]))
            game.change_mob(info[0], int(info[1]))
        elif code == "$getInput":
            game.btn_show = True
            game.damage = -1
        elif code.split()[0] == "$Success" or code.split()[0] == "$Failed":
            game.damage = int(code.split()[1])
        elif code.split()[0] == "$card":
            card_list = eval(' '.join(code.split()[1:]))
            game.btn = card_list
        elif code.split()[0] == "$reward":
            reward_dict = eval(' '.join(code.split()[1:]))
            game.reward = reward_dict
        elif code == "$gameOver":
            status = 3
        else:
            gg.chatting_input(code)
        # print(code)


def connect():
    global my_socket
    global status

    nickname = select_nickname()
    if status == 1:
        return
    while True:
        status = 0
        room_name = select_room()
        if status == 1:
            return

        room = gui.RoomGui(room_name=room_name, client_nickname=nickname)
        t = [False]
        r = threading.Thread(target=receive, args=(room, t, ))
        r.start()
        while status == 0:
            tmp = room.show()
            if not tmp:
                status = 1
                return
            msg, com = tmp
            if msg:
                try:
                    my_socket.send(bytes(msg, 'utf-8'))
                except ConnectionError:
                    alert_connection_error()
                    return
            if com:
                try:
                    my_socket.send(bytes(com, 'utf-8'))
                except ConnectionError:
                    alert_connection_error()
                    return
                if com == "$leave":
                    status = 3
        room.quit()
        if not t[0]:
            my_socket.send(bytes("$tmp", 'utf-8'))
        r.join()
        if status == 3:
            continue

        game = gg.Game()
        rg = threading.Thread(target=receive_in_game, args=(game, ))
        rg.start()
        while status == 2:
            msg, com = game.show()
            if msg:
                try:
                    my_socket.send(bytes(msg, 'utf-8'))
                except ConnectionError:
                    alert_connection_error()
                    return
            if com:
                try:
                    my_socket.send(bytes(com, 'utf-8'))
                except ConnectionError:
                    alert_connection_error()
                    return

            if status == 1:
                return
        game.quit()
        rg.join()

        # print('receive start')
        try:
            data = my_socket.recv(1024)
        except ConnectionError:
            alert_connection_error()
            return
        # print(data)
        gui.FinalGui(result=eval(data.decode('utf-8'))).show()
        my_socket.send(bytes("$end", 'utf-8'))


server_address = (server_ip, server_port)

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.connect(server_address)
except ConnectionRefusedError:
    print("서버가 응답하지 않습니다.")
    quit()

connect()

my_socket.close()
