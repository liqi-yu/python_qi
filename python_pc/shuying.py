import math

num=input()
n=[]
shuzu=('zero','one','two','three','four','five','six','seven','eight','night')
for i in num:
    numm=ord(i)-48
    n.append(shuzu[numm])
print(n[0],n[1],n[2])