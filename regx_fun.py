import csv
import re

pathdir = './testdataset'
def read_csv(filename):
    filepath = pathdir+'/'+filename
    content = list()
    with open(filepath,'r+') as f:
        for line in f.readlines():
            content.append(line.strip('\n'))
            pass
    print(content)
    return content

def ipv4_regx():
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00001.IPV4/G.csv')
    test_regx(regx , content)

def ipv6_regx():
    regx = re.compile('^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$')
    content = read_csv('/00002.IPV6/G.csv')
    test_regx(regx , content)

def mac_regx():
    regx = re.compile('^([0-9a-fA-F]{2})(([/\s:][0-9a-fA-F]{2}){5})$')
    content = read_csv('/00003.MAC/G.csv')
    test_regx(regx , content)

def dhcp_ipv4_regx():
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00004.DHCP_IPV4/G.csv')
    test_regx(regx , content)

def dhcp_dns_regx():
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00005.DHCP_DNS/G.csv')
    test_regx(regx , content)

def domain_regx():
    regx = re.compile('^[a-zA-Z0-9]([a-zA-Z0-9\\-\\.]{0,62})[a-zA-Z0-9]$')
    content = read_csv('/00006.DHCP_DOMAIN/G.csv')
    test_regx(regx , content)

def password_regx():
    regx = re.compile('^[\x21 -\x7e]{8,32}$')
    content = read_csv('/00007.PASSWORD/G.csv')
    test_regx(regx , content)
    

def hostname_regx():
    regx = re.compile('^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$')
    content = read_csv('/00009.HOSTNAME/G.csv')
    test_regx(regx , content)

def netmask_regx():
    regx = re.compile('^(254|252|248|240|224|192|128|0)\.0\.0\.0|255\.(254|252|248|240|224|192|128|0)\.0\.0|255\.255\.(254|252|248|240|224|192|128|0)\.0|255\.255\.255\.(255|254|252|248|240|224|192|128|0)$')
    content = read_csv('/00010.NETMASK/G.csv')
    test_regx(regx , content)

def gateway_regx():
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00011.GATEWAY/G.csv')
    test_regx(regx , content)

def test_regx(regx , content):
    error_num = 0
    error_index = []
    for i in range(0,len(content)):
        try:
            testregx_result = regx.search(str(content[i])).group()
        except AttributeError:
            print("REGX can't search from input String ")
            error_num += 1
            error_index.append(i+1)
            continue
        else:
            print(testregx_result)
        pass
    print("Total input test num is " + str(len(content))+" and ,pass : "+str(len(content)-error_num)+", no pass : "+str(error_num))
    print("No pass index is " +str(error_index))