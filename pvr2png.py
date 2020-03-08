#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.ElementTree as ET

SUFFIX = ".pvr.ccz"

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

def tree_to_dict(tree):
    for index,item in enumerate(tree):
        if item.tag =='key':
            if tree[index+1].tag == 'string':
                global SUFFIX
                # .pvr.ccz 替换为 .png
                if endWith(tree[index+1].text, SUFFIX):
                    tree[index+1].text = tree[index+1].text.replace(SUFFIX, '.png')
            elif tree[index+1].tag == 'true':
                pass
            elif tree[index+1].tag == 'false':
                pass
            elif  tree[index+1].tag == "integer":
                pass
            elif  tree[index+1].tag == "array":
                pass
            elif tree[index+1].tag == 'dict':
                k = item.text
                if k != 'frames' and k != 'metadata':
                    t = tree[index].text
                    # 没有png后缀进行添加
                    if not endWith(t, '.png'):
                        tree[index].text = t + '.png'
                    print(tree[index].text)
                tree_to_dict(tree[index+1])

def readXml(plist_filename):
    tree = ET.parse(plist_filename)
    root = tree.getroot()
    tree_to_dict(root[0])
    # 保存
    tree.write(plist_filename, encoding="UTF-8")

def pvrToPng (_path,_OutPath):
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
                plistName = newFileName + ".plist"
                cmd = GetTexturePackerPath() + os.path.join(dirpath,filename) + " --data " + plistName + " --sheet " + outFileName + " --opt RGBA8888" + " --allow-free-size --algorithm Basic --no-trim --dither-fs --max-size 4096"
                ret = os.system(cmd)
                if ret == 0:
                    f = os.path.join(dirpath,filename)
                    os.remove(f) 
                    readXml(os.path.join(OutPath, plistName))      
    #os.remove("pvr2png.plist")
    print "pvrToPng"

def main():
    if len(sys.argv) < 2:
        print("usage : python pvr2png.py [source Path] [suffix] [OutPath:option]")
    else:
        #SUFFIX = sys.argv[2]
        global SUFFIX
        OutPath = './'
        if len(sys.argv) == 4:
            OutPath = sys.argv[3]
        if SUFFIX[0] != '.':
            SUFFIX = "." + SUFFIX
        pvrToPng(sys.argv[1],OutPath)

if __name__ == '__main__':
    main()
    #readXml("D:\\tmp\\com.xxqp.dz\\assets\\YbMj_Res\\YbMj_MobileRes\\PicRes-cp\\Ybmj_M_PokerValue.plist")