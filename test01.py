from imp import reload

import requests
#
# r = requests.get("http://www.baidu.com",timeout=1)
# s = r.text
# print(s)
# st = "www."
# en = ".png"
# n = s.find(st)
# f = s.find(en)
# print(s[n:f + len(en)])
#
# print(r.elapsed.total_seconds())
#
# assert "//www.baidu.com/img/bd_logo1.png" in r.text


r = requests.session().get("http://www.baidu.com")
print(r.text)


