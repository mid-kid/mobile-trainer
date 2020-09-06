#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = int(argv[1], 16)
addr = int(argv[2], 16)

offs = 0x4000 * bank + addr - 0x4000
start = offs
while file[offs] != 0:
    offs += 1

len = offs - start + 1
ptr = (start % 0x4000) + 0x4000
print("%02x:%04x Comp_0%02x_%04x" % (bank, ptr, bank, ptr))
print("%02x:%04x .data:%x" % (bank, ptr, len))
