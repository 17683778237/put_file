from socket import *
from multiprocessing import  Process
user = {}
def enter(udp_socket,name,address):
    if name in user:udp_socket.sendto("fail".encode(),address)
    else:
        udp_socket.sendto('ok'.encode(),address)
        for item in user:udp_socket.sendto(f'欢迎{name}进入聊天室'.encode(),user[item])
        user[name] = address
        # print(user)
def chat(udp_socket, name,content):
    for item in user:
        if item != name:
            udp_socket.sendto(f'{name}:{content}'.encode(),user[item])

def eixt(udp_socket, name):
    del user[name]
    for item in user:
        udp_socket.sendto(f'{name}已退出聊天室'.encode(),user[item])

def handle(udp_socket):
    while True:
        # print('waitting to connect...')
        data,addr = udp_socket.recvfrom(128)
        temp = data.decode().split(' ',2)
        # print(f'客户端{addr}已连接')
        if temp[0] == "L":enter(udp_socket,temp[1],addr)
        elif temp[0] == "C":chat(udp_socket,temp[1],temp[2])
        elif temp[0] == "E":eixt(udp_socket,temp[1])

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 8888))
    p = Process(target=handle,args=(udp_socket,))
    p.start()
    while True:
        message = input("管理员消息:")
        if message == "quit":break
        data = f'C 管理员消息 {message}'
        udp_socket.sendto(data.encode(),('0.0.0.0', 8888))

if __name__ == '__main__':
    main()




