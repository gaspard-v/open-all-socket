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

TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
RAW = socket.SOCK_RAW

def create_socket(ip, port, options: list[socket.SocketKind]):
    pass
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.bind((ip, port))
    # s.listen(1)
    # return s