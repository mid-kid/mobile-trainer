#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = 0x72
addr = 0x5035
table = bank * 0x4000 + addr - 0x4000

for x in range(23 + 44):
    pos = table + x * 2
    ptr = file[pos + 0] | file[pos + 1] << 8

    print("%02x:%04x Data_@" % (bank, ptr))
    print("%02x:%04x .data:3" % (bank, ptr))

    pos = bank * 0x4000 + ptr + 3 - 0x4000
    string1 = pos
    while file[pos] != 0:
        pos += 1
    pos += 1
    string1_len = pos - string1

    string2 = pos
    while file[pos] != 0:
        pos += 1
    pos += 1
    string2_len = pos - string2

    print("%02x:%04x .text:%x" % (bank, string1 % 0x4000 + 0x4000, string1_len))
    print("%02x:%04x .text:%x" % (bank, string2 % 0x4000 + 0x4000, string2_len))
