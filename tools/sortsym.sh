#!/bin/sh
sed -e 's/ \./ ~/' | LC_ALL=C sort | sed -e 's/ ~/ \./'
