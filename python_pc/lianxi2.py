'''自己写的 不完善
d={'a':39,'b':40,'c':99,'d':100}

def find(x,y):
    if x in d:
        if int(y) == d[x]:
            print('yes')

    else:
        print('no')

    
a=1
b=40
find(a,b)
'''
# 老师代码
def findkv(dct,**kwargs):
    r={k:v for k,v in kwargs.items() if dct.get(k)==v}
    return r

d={'a':39,'b':40,'c':99,'d':100}
fr=findkv(d,a=1,b=40)
print(fr)