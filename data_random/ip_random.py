import random
import sys
import createfile as cf
def ipcell_random(begin,end):
    return random.randint(begin,end)

def ip_compose(begin,end):
    ipaddress = ""
    for i in range(4):
        if i < 3:
            ipaddress += str(ipcell_random(begin,end))+'.'
        else:
            ipaddress += str(ipcell_random(begin,end))
    return ipaddress

def ipset_creation(num , filename):
    for n in range(num):
        ip =ip_compose(0,255)
        #print(ip)
        cf.createfile(filename, ip)

if __name__ == "__main__":
    num = 1000
    ip_good_name = "/00001.IP/G.csv"
    ipset_creation(num,ip_good_name)
    ip_bad_name = "/00001.IP/NG.csv"
    ipset_creation(num,ip_bad_name)
    pass

