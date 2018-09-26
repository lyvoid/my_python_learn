#!usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


# 获取一个BeautifulSoup对象
def get_soup(doc=False, driver=False):
    if not driver:
        return BeautifulSoup(doc, 'html_parser')
    else:
        return BeautifulSoup(driver.page_source, 'html_parser')


# 属性选择
# soup.find_all("p", class_="strikeout")
# soup.find_all("a", attrs={"class": "sister"})
# soup.find_all("a", limit=2) #只返回两个
# soup.find_all("a", text="Elsie")
# soup.find()

# 获取节点内容
def get_content(ele):
    return ele.get_text()


# 获取所有的属性
def get_all_attr(ele):
    return ele.attrs


# 获取单个的属性
def get_attr(ele, attr_name):
    return ele[attr_name]


# 获取标签名
def get_tag(ele):
    return ele.name


# 获取可以可以遍历的全部父节点
def get_patents(ele):
    return ele.parents
    # ele.parent


# 获取可以可以遍历的全部子节点
def get_descendants(ele):
    return ele.descendants
    # ele.children
