#!/bin/sh
./mgbdis/mgbdis.py --overwrite \
    --ld_c ldh_c \
    --print-hex \
    "$@" baserom.gbc
