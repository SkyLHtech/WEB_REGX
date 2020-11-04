import csv
import re
import regx_fun as regx
import sys
def choose_regx(msg):
    REGX = {
        'ipv4':regx.ipv4_regx,
        'ipv6' : regx.ipv6_regx,
        'mac' : regx.mac_regx,
        'password' : regx.password_regx,
        'dhcp_ipv4' : regx.dhcp_ipv4_regx,
        'dhcp_dns' : regx.dhcp_dns_regx,
        'domain' : regx.domain_regx,
        'gateway' : regx.gateway_regx,
        'hostname' : regx.hostname_regx,
        'netmask' : regx.netmask_regx
    }
    method = REGX.get(msg)
    if method:
        method() 


if __name__ == "__main__":
    input = sys.argv[1]
    choose_regx(input)
    pass
