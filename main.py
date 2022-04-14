#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket_creation
import utils
import argparse
from ipaddress import ip_address

port_dict = {
    'tcp': socket_creation.TCP,
    'udp': socket_creation.UDP,
    'raw': socket_creation.RAW
}


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
    parser.add_argument('--debug', action='store_true',
                        help='afficher les messages de debug', required=False)
    parser.add_argument('--no-close', action='store_true',
                        help='ne ferme pas les sockets à la fin du programme', required=False, default=False)
    parser.add_argument(
        '-r', '--range', type=port_ranges, nargs='+', help="interval de port à écouter", required=False)
    args = parser.parse_args()
    if args.port == None and args.range == None:
        parser.error("port ou range requis")
    return args


def append_socket(socket_list, port, ip, socket_type):
    try:
        socket_list.append(
            socket_creation.create_listen_socket(ip, port, socket_type))
    except Exception as err:
        print(f'unable to create socket on port {port}\
                \nError message: {err}\n', file=sys.stderr)


def main():
    args = parse_args()
    if(args.debug):
        utils.DEBUG = True
    socket_list = []

    if args.port != None:
        for port in args.port:
            append_socket(socket_list, port, str(
                args.ip), port_dict[args.type])

    if args.range != None:
        for port_range in args.range:
            port_min, port_max = port_range
            for port in range(port_min, port_max + 1):
                append_socket(socket_list, port, str(
                    args.ip), port_dict[args.type])

    socket_creation.display_input_sockets(socket_list)

    if(not args.no_close):
        socket_creation.close_sockets(socket_list)


if __name__ == '__main__':
    main()
