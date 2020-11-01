'''
这是生成斐波那契数列的程序
'''
import os

os.chdir("D:\python_work")
f=open("lianxi12.txt","a+")
f.write("斐波那契数列:\n")
a=1
b=2
f.write(str(a)+' ')
f.write(str(b)+' ')
for i in range(0,98):
    c=a+b
    f.write(str(c)+' ')
    a=b
    b=c
f.close()