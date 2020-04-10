import socket
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
addr = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
DISCONNECT_MESSAGE = '!DISCONNECT\n'

def handle_client(conn, addr):
    print(f'[New connection] {addr} connected.\n')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print('User Disconnected')
            print(f'[{addr}] {msg}')
        conn.send('You are connected'.encode(FORMAT))
    conn.close()
def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}\n')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active connections {threading.activeCount() - 1}')
print('SERVER is starting...\n')
start()

