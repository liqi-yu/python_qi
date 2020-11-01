from lxml import etree


html = etree.parse('hello.html')
result = html.xpath('//h4')
print(result)
