'''
凯撒密码加密
'''

caesar=input('enter zifu:')
d=3
pwd=ord(caesar)
pwd+=d
if pwd>ord('z'):
    pwd=pwd-26

pwdd=chr(pwd)

print(caesar,'-->',pwdd)