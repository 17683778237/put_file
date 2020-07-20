from socket import *
from signal import *
import sys
from multiprocessing import Process
ADDR = ('127.0.0.1', 8888)

def login(udp_socket):
    while True:
        name = input("请输入用户名:")
        message = 'L '+name
        udp_socket.sendto(message.encode(),ADDR)
        data,addr = udp_socket.recvfrom(128)
        if data.decode() == "ok":print(f'您已进入聊天室'); return name
        else:print('用户已存在,请重新输入')

def recv(udp_socket):
    while True:
        data,addr = udp_socket.recvfrom(1024)
        if not data:break
        print(data.decode())
# signal(SIGCHLD,SIG_IGN)

def send(udp_socket,name):
    while True:
        try:
            content = input("")
        except :
            content = "exit"
        if content == "exit":udp_socket.sendto(f"E {name}".encode(),ADDR);sys.exit("您已退出聊天室")
        data = f"C {name} {content}"
        udp_socket.sendto(data.encode(),ADDR)

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    name = login(udp_socket)
    p = Process(target=recv,args=(udp_socket,))
    p.daemon = True
    p.start()
    send(udp_socket,name)

if __name__ == '__main__':
    main()
