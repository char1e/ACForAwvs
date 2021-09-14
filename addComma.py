# -*- coding: utf-8 -*-
import sys
"""
Add Comma for Awvs
Created on Sun Mar 22 10:06:17 2020
AWVS上传多个目标的时候，要求必须为为csv文件，该脚本将IP输入文件
去除空行以及行末多余逗号
@author: rhaps
"""

import os
while(True):
    path = sys.argv[1]
    if os.path.exists(path):
        break
    else:
        print("cannot find file >_<  \n")
        path = input("Plz input the filepath again")
        
readFile = open(path,'r+')
writeFile = open('output_'+os.path.basename(path)+'.csv','w+')
flag = 1
while(True):
     line = readFile.readline()
     if not line:
         print("End\n")
         break
     else:
         if line == '\n':
             continue
         else:
             if (flag == 1):
                 flag = 0
             else:
                 writeFile.write('\n')
             print('processing '+line)
             line = line.rstrip('\n')
             line = line.rstrip(',')
             if not line.startswith('http'):
                 line01 = "http//" + line + ','
                 writeFile.write(line01)
                 line = "https//" + line + ','
             else:
                 line = line + ','
             writeFile.write(line)
print("create:output_"+os.path.basename(path)+'.csv')
readFile.close()
writeFile.close()


