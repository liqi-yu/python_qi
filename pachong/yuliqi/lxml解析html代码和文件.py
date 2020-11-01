from lxml import etree

# text='''
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title>多测师里最帅的</title>
# 	</head>
# 	#h1到h6字体依次减小
# 	<body>
#     	<h1>我是最帅的</h1>
#     	<h2>我是最帅的</h2>
#     	<h3>我是最帅的</h3>
#     	<h4>我是最帅的</h4>
#     	<h5>我是最帅的</h5>
#     	<h6>我是最帅的</h6>
# 	</body>
# </html>
# '''
# html=etree.HTML(text)
# print(html)
# result=etree.tostring(html).decode('utf-8')
# print(result)


html= etree.parse('hello.html')
result=etree.tostring(html).decode('utf-8')
print(result)
