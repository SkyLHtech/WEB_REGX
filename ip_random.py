import random
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
        cf.createfile(filename, ip)

if __name__ == "__main__":
    ipfile_name = "ip_dataset.csv"
    ipset_creation(1000,ipfile_name)
    pass

