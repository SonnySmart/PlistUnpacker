#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

SUFFIX = ".plist"

def GetTexturePackerPath():
	if(os.name == 'posix'):
		return '/usr/local/bin/TexturePacker '
	else:
		return 'TexturePacker.exe '

def endWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def plistUnpackerToUnity(_path,_OutPath):
    OutPath = _OutPath
    for(dirpath, dirnames, filenames) in os.walk(_path):
        for filename in filenames:
            if filename.endswith(SUFFIX):
                basename = os.path.basename(filename)
                newFileName = basename[0:basename.find(SUFFIX)]
                if not os.path.isabs(_OutPath):
                    OutPath = os.path.join(dirpath,_OutPath)
                # deltaPath = dirpath
                if not os.path.exists(OutPath):
                    os.makedirs(OutPath)
                outFileName = os.path.join(OutPath,newFileName + ".png")
                outConfigName = os.path.join(OutPath,newFileName + ".txt")
                plistName = os.path.join(dirpath,filename)
                plistDir = os.path.join(dirpath,newFileName)
                #解包plist
                cmd = 'python plistUnpacker.py %s' % (plistName)
                print(cmd)
                ret = os.system(cmd)
                ret = -1
                #解包完成删除plist png 留下文件夹
                if ret == 0:
                    #os.remove(plistName) 
                    #os.remove(outFileName)
                    #%TPPath% %%i --sheet %TexturePath%\%%~ni.png --data %TexturePath%\%%~ni.tpsheet --no-trim --max-size 1024 --format unity-texture2d --size-constraints POT
                    cmd = '%s %s --sheet %s --data %s --no-trim --max-size 4096 --format unity --size-constraints POT' % (
                        GetTexturePackerPath(),
                        plistDir,
                        outFileName,
                        outConfigName
                    )
                    ret = os.system(cmd)
                    pass

def main():
    if len(sys.argv) < 2:
        print("usage : python plistUnpackerToUnity.py [source Path] [OutPath:option]")
    else:
        global SUFFIX
        OutPath = './'
        if len(sys.argv) == 4:
            OutPath = sys.argv[3]
        if SUFFIX[0] != '.':
            SUFFIX = "." + SUFFIX
        plistUnpackerToUnity(sys.argv[1],OutPath)

if __name__ == '__main__':
    main()