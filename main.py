#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket_creation
def main():
    try:
        socket_creation.create_listen_socket('::1', 33426)
    except Exception as err:
        print(f'{err}', file=sys.stderr)
        exit(1)

if __name__ == '__main__':
    main()