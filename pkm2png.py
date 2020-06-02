#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from FileUtil import FileUtil

suffix_pkm = '.pkm'
suffix_png = '.png'
suffix_plist = '.plist'
cwd = os.getcwd()
exe = os.path.join(os.path.join(cwd, 'pkm2png'), 'etc1tool.exe')

def pkm2png(path):
    files = FileUtil.getAlllFilesPathOfCurrentDirectory(path)
    for f in files:
        if f.endswith(suffix_pkm):
            #print(f)
            pkm = f
            png = pkm.replace(suffix_pkm, suffix_png)
            #print(png)
            plist = pkm.replace(suffix_pkm, suffix_plist)
            #print(plist)
            #etc1tool.exe %%x --decode -o %%x.png
            command = '%s %s --decode -o %s' % (exe, pkm, png)
            print(command)
            os.system(command)
    pass

if __name__ == '__main__':
    pkm2png("D:\\tmp\\com.qqgame.hlddz")
    pass