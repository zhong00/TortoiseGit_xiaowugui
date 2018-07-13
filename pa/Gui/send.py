#-*-coding:utf-8-*-
__author__ = 'zhonglingling'

import requests

user_agent ="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
cookie = r'd_c0="ADDCZ2ahaQuPTuwr-1KIWstLOioFztGaVj4=|1488847301"; _zap=fb201e6f-08ba-4fd3-9475-399dfe97cfba; _ga=GA1.2.1744522891.1488847288; q_c1=2d6d26a9cd474ed093eb3ca129de490c|1507719376000|1498014857000; z_c0="2|1:0|10:1521509581|4:z_c0|92:Mi4xbF9WN0FBQUFBQUFBTU1KblpxRnBDeVlBQUFCZ0FsVk56YktkV3dEMl9PUFVYbHNtWUV5S3NQZWxiZUNmTU5QcHF3|64f867701607b845ddb680ae7ab5ebf379180994fb5a67344a11773601d82a55"; __DAYU_PP=U6Qinar6iJAyN7AZy3YRffffffff8538846bd1d1; q_c1=2d6d26a9cd474ed093eb3ca129de490c|1525240301000|1498014857000; __utma=51854390.1744522891.1488847288.1527237177.1527237177.1; __utmz=51854390.1527237177.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhong00/collections; __utmv=51854390.100--|2=registration_date=20140915=1^3=entry_date=20140915=1; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8; _xsrf=f2909f87-a4b3-478c-a837-083e0ef6c1d6'
headers = {
    user_agent:user_agent,
    #cookies:cookie
}

url = "http://www.zhihu.com"
req = requests.get(url,headers=headers)
print(req.url)
