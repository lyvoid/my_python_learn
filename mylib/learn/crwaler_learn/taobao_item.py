#!usr/bin/env python3
# -*- coding:utf-8 -*-

from yang.crwaler import my_requests
from yang.util.file_operate import *
import re

item_name = "眼镜"
url = "https://s.taobao.com/search"
kv = {"q": item_name, "s": None}
r = my_requests.get_response_with_keywords(url, kv)
html = r.text
plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
ilt = list()
for i in range(len(plt)):
    price = eval(plt[i].split(':')[1])
    title = eval(tlt[i].split(':')[1])
    ilt.append([price, title])
tplt = "{:4},{:8},{:16}\n"

count = 0
for g in ilt:
    count += 1
    add_line('D:/1.csv', tplt.format(count, g[0], g[1].replace(",", "/c")))
