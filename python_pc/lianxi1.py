def convert(s):
    lst=[i.upper() if i==i.lower() else i.lower() for i in s]
    return ''.join(lst)

s='Hello'
c=convert(s)
print(c)
print(0)
print('O')