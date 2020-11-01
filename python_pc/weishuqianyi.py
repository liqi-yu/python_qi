
'''
问题描述
求一个自然数N，个位数是6，将6提到最前面所得数是N的4倍
解题思路
令末位数t=6，除最末位数以外部分n
t连续乘10，移动到最高位，再加上n
t+n=10*n+6
153846
代码没有正确结果，待研究研究
'''


def fun(n):
#    if n==15384:
#        print(n)
    nn=n
    t=6
    while nn>1:    #视频给的是nn>0，因为没有给nn确定是int，所以nn/=10永远大于0
        t *=10
        nn /=10

    m = 10*n+6
    if t+n == m*4:
        print(m)

for x in range(1,100000):
#    if x==15384:
#        print(x)
    fun(x)