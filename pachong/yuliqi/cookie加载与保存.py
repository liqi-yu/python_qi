from urllib import request
from http.cookiejar import MozillaCookieJar

#cookie的保存
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# resp = opener.open('http://httpbin.org/cookies/set/course/abc')
#
# cookiejar.save(ignore_discard=True,ignore_expires=True)

#加载cookie

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://httpbin.org/cookies/set/course/abc')

for cookie in cookiejar:
    print(cookie)
