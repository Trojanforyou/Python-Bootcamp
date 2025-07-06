#! /usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
arg = sys.argv[1:]
print("parameters :", len(arg))
for i in arg:
    print(f"{i}: {len(i)}")