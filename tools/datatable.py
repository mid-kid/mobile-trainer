#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = int(argv[1], 16)
addr = int(argv[2], 16)
size = int(argv[3], 16)

table = 0x4000 * bank + addr - 0x4000

for x in range((size // 2) - 1):
    ptr1 = file[table + x * 2] | (file[table + x * 2 + 1] << 8)
    ptr1 += 0x4000 * bank - 0x4000

    ptr2 = file[table + (x + 1) * 2] | (file[table + (x + 1) * 2 + 1] << 8)
    ptr2 += 0x4000 * bank - 0x4000

    len = ptr2 - ptr1
    ptr = (ptr1 % 0x4000) + 0x4000
    print("%02x:%04x Data_0%02x_%04x" % (bank, ptr, bank, ptr))
    print("%02x:%04x .data:%x" % (bank, ptr, len))
