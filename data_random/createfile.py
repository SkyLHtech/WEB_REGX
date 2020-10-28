import os
import csv
pathdir = './testdataset'
def createfile(filename,content):
    if not os.path.exists(pathdir):
        os.makedirs(pathdir)
    with open(pathdir+'/'+filename,'a') as f:
        f.writelines(content+'\n')