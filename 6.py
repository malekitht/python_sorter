from PIL.ExifTags import TAGS
from PIL import Image
import os
import datetime
import shutil
now = datetime.datetime.now()
god=now.year
god=str(god)
link=input()
l=os.listdir(r""+link)
dirName = 'C:\sorted-'
print(l)
lenth=len(l)
spec=chr(92) 
for i in range(lenth):
    img = Image.open(r""+link+spec+l[i])
    exif = {
    TAGS[k]: v
    for k, v in img._getexif().items()
    if k in TAGS
    }
    #print(exif)
#print(exif['DateTimeOriginal'])
    a=exif['DateTimeOriginal']
    a=a[:-9]
    god=a[:4]
    print(god)
    a=a.replace(":","-")
    print(a)
    a=a[5:-3]
    print(a)
    try:
        os.makedirs(dirName+god+spec+a)    
        print("Directory " , dirName+god+spec+a ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName+god+spec+a ,  " already exists")
    try:
        shutil.move(link+spec+l[i], dirName+god+spec+a+spec+l[i])
    except PermissionError:
        print("Bruh")
print(len(l))

