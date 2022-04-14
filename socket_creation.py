# -*- coding: utf-8 -*-

# socket cheat sheet
# AF_INET       = IPv4
# AF_INET6      = IPv6
# SOCK_STREAM   = TCP
# SOCK_DGRAM    = UDP
# SOCK_RAW      = raw socket
# setsockopt
# https://pubs.opengroup.org/onlinepubs/000095399/functions/setsockopt.html

import socket
from typing import Union, List
from utils import printd
import sys
import select

TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
RAW = socket.SOCK_RAW


def create_listen_socket(ip: str,
                         port: int,
                         socket_type: socket.SocketKind = TCP,
                         socket_setsockopt: List[int] = [socket.SO_REUSEADDR]) -> socket.socket:
    def get_ip_type(ip: str = ip) -> tuple[socket.AddressFamily, str]:
        ip_type = socket.getaddrinfo(ip, None)
        address_family = ip_type[0][0]
        address = ip_type[0][4][0]
        return (address_family, address)
    address_family, address = get_ip_type()
    s = socket.socket(address_family, socket_type)
    for opt in socket_setsockopt:
        s.setsockopt(socket.SOL_SOCKET, opt, 1)
    s.bind((address, port))
    s.listen(1)
    s.setblocking(False)
    printd(f'Socket port {port} created')
    return s


def close_sockets(socket_list: List[socket.socket]) -> None:
    for socket in socket_list:
        address, port, *rest = socket.getsockname()
        try:
            socket.close()
            printd(f'Socket port {port} closed')
        except:
            print(f'unable to close socket port {port}', file=sys.stderr)


def create_all_socket(ip: str, port: Union[int, tuple[int, int]], *args) -> List[socket.socket]:
    sockets = []
    min, max = 0, 0
    if isinstance(port, int):
        min, max = port, port
    elif isinstance(port, tuple):
        min, max = port
    else:
        raise TypeError('port must be int or tuple')
    for port in range(min, max + 1):
        try:
            sockets.append(create_listen_socket(ip, port, *args))
        except Exception as err:
            print(f'unable to create socket on port {port}\
                        \nError message: {err}\n', file=sys.stderr)
    return sockets


def display_input_sockets(socket_list):
    while True:
        rlist, wlist, xlist = select.select(socket_list, [], [])
        for socket in rlist:
            connection, client_address = socket.accept()
            printd(f'connection from {client_address}')
            print(connection.recv(1024))
