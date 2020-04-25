#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from pkm2png import pkm2png

SUFFIX = ".pkm"

def _pkm2png(_path,_OutPath):
	my_pkm = open(_path, 'r').read()
	my_pkm_img = pkm2png.pkm2png(gen=5, data=my_pkm)
	with open(_OutPath, 'w') as f:
	    f.write(my_pkm_img)

def main():
    if len(sys.argv) < 2:
        print("usage : python pkm2png.py [source Path] [suffix] [OutPath:option]")
    else:
        #SUFFIX = sys.argv[2]
        global SUFFIX
        OutPath = './'
        if len(sys.argv) == 4:
            OutPath = sys.argv[3]
        if SUFFIX[0] != '.':
            SUFFIX = "." + SUFFIX
        _pkm2png(sys.argv[1],OutPath)

if __name__ == '__main__':
    main()