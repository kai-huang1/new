import requests

r = requests.get("http://www.baidu.com",timeout=1)
r.encoding = "utf-8"
s = r.text
st = "www."
en = ".png"
n = s.find(st)
f = s.find(en)
print(s[n:f + len(en)])

assert "//www.baidu.com/img/bd_logo1.png" in r.text
