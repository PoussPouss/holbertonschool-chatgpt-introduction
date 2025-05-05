#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("Aucun argument n'a été fourni.")
else:
    for i in range(len(sys.argv)):
        print(sys.argv[i])