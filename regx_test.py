import csv
import re
import regx_fun as regx

def choose_regx(msg):
    REGX = {
        'password' : regx.password_regx,
        'ipv4':regx.ipv4_regx,
        'mac' : regx.mac_regx
    }
    method = REGX.get(msg)
    if method:
        method() 


if __name__ == "__main__":
    #choose_regx('password')
    #choose_regx('ipv4')
    choose_regx('mac')
    pass
