import random
import string
import createfile as cf

def str_chinese():
    val = random.randint(0x4e00,0x9fa5) #(0x4e00,0x9fa5) = Chinese 
    return chr(val)
    
def str_korean():
    val = random.randint(0xac00,0xd7a3) #(0x3130,0x318f) = Korean
    return chr(val)

# def str_janpanese():
#     val = random.randint(0x0800,0x4e00) #(0x4e00,0x9fbf) = Japanese
#     return chr(val)

def str_compose(str_type , str_len):
    cstring = ""
    if  str_type == 'chinese':    
        for i in range(0, str_len) :
            cstring += str(str_chinese())
            pass
    elif str_type == 'korean':
        for i in range(0, str_len) :
            cstring += str(str_korean())
            pass
        pass
    return cstring


def str_special():
    initspecial = string.punctuation
    special = ''
    for i in initspecial:
        special += i
        pass
    return special

# This fun produces string include [a-zA-Z0-9] and special chr 
def str_total(filename):
    ascii_letter = string.ascii_letters
    number = string.digits
    special = ''
    special = str_special()
    for num in range(1,41):
        #for i in range(0,200):
            #num = random.randint(1,40)
            value = ''.join(random.sample(ascii_letter + str(number) + special, num))
            cf.createfile(filename, value)
            print(value)
        #pass
    pass

if __name__ == "__main__":
    str_test_filename = "password_dataset.csv"
    str_total(str_test_filename)
    #print(str_compose('chinese',10))
    #print(str_compose('korean',10))

    pass    
