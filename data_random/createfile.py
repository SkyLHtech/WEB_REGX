import os
import csv

def createfile(filename,content):
    pathdir = './testdataset'
    if not os.path.exists(pathdir):
        os.makedirs(pathdir)
    with open(pathdir+'/'+filename,'a') as f:
        f.writelines(content+'\n')

def ErrorRecord(filename,content):
    pathdir = './RecordError'
    if not os.path.exists(pathdir):
        os.makedirs(pathdir)
    with open(pathdir+'/'+filename,'a') as f:
        f.writelines(content+'\n')