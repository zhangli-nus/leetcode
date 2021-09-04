#coding: utf-8

def add(x, y):
    while (y!=0):
        c = x & y #0011 & #0101， 同为1则进一位
        x = x ^ y #0111，不同则为1，同则为0, 0110
        y = c<<1 #进一位, 0010
        print(x, y)
    return x

if __name__ == '__main__':
    res = add(3, 5)
    print(res)