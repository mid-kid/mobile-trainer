#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = int(argv[1], 16)
addr = int(argv[2], 16)
count = 1
if len(argv) > 3:
    count = int(argv[3], 0)

ptr = 0x4000 * bank + (addr % 0x4000)

for x in range(count):
    tmp = ptr
    while file[tmp] != 0:
        tmp += 1

    len = tmp - ptr + 1
    addr = ptr % 0x4000
    if bank != 0:
        addr += 0x4000
    print("%02x:%04x String_@" % (bank, addr))
    print("%02x:%04x .text:%x" % (bank, addr, len))
    ptr = tmp + 1
