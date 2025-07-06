#! /usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
arr = []
for i in range(1, len(sys.argv)):
    for j in range(len(sys.argv[i])):
        if (sys.argv[i][j] == 'z'):
            arr.append('z')
if (len(arr) == 0):
    print("none")
else:
    print(''.join(arr))
            


