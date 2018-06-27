#!/usr/bin/env python

import os
import sys
import argparse

CDImageName = 'CDImage'
cue = '.cue'
ape = '.ape'
flac = '.flac'
wav = '.wav'
audioExtList = [ape, cue, flac, wav]

jpg = '.jpg'
png = '.png'
picExtList = [jpg, png]


def walkdir(dir):
    for dirpath, dirs, files in os.walk(dir):
        CDImageDic = {}
        for filename in files:
            basename, ext = os.path.splitext(filename)
            if ext in audioExtList:
                if CDImageName in basename:
                    if basename not in CDImageDic: 
                        CDImageDic[basename] = []
                    CDImageDic[basename].append(ext)
                    #print basename, ext
            fname = os.path.join(dirpath, filename)
        print CDImageDic    

            #with open(fname) as myfile:
            #    print(myfile.read())

def createArgParser():
    parser = argparse.ArgumentParser(description='QQ music file info grabber')
    parser.add_argument('inputDir', help='input Dir')
    return parser

if __name__ == '__main__':
    dir = "."
    argParser = createArgParser()
    parsedArgs = argParser.parse_args(sys.argv[1:])
    if os.path.exists(parsedArgs.inputDir):
        dir = parsedArgs.inputDir
        walkdir(dir)
    else:
        print 'No Input Dir Assigned'
