#!/bin/sh

bank="$1"
addr="$2"
prefix="${3:-Data}_"

sed -i -e 's/^; INSERT$/'"$1:$2 ${prefix}0${bank}_$addr"'\n; INSERT/' baserom.sym
