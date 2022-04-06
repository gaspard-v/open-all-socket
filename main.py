#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket_creation
def main():
    socket_creation.create_socket(1, 2, (socket_creation.TCP))

if __name__ == '__main__':
    main()