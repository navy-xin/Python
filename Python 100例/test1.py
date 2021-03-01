#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 18:51
#@Author : navy
#@File : test1.py
#@Software: PyCharm

import socket
import threading

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.send(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7891))

    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("请输入对方的port:"))

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()
