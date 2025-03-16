from os import listdir, rename
import hashlib

def hashFileMD5(string):
    ext = string.split('.')[-1]
    m = hashlib.md5()
    m.update(string.encode('UTF-8'))
    return f"{m.hexdigest()}.{ext}"

def renameFiles(dir):
    files = listdir(dir)
    for file in files:
        orgFile = dir + file
        newFile = dir + hashFileMD5(file)
        rename(orgFile, newFile)
        #print(orgFile, newFile) # Debug line 


inputDirectory = input("Image Anonymizer v0.0.1\nEnter target path:")
renameFiles(inputDirectory)