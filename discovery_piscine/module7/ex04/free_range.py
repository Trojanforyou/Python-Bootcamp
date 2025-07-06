#! /usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
arg1 = int(sys.argv[1])
arg2 =int(sys.argv[2])
if (arg1 < arg2):
    print(list(range(arg1, arg2 + 1)))
