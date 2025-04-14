import json
import os

PATH = "Elementals"

def extract_integer(filename):
    return int(filename.split('.')[0])

def getName(c):
    return str(c)+"-"+Data[str(c)]["Name"]+".png"


with open("PTE.json", "r") as x:
    Data = json.loads(x.read())

files = sorted(os.listdir(PATH), key=extract_integer)

c = 1
for f in files:
    print(f," => ", getName(c))

    os.rename(PATH+"\\"+f,PATH+"\\"+getName(c))
    c+=1