#! /usr/bin/env python3
import sys
arg = sys.argv[1:] # [1:] это: Возьми элементы списка начиная с индекса 1 и до конца
arg.reverse()
for i in arg:
    print(i)


