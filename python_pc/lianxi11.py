import os


os.chdir("D:\python_work")
f=open("lianxi11.txt","a+")
f.write("3位水仙花数，4到6位的字幂数: \n")
for num in range(100,1000000):
    abit=len(str(num))
    if abit-len(str(num-1))>0:
        s='\n{0}位自幂数:'.format(len(str(num)))
        f.write(s)
    sumn=0
    temp=num
    for i in range(abit):
        sumn+=(temp%10)**abit
        temp//=10
    if sumn==num:
        f.write(str(num)+" ")

f.close()