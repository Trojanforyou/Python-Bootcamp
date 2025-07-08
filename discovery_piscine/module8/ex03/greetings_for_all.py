#! /usr/bin/env python3
import sys
def greetings(name = "noble stranger."):
    if (isinstance(name, int)):
        print("Error! It was not a name. ")
    else:
        print(f"Hello, {name}")
greetings("Alexandra")
greetings("Wil")
greetings("42")
greetings()
