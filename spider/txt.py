#coding=utf-8
__author__='老王'
import re
def write():
    while 1:
        s=raw_input(u'输入存入的内容，输入Q结束：')
        if s=='Q':
            break
        else:
            f=open(r'D:\test.txt','a+')
            f.write(s+'\n')
            f.close()
def read():
    f=open(r'D:\test.txt','r')
    print u'---文件路径{}--------'.format(f.name)
    print f.read()
    f.close()
def delete():
    f=open(r'D:\test.txt','w')
    f.write('')
    f.close()
def updata(x,y):
    f=open(r'D:\test.txt','r+')
    '''
    1.当文件不存在时，“r+”不会自动创建而导致调用失败；“w+”会自动创建文件
    2.当文件存在时，“r+”不会清空文件内容，“w+”会清空原文件内容
    3.“r+”打开文件后，文件内部的读写指针会被移动到文件开头，如果直接写入数据会覆盖原文件内容
    '''
    d=f.read()
    #open(r'D:\test.txt','w').write(re.sub(x, y, d))
    s=re.sub(x,y,d)
    f.close()
    f=open(r'D:\test.txt','w')
    f.write(s)
    f.close()

if __name__=='__main__':
    while 1:
        s=raw_input(u'输入w写入，r读取，u更改，d清空，其他退出:')
        if s=='q':
            break
        elif s=='w':
            write()
        elif s=='r':
            read()
        elif s=='u':
            x=raw_input(u'输入原内容：')
            y=raw_input(u'输入目标内容：')
            updata(x,y)
        elif s=='d':
            delete()
        else:
            break