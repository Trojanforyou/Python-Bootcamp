#! /usr/bin/env python3
import sys
if (len(sys.argv) < 2):
    print("none")
    sys.exit(1)
def enlarge(string):
    while (len(sys.argv) < 8):
        string += "Z"
    return (string)

def shrink(string):
    if (len(sys.argv) > 8):
        return(string[:8])
def main():
    shrink()
    enlarge()
if (__name__ =="__main__"):
    main()
