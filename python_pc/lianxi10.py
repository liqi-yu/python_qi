# UTF-8

def ischongfu(n):
    a=[]
    t=n
    while t>0:
        a.append(t%10)
        t =t//10
    
    if a[0]!=a[1]:
        if a[0]!=a[2]:
            if a[1]!=a[2]:
                return True
            else:
                return False

a=n=0
for x in range(100,1000):
    if ischongfu(x):
        print(x,end=' ')
        n+=1
        a+=1
        if a==10:
            print('')
            a=0
print('')
print(n)