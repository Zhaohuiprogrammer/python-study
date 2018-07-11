from urllib import request
from http import cookiejar


url = "http://www.baidu.com"

print("第一种方法")
resp1 = request.urlopen(url)
print(resp1.getcode())
print(len(resp1.read()))

print("第二种方法")
req = request.Request(url)
req.add_header("user-agent", "Mozilla/5.0")
resp2 = request.urlopen(req)
print(resp2.getcode())
print(len(resp2.read()))

print("第三种方法")
cj = cookiejar.CookieJar()
cookieProc = request.HTTPCookieProcessor(cj)
opener = request.build_opener(cookieProc)
request.install_opener(opener)
resp3 = request.urlopen(url)
print(resp3.getcode())
print(cj)
print(resp3.read())
