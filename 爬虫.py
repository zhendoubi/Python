#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'http://library_web.ahut.edu.cn/MainWeb/datasource/mainshow.asp?d_id=2'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div')
    print(texts[0].text.replace())
