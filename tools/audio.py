#!/usr/bin/env python3

file = open("baserom.gbc", "rb").read()

table = 0x04 * 0x4000 + 0x5515 - 0x4000

for x in range(70):
    cur = table + 8 * x
    addr = file[cur + 0] | (file[cur + 1] << 8)
    bank = file[cur + 2] | (file[cur + 3] << 8)
    print("%02x:%04x Audio_%03x_%04x" % (bank, addr, bank, addr))
