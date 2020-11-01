'''
水仙花数
'''
'''能成功
for i in range(100,1000):
    ge=i%10
    shi=i%100-ge
    shi/=10
    bai=i//100 #//是得到向下取整
    if ge**3+shi**3+bai**3 == i:
        print("{} is shui xian hua shu.".format(i))
'''


def isshuixianhua(n):
    a=[]
    t=n
    while t>0:
        a.append(t%10)
        t=t//10
    k=len(a)
    return sum([x ** k for x in a])==n   #列表解析，sum函数应用
'''
    s=0
    for x in a:
        s+=x**k
    return s==n


    i=x
    ge=i%10
    i=i//10
    shi=i%10
    i=i//10
    bai=i%10
    i=i//10
    qian=i%10
    if x<1000:
        if ge**3+shi**3+bai**3==x:
            return True
        else:
            return False
    else:
        if ge**4+shi**4+bai**4+qian**4==x:
            return True
        else:
            return False
'''



for x in range(100,100000):
    if isshuixianhua(x):
        print("{} is shuixianhuashu.".format(x))