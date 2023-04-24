#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = 0x6c
addr = 0x5f6e
table = 0x4000 * bank + (addr % 0x4000)

for x in range(31):
    ptr = table + x * 5
    bank = file[ptr + 0]
    addr1 = file[ptr + 1] | file[ptr + 2] << 8
    addr2 = addr1 + 0x400
    addr3 = file[ptr + 3] | file[ptr + 4] << 8
    print("%02x:%04x Gfx_@" % (bank, addr1))
    print("%02x:%04x .image:400" % (bank, addr1))
    print("%02x:%04x Gfx_@" % (bank, addr2))
    print("%02x:%04x .image:80" % (bank, addr2))
    print("%02x:%04x Pal_@" % (bank, addr3))
    print("%02x:%04x .data:8:8" % (bank, addr3))
