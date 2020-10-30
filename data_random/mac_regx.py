import random
import createfile as cf

def mac_random(size):
    maclist = []
    if size == 'mac':
        for i in range(1,7):
            RANDSTR = "".join(random.sample("0123456789abcdef",2))
            maclist.append(RANDSTR)
    elif size == 'MAC':
        for i in range(1,7):
            RANDSTR = "".join(random.sample("0123456789ABCDEF",2))
            maclist.append(RANDSTR)
    MAC = ":".join(maclist)
    return MAC

def macset_creation(num,filename):
    for i in range(num):
        MAC = mac_random('MAC')
        cf.createfile(filename, MAC)
    for i in range(num):
        mac = mac_random('mac')
        cf.createfile(filename, mac)

if __name__ == "__main__":
    macfile_name = "/00002.MAC/G.csv"
    macset_creation(1000,macfile_name)
    pass
