import csv
import re
import time
import data_random.createfile as cf

pathdir = './testdataset'
def read_csv(filename):
    filepath = pathdir+'/'+filename
    content = list()
    with open(filepath,'r+') as f:
        for line in f.readlines():
            content.append(line.strip('\n'))
            pass
    return content

def all_regx(path):
    regx_G = []
    regx_NG = []
    if path == "G.csv":
        print("Test file is G.csv, that's mean all test data is OK. If there are some error in the result, please check the regx.")
        regx_G.append("IPV4") if ipv4_regx(path) == True else regx_NG.append("IPV4")
        regx_G.append("IPV6") if ipv6_regx(path) == True else regx_NG.append("IPV6")
        regx_G.append("MAC") if mac_regx(path) == True else regx_NG.append("MAC")
        regx_G.append("DHCP_IPV4") if dhcp_ipv4_regx(path) == True else regx_NG.append("DHCP_IPV4")
    print("\nREGX pass-test list = " +str(regx_G))
    print("REGX no-pass-test list = " +str(regx_NG))

def ipv4_regx(path):
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00001.IPV4/'+path)
    return test_regx(regx, content, "IPV4", path)



def ipv6_regx(path):
    regx = re.compile('^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$')
    content = read_csv('/00002.IPV6/'+path)
    return test_regx(regx, content, "IPV6", path)


def mac_regx(path):
    regx = re.compile('^([0-9a-fA-F]{2})(([/\s:][0-9a-fA-F]{2}){5})$')
    content = read_csv('/00003.MAC/'+path)
    return test_regx(regx, content, "MAC", path)

def dhcp_ipv4_regx(path):
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00004.DHCP_IPV4/'+path)
    return test_regx(regx, content, "DHCP_IPV4", path)

def dhcp_dns_regx(path):
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00005.DHCP_DNS/'+path)
    test_regx(regx , content)

def domain_regx(path):
    regx = re.compile('^[a-zA-Z0-9]([a-zA-Z0-9\\-\\.]{0,62})[a-zA-Z0-9]$')
    content = read_csv('/00006.DHCP_DOMAIN/'+path)
    test_regx(regx , content)

def password_regx(path):
    regx = re.compile('^[\x21 -\x7e]{8,32}$')
    content = read_csv('/00007.PASSWORD/'+path)
    test_regx(regx , content)
    

def hostname_regx(path):
    regx = re.compile('^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$')
    content = read_csv('/00009.HOSTNAME/'+path)
    test_regx(regx , content)

def netmask_regx(path):
    regx = re.compile('^(254|252|248|240|224|192|128|0)\.0\.0\.0|255\.(254|252|248|240|224|192|128|0)\.0\.0|255\.255\.(254|252|248|240|224|192|128|0)\.0|255\.255\.255\.(255|254|252|248|240|224|192|128|0)$')
    content = read_csv('/00010.NETMASK/'+path)
    test_regx(regx , content)

def gateway_regx(path):
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('/00011.GATEWAY/'+path)
    test_regx(regx , content)

def test_regx(regx , content, regx_type, path):
    E_NUM = 0
    E_CONTENT = []
    D_LEN = len(content)
    for i in range(0,len(content)):
        try:
            testregx_result = regx.search(str(content[i])).group()
        except AttributeError:
            E_NUM += 1
            E_CONTENT.append(content[i])
            continue
        pass

    if path == 'G.csv':
        tmp = "--------------------------"
        if E_NUM >= 1:
            TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            cf.ErrorRecord(regx_type+ '/G.csv', TIME)
            cf.ErrorRecord(regx_type+ '/G.csv', tmp)
            for i in range(0, E_NUM-1):
                cf.ErrorRecord(regx_type+ '/G.csv', E_CONTENT[i])
            cf.ErrorRecord(regx_type+ '/G.csv', tmp)
            print(regx_type + " total input test num is " + str(D_LEN)+" and, pass : "+str(D_LEN-E_NUM)+", error test data num is : "+str(E_NUM) + ", because test dataset is G.csv, so please check REGX fomula.")
            return False
        else:
            print(regx_type + " total input test num is " + str(D_LEN) + " and test result is OK.")
            return True


