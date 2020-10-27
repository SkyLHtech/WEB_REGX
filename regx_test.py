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

def choose_regx(msg):
    REGX = {
        'password' : password_regx,
        'ip':ip_regx
    }
    method = REGX.get(msg)
    if method:
        method() 

def password_regx():
    regx = re.compile('^[\x21 -\x7e]{8,32}$')
    content = read_csv('password_dataset.csv')
    test_regx(regx , content)

def ip_regx():
    regx = re.compile('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    content = read_csv('ip_dataset.csv')
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


if __name__ == "__main__":
    #choose_regx('password')
    choose_regx('ip')
    pass
