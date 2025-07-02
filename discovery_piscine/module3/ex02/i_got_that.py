#! /usr/bin/env python3
stop = "STOP"
user = input("What you gonna say? : ")
if (user == stop):
    exit()
else:
    while (input("I got that ! Anything else? : ") != stop):
        input("I got that ! Anything else? : ")
