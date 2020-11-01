from urllib import parse

data={'name':'老余','age':'24','greet':'hello world'}

qs=parse.urlencode(data)
print(qs)

print(parse.parse_qs(qs))



