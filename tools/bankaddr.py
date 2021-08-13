#!/usr/bin/env python3

from sys import argv

pos = int(argv[1], 16)
bank = pos // 0x4000
addr = pos % 0x4000
if bank:
    addr += 0x4000
print("%02x:%04x" % (bank, addr))
