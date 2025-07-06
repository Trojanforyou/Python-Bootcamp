#! /usr/bin/env python3
import sys
import re
if (len(sys.argv) < 3):
    print("none")
    sys.exit(1)
first = sys.argv[1]
second = sys.argv[2]
res = re.findall(rf'{first}',second , re.IGNORECASE)
print(len(res))