# -*- coding: utf-8 -*-
DEBUG = False


def printd(msg: str, *args) -> None:
    if DEBUG:
        print(msg, *args)
