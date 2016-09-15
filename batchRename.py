import os
import os.path
from os.path import dirname


def split_name(fileName):
    return fileName.split('.')

def renameFiles(baseDirectory):
    counter = 0
    for files in os.listdir(baseDirectory):
        counter = counter + 1
        oldName = baseDirectory + '/' + files
        if (os.path.isfile(oldName)):
            parentFolder = os.path.relpath(baseDirectory, files)
            parentFolder = parentFolder[3:]
            #print parentFolder
            newName = baseDirectory + "/"+parentFolder+ " "+ str(counter) + '.' + split_name(files)[1]
            #print "newName: " + newName
            os.rename(oldName, newName)
        else:
            renameFiles(oldName)
renameFiles(os.getcwd())
