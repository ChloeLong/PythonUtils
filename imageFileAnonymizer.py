from os import listdir, rename, remove
import hashlib
from PIL import Image

def hashFileMD5(string):
    ext = string.split('.')[-1]
    m = hashlib.md5()
    m.update(string.encode('UTF-8'))
    return f"{m.hexdigest()}.{ext}"

def renameFiles(dir):
    files = listdir(dir)
    for file in files:
        orgFile = f"{dir}/{file}"
        newFile = f"{dir}/{hashFileMD5(file)}"
        rename(orgFile, newFile)
        #print(orgFile, newFile) # Debug line 

def convertToPng(dir):
    files = listdir(dir)
    for file in files:
        im = Image.open(f"{dir}/{file}")
        im.save(f"{dir}/{file.split('.')[0]}.png")
        remove(f"{dir}/{file}")

inputDirectory = input("Image file anonymizer v0.0.1\nEnter target path:")
renameFiles(inputDirectory)
convertToPng(inputDirectory)