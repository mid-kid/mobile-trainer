#!/usr/bin/env python3

from sys import argv

file = open("baserom.gbc", "rb").read()

bank = int(argv[1], 16)
addr = int(argv[2], 16)
size = int(argv[3], 16)

table = 0x4000 * bank + addr - 0x4000

def read_u16(addr):
    r = file[addr] | (file[addr + 1] << 8)
    return r

def read_ptr(addr):
    addr = read_u16(addr)
    if addr >= 0x4000 and addr < 0x8000:
        addr += 0x4000 * bank - 0x4000
    return addr

for x in range(0, size // 2, 2):
    frameset = read_ptr(table + x * 2)
    anim = read_ptr(table + (x + 1) * 2)

    if frameset != 0:
        offs = 0
        while True:
            ptr = read_u16(frameset + offs * 2)
            if ptr < 0x4000 or ptr >= 0x8000:
                break
            offs += 1
        frames = offs

        ptr = (frameset % 0x4000) + 0x4000
        print("%02x:%04x SpriteFrameset_@" % (bank, ptr))
        print("%02x:%04x .ptrtable:%x:data" % (bank, ptr, frames * 2))

        for frame in range(frames):
            ptr = read_ptr(frameset + frame * 2)
            len = file[ptr]
            ptr = (ptr % 0x4000) + 0x4000
            print("%02x:%04x SpriteFrame_@" % (bank, ptr))
            print("%02x:%04x .data:1" % (bank, ptr))
            print("%02x:%04x .data:%x:4" % (bank, ptr + 1, len * 4))

    if anim != 0:
        len = file[anim]
        ptr = (anim % 0x4000) + 0x4000
        print("%02x:%04x SpriteAnim_@" % (bank, ptr))
        print("%02x:%04x .data:1" % (bank, ptr))
        print("%02x:%04x .data:%x:2" % (bank, ptr + 1, len * 2))
