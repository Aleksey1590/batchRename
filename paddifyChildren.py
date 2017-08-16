import os
import re 
import os.path
from os.path import dirname
numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def split_name(fileName):
    return fileName.split('.')

def renameFiles(baseDirectory):
    counter = 0
    for files in sorted(os.listdir(baseDirectory), key=numericalSort):
        path, sourceName = os.path.split(os.path.realpath(__file__))
        if (files==sourceName):pass
        else:
            counter+=1  
            oldName = baseDirectory + '/' + files
            if (os.path.isfile(oldName)):
                parentFolder = os.path.relpath(baseDirectory, files)
                parentFolder = parentFolder[3:]
                newName = baseDirectory + "/"+parentFolder+ " "+str(counter).zfill(4)+ split_name(files)[1]
                os.rename(oldName, newName)
            else:
                renameFiles(oldName)
renameFiles(os.getcwd())