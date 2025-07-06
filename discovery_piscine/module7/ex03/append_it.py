#! /usr/bin/env python3
import sys
import re
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
res = []
arg = sys.argv[1:]
for i in range(len(arg)):
    if (re.findall(f"ism", arg[i], re.IGNORECASE)):
        continue
    else:
        res.append(arg[i] + "ism")
print("\n".join(res))
        