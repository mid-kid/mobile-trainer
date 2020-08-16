#!/usr/bin/env python3

file = open("baserom.gbc", "rb").read()

banks = len(file) // 0x4000

for bank in range(banks):
    offset = 0x4000
    while offset > 0:
        if file[bank * 0x4000 + offset - 1] != 0:
            break
        offset -= 1
    length = 0x4000 - offset
    if bank != 0:
        offset += 0x4000
    print("%02x:%04x .data:%04x" % (bank, offset, length))
