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
    return s
