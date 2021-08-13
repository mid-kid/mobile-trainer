#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = int(argv[1], 16)
addr = 0x4000
pos = bank * 0x4000 + (addr % 0x4000)

count = int(argv[2], 0)

def text(pos):
    tmp = pos
    while file[tmp] != 0:
        tmp += 1
    len = tmp - pos + 1
    addr = pos % 0x4000
    if bank != 0:
        addr += 0x4000
    print("%02x:%04x String_@" % (bank, addr))
    print("%02x:%04x .text:%x" % (bank, addr, len))
    return tmp + 1

for x in range(count):
    pos = text(pos)
    addr = pos % 0x4000
    if bank != 0:
        addr += 0x4000
    print("%02x:%04x Data_@" % (bank, addr))
    print("%02x:%04x .ptrtable:2" % (bank, addr))
    pos += 2
    pos = text(pos)
