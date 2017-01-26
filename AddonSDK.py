import os
import json
import random
import zipfile


#_____________________________________________________________________
def _rand():#this function makes a random uuid
    x1 = ''
    x2 = ''
    x3 = ''
    x4 = ''
    while len(x1) != 8:
        z = str(hex(random.randrange(16)))
        x1 = x1 + z[2]
    x1 = x1 + '-'
    while len(x2) != 4:
        z = str(hex(random.randrange(16)))
        x2 = x2 + z[2]
    x2 = x2 + '-'
    while len(x3) != 4:
        z = str(hex(random.randrange(16)))
        x3 = x3 + z[2]
    x3 = x3 + '-'
    while len(x4) != 12:
        z = str(hex(random.randrange(16)))
        x4 = x4 + z[2]
    x = x1 + x2 + x3 + x4
    return x
#_____________________________________________________________________
def _zip(x):#this function makes ziper
    with open('zip.txt', 'r') as f:
        z = f.read()#this makes zip excutable
    with open(x+'ip.py', 'w') as f:
        f.write(z)
#_____________________________________________________________________
def _PMU(x):#this function makes manifest
    with open(x+'ack_manifest.json', 'w') as f:
        print('Give pack name and the packs version $<version> <name>')
        a = input('>')
        a = a + ';'
        z = 0
        while a[z] != ' ':
            z +=1
        print('Give description and version $<version> <description>')
        b = input('>')
        b = b + ';'
        x = 0
        while b[x] != ' ':
            x += 1
        uc = {"header": {"pack_id": _rand(),"modules": [ {"uuid": _rand(),"type": "data"}]}}
        uc["header"]["name"] = a[z+1:-1]
        uc["header"]["packs_version"] = a[0:z]
        uc["header"]["modules"][0]["description"] = b[x+1:-1]
        uc["header"]["modules"][0]["version"] = b[0:x]
        f.write(json.dumps(uc))
#_____________________________________________________________________
while True:#console loop
    uc = input(">")
    uc = uc + ';'

    if uc[0:6] == 'update':
        _PMU(uc[7:-1]+'/p')#this updates an old manifest, or makes a new one
        #depends on how being used in code

    elif uc == 'make manifest;':
        _PMU('p')#this makes a manifest, just incase thats all they want

    elif uc == 'make ziper;':
        _zip('z')#this makes ziper
        
    elif uc == 'random;':
        print(_rand())#this makes a random uuid, should be 100% new and
        #random everytime

    elif uc == 'exit;':
        break#this exits console
        
    elif uc[0:3] == 'new':#this makes a new behavior addon
        x = 4
        while uc[x] != ';':
            x += 1
        try:
            os.mkdir(uc[4:x])#this makes the project file
            os.mkdir(uc[4:x]+'/entities')#this makes the entities folder
            os.mkdir(uc[4:x]+'/loot_tables')#this makes the loot_tables foldeer
            _PMU(uc[4:x]+'/p')#this makes manifest
            _zip(uc[4:x]+'/z')#this makes the zip executable
        except:
            print("Error: Project: {}, already exists".format(uc[4:x]))
