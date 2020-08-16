#!/usr/bin/env python3

import re
from sys import argv

for lineno, line in enumerate(open(argv[1])):
    match = re.search(r'\$([0-9a-f]{2,4})', line.split(";")[0])
    if not match:
        continue

    value = int(match.group(1), 16)

    if line.startswith("    ldh "):
        print("%d: $%02x" % (lineno + 1, value))
        continue

    if value < 0x100:
        # incredibly unlikely to be something in the header
        continue
    if value >= 0x2183 and value < 0x4000:
        # unused part of bank 0
        continue
    if value >= 0x8000 and value < 0xa000:
        # vram, used in a ton of ways depending on context
        continue
    if value >= 0xd000 and value < 0xe000:
        # switchable wram bank, hard to untangle
        continue
    if value == 0x4000:
        # rROMB0
        continue

    print("%d: $%04x" % (lineno + 1, value))

empty = 0
for lineno, line in enumerate(open(argv[1])):
    if line.endswith("\n"):
        line = line[:-1]

    if not line:
        empty += 1
        continue

    if empty >= 2:
        if line[0] == ' ':
            print("missing:", lineno + 1)
    empty = 0
