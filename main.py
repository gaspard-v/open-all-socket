#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket_creation
from utils import printd


def main():
    socket_list = socket_creation.create_all_socket('::1', (10, 20))

    socket_creation.close_sockets(socket_list)


if __name__ == '__main__':
    main()
