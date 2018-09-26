#!urs/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from yang.util import file_operate as my_file


# 设置窗口大小及关闭消息通知
def get_chrome_browser():
    chrome_options = webdriver.ChromeOptions()
    # 关闭通知消息（防止覆盖住了应该填写的页面）
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # 设置窗口尺寸
    # driver.set_window_size(2000, 1000)
    # 窗口最大化
    driver.maximize_window()
    return driver


# 通过driver登录并将cookie dump到指定文件中
def selenium_cookie_save(path, driver):
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookie_str = ';'.join(item for item in cookie)
    my_file.save_dump(cookie_str, path)


def get_phantom_browser(driver_path=None):
    if driver_path is None:
        driver = webdriver.PhantomJS()
    else:
        driver = webdriver.PhantomJS(driver_path)
        driver.maximize_window()
    return driver


# 等待某个元素加载完成，最长时间为longestTime
def wait_page_load(driver, xpath_str, longest_time=100):
    WebDriverWait(driver, longest_time).until(lambda x: x.find_element_by_xpath(xpath_str))


# 将滚动条移动到页面的顶部
def scroll_top(driver):
    js = "var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)


# 将窗口滚动到页面顶部
def scroll_buttom(driver):
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)


# 打开新的窗口
def new_windows(driver, url='http://www.baidu.com'):
    js = 'window.open("%s");' % url
    driver.execute_script(js)
    # browser.current_window_handle #当前窗口句柄
    # handles = browser.window_handles  # 获取当前窗口句柄集合（列表类型）
    # browser.switch_to_window(handle) #切换窗口
    # browser.close() #关闭当前窗口
    # browser.quit() #退出浏览器


# 移动页面到某个元素位置
def move_into(driver, ele):
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(ele, 5, 5)
    # action.click()
    action.perform()


# 获取元素属性值
def get_attr(attr_name, ele):
    return ele.get_attribute(attr_name)


# 获取元素内容
def get_content(ele):
    return ele.text
