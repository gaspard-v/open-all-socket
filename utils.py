# -*- coding: utf-8 -*-
DEBUG = True

def printd(msg: str, *args) -> None:
    if DEBUG:
        print(msg, *args)