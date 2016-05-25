#!/usr/bin/env python
import os
import upload2qiniu
cmd = 'ls ./chapter'
output = open('./all.md', 'w+')
filelist = os.popen(cmd).readlines()
for i in filelist:
    f = open("./chapter/%s" % i.strip('\n'))
    for j in f.readlines():
        output.write(j)
    f.close()
cmd = 'ls ./imgs'
filelist = os.popen(cmd).readlines()
for i in filelist:
    imgname = i.strip('\n')
    imgpath = "./imgs/%s" %imgname
    print imgname,imgpath
    upload2qiniu.putimg(imgname,imgpath)
