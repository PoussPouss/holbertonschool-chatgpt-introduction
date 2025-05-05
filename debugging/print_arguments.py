#!/usr/bin/python3
import sys

# Commencer à l'index 1 pour ignorer le nom du script (sys.argv[0])
for i in range(1, len(sys.argv)):
    print(sys.argv[i])