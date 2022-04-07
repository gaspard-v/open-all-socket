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

def create_socket(ip: str, 
                  port: int, 
                  socket_type: Union[TCP, UDP, RAW] = TCP,
                  socket_setsockopt: List[int] = [socket.SO_REUSEADDR]) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket_type)
    for opt in socket_setsockopt:
        s.setsockopt(socket.SOL_SOCKET, opt, 1)
    s.bind((ip, port))
    s.listen(1)
    return s