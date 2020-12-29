import csv
import re
import regx_fun as regx
import sys
def choose_regx(fun , path):
    REGX = {
        'all'       : regx.all_regx, 
        'ipv4'     : regx.ipv4_regx,
        'ipv6'      : regx.ipv6_regx,
        'mac'       : regx.mac_regx,
        'password'  : regx.password_regx,
        'dhcp_ipv4' : regx.dhcp_ipv4_regx,
        'dhcp_dns'  : regx.dhcp_dns_regx,
        'domain'    : regx.domain_regx,
        'gateway'   : regx.gateway_regx,
        'hostname'  : regx.hostname_regx,
        'netmask'   : regx.netmask_regx
    }
    method = REGX.get(fun)  
    if method:
        method(path)
    else:
        print("Input regx_name has error, please check again.")



if __name__ == "__main__":
    input_type = sys.argv[1] # -G or -NG
    test_regx_fun = sys.argv[2]
    if input_type == '-G':
        file_path = 'G.csv'
    elif input_type == '-NG':
        file_path = 'NG.csv'
    else:
        print('Input test file type is -G or -NG, please check again.' )
        exit()
    choose_regx(test_regx_fun , file_path)
