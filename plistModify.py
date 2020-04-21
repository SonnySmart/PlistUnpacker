#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.ElementTree as ET
import json

SUFFIX = ".plist"

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
                key = tree[index].text
                val = tree[index + 1].text
                if key == 'frame' or key == 'sourceColorRect':
                    # print(key + " " + val)
                    val = val.replace("{", "").replace("}", "")
                    array = val.split(",")
                    w = int(array[2]) + 2
                    h = int(array[3]) + 2
                    # s = ('{{{0},{1}},{{2},{3}}'.format(array[0], array[1], w, h))
                    s = "{{" + array[0] + "," + array[1] + "},{" + str(w) + "," + str(h) + "}}"
                    print(s)
                    tree[index + 1].text = s
                
            elif tree[index+1].tag == 'true':
                pass
            elif tree[index+1].tag == 'false':
                pass
            elif  tree[index+1].tag == "integer":
                pass
            elif  tree[index+1].tag == "array":
                pass
            elif tree[index+1].tag == 'dict':
                # k = item.text
                # if k == 'frame' or k == 'sourceColorRect':
                #     t = tree[index].text
                #     print(t)
                tree_to_dict(tree[index+1])

def readXml(plist_filename):
    tree = ET.parse(plist_filename)
    root = tree.getroot()
    tree_to_dict(root[0])
    # 保存
    tree.write(plist_filename, encoding="UTF-8")

def plistModify (_path,_OutPath):
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
                plistName = newFileName + ".plist"
                readXml(os.path.join(OutPath, plistName))

def main():
    if len(sys.argv) < 2:
        print("usage : python plistModify.py [source Path] [suffix] [OutPath:option]")
    else:
        #SUFFIX = sys.argv[2]
        global SUFFIX
        OutPath = './'
        if len(sys.argv) == 4:
            OutPath = sys.argv[3]
        if SUFFIX[0] != '.':
            SUFFIX = "." + SUFFIX
        plistModify(sys.argv[1],OutPath)

if __name__ == '__main__':
    #main()
    readXml("D:\\git\\Mahjong\\client\\game\\yule\\sparrowtwo\\res\\gameplist\\Ybmj_M_PokerValue.plist")