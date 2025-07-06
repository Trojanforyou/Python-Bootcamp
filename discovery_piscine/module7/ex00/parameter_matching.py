#! /usr/bin/env python3
import re
import sys
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
arg = sys.argv[1]
user = input("What was the parameter? ")
if (re.findall(fr'{arg}', user, re.IGNORECASE)):
    print("Good job!")
else:
    print("Nope, sorry...")





