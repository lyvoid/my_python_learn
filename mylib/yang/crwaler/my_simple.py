#!urs/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
from http import cookiejar


# 获取一个啥都没有的opener
def get_opener():
    handler = request.HTTPHandler
    return request.build_opener(handler)


# 通过cookie获取一个opener
def get_cookie_opener(cookie):
    handler = request.HTTPCookieProcessor(cookie)
    return request.build_opener(handler)


# 构建一个给一个opener加上头,head是一个dict
def add_header(opener, head):
    header = []
    for k, v in head.items():
        header.append((k, v))
    opener.addheaders = header


# 通过cookie位置，获取一个cookie文件，或者是需要保存的路径
def get_cookie(cookie_save_path=False, cookie_load_path=False):
    if cookie_save_path:
        cookie = cookiejar.MozillaCookieJar(cookie_save_path)
    else:
        cookie = cookiejar.MozillaCookieJar()
        cookie.load(cookie_load_path, ignore_discard=True, ignore_expires=True)
    return cookie


# 返回一个较为通用的头部
def get_header():
    return {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
