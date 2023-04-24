#!/bin/sh

bank="$1"
addr="$2"
prefix="${3:-Call}"

sed -i -e 's/^; INSERT$/'"$1:$2 ${prefix}_@"'\n; INSERT/' baserom.sym
