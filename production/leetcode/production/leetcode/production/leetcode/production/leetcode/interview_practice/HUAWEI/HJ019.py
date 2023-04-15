# -*- coding: utf-8 -*-
# @Time    : 2022-09-05 8:47 p.m.
# @Author  : qkzhong
# @FileName: HJ019.py
# @Software: PyCharm
import queue
import sys

error_dict = {}  # 存储所有错误记录
outqueue = queue.Queue()
outqueue.maxsize = 8
for line in sys.stdin:
    filename, linenum = line.rstrip("\n").split(" ")
    filename = str(filename)
    linenum = str(linenum)
    fnlist = filename.split("\\")
    filename = fnlist[fnlist.__len__() - 1][-16:]
    if filename + " " + linenum not in error_dict:
        error_dict[filename + " " + linenum] = 1
    else:
        error_dict[filename + " " + linenum] += 1

for error in error_dict:
    if not outqueue.full():
        outqueue.put([error, error_dict[error]])
    else:
        outqueue.get()
        outqueue.put([error, error_dict[error]])
while not outqueue.empty():
    print(outqueue.get())

