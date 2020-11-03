from faker import Faker
from faker.providers import internet
import createfile as cf

def ipv4(num, filename):
    fake = Faker()
    for i in range(num):
        ipv4 = fake.ipv4()
        cf.createfile(filename, ipv4)

def ipv6(num, filename):
    fake = Faker()
    for i in range(num):
        ipv6 = fake.ipv6(network = False)
        cf.createfile(filename, ipv6)

def mac(num, filename):
    fake = Faker()
    for i in range(num):
        mac = fake.mac_address()
        cf.createfile(filename, mac)

def usr_name(num, filename):
    fake = Faker()
    for i in range(num):
        name = fake.user_name()
        cf.createfile(filename, name)

def hostname(num, filename):
    fake = Faker()
    for i in range(num):
        name = fake.hostname()
        cf.createfile(filename, name)

def domain_name(num, filename):
    fake = Faker()
    for i in range(num):
        domain_name = fake.domain_name()
        cf.createfile(filename, domain_name)

if __name__ == "__main__":
    num = 1000
    # path = "/00001.IPV4/G.csv"
    # ipv4(num,path)
    # path = "/00002.IPV6/G.csv"
    # ipv6(num,path)
    path = "/00003.MAC/G.csv"
    mac(num,path)
    # path = "/00006.DHCP_DOMAIN/G.csv"
    # domain_name(num,path)
    # path = "/00008.USRNAME/G.csv"
    # usr_name(num,path)
    # path = "/00009.HOSTNAME/G.csv"
    # hostname(num,path)
    pass