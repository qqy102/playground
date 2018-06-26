#!/usr/bin/env python

import os

def walkdir(dir):
    for dirpath, dirs, files in os.walk(dir):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            print fname
            #with open(fname) as myfile:
            #    print(myfile.read())

if __name__ == '__main__':
    dir = "."
    walkdir(dir)
