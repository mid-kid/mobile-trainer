#!/usr/bin/env python3

file = open("baserom.gbc", "rb").read()

bank = 0xf
addr = 0x4011
size = 0x22

table = 0x4000 * bank + addr - 0x4000

for x in range(size // 2):
    ptr = file[table + x * 2] | (file[table + x * 2 + 1] << 8)
    ptr += 0x4000 * bank - 0x4000

    tmp = ptr
    while file[tmp] != 0:
        tmp += 1

    len = tmp - ptr + 1
    ptr = (ptr % 0x4000) + 0x4000
    print("%02x:%04x String_0%02x_%04x" % (bank, ptr, bank, ptr))
    print("%02x:%04x .text:%x" % (bank, ptr, len))
