#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket_creation
from utils import printd
def main():
    def close_sockets(socket_list: list) -> None:
        for counter, socket in enumerate(socket_list):
            try:
                socket.close()
                printd(f'Socket {counter} closed')
            except:
                print(f'unable to close socket {counter}', file=sys.stderr)
    socket_list = []
    for port in range(1, 10):
        try:
            socket_list.append(socket_creation.create_listen_socket('::1', port))
            printd(f'Socket port {port} created')
        except Exception as err:
            print(f'unable to create socket on port {port}\
                   \nError message: {err}\n', file=sys.stderr)
    close_sockets(socket_list)


if __name__ == '__main__':
    main()