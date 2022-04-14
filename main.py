#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket_creation
from utils import printd, DEBUG
import argparse
from ipaddress import ip_address


def port_ranges(s):
    try:
        x, y = map(int, s.split(','))
        if(x >= y):
            raise ValueError
        return x, y
    except:
        raise argparse.ArgumentTypeError("ports ranges must be x,y")


def parse_args():
    parser = argparse.ArgumentParser(
        description='créer des sockets en écoute, peut être utilisé pour tester des règles de par-feu')
    parser.add_argument('-p', '--port', type=int,
                        nargs='+', help='port(s) à écouter', required=False)
    parser.add_argument('-t', '--type', type=str,
                        choices=['tcp', 'udp', 'raw'], help='type de socket', required=False, default='tcp')
    # parser.add_argument('-s', '--setsockopt', type=int,
    #                     nargs='+', help='option(s) à appliquer', required=False)
    parser.add_argument('-i', '--ip', type=ip_address,
                        help='adresse IP à écouter', required=True)
    parser.add_argument('-d', '--debug', action='store_true',
                        help='afficher les messages de debug', required=False)
    parser.add_argument(
        '-r', '--range', type=port_ranges, nargs='+', help="interval de port à écouter", required=False)
    args = parser.parse_args()
    if args.port == None and args.range == None:
        parser.error("port ou range requis")
    return args


def main():
    parse_args()
    # socket_list = socket_creation.create_all_socket('::1', (10, 20))
    # socket_creation.close_sockets(socket_list)


if __name__ == '__main__':
    main()
