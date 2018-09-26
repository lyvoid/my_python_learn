import time

from yang.crwaler import my_bs4, my_selenium
from yang.util import file_operate as my_file

#  登录+搜索
key_word = '汉服'
driver = my_selenium.get_chrome_browser()
driver.get('http://weibo.com/')
my_selenium.wait_page_load(driver, '//input[@node-type="searchInput"]')
search_input = driver.find_element_by_xpath('//input[@id="loginname"]')
search_input.clear()
search_input.send_keys("735600970@qq.com")
search_input = driver.find_element_by_xpath('//input[@type="password"]')
search_input.clear()
search_input.send_keys("*****")
search_button = driver.find_element_by_xpath('//span[@node-type="submitStates"]')
search_button.click()
my_selenium.wait_page_load(driver, '//input[@node-type="searchInput"]')
search_input = driver.find_element_by_xpath('//input[@node-type="searchInput"]')
search_input.clear()
search_input.send_keys(key_word)
search_button = driver.find_element_by_xpath('//a[@href="javascript:void(0);"]')
search_button.click()
a = 0

# 抓取+存储
pic_urls = []
nick_names = []
dir_txt = my_file.mk_dir_below_current('测试数据')
dir_pic = my_file.mk_dir_below_current(key_word + '图片爬取')
small_pics = driver.find_elements_by_xpath('//img[@class="bigcursor"]')
try:
    while True:
        # 拉到最底下，防止有没有加载完
        my_selenium.scroll_buttom(driver)
        # 等待下一页加载出来（防止内容不够的时候就开始抓取）
        my_selenium.wait_page_load(driver, '//a[@class="page next S_txt1 S_line1"]')
        # 睡5s，防止被新浪封
        time.sleep(5)
        soup = my_bs4.get_soup(driver=driver)
        # 获取本页所有的图片
        small_pics = soup.find_all('img', class_="bigcursor")
        pic_urls.clear()
        nick_names.clear()
        # 遍历所有图片
        for small_pic in small_pics:
            pic_urls.append(small_pic['src'])
            # 遍历该图片的父类，并找到和名字相同父类的那个节点
            for parent in small_pic.parents:
                try:
                    # 如果找到了这个父类节点，那么把名字取下来
                    if (parent['class'] == ['feed_list', 'feed_list_new', 'W_linecolor']):
                        nick_names.append(parent.find('a', class_="W_texta W_fb")['nick-name'])
                except:
                    pass
        # 存储所有图片以及对应的微博名
        for i in range(len(pic_urls)):
            url = pic_urls[i]
            nick_name = nick_names[i]
            a += 1
            try:
                my_file.save_image_from_url(url, dir_pic, str(a))
                my_file.write_txt_add_oneline(my_file.get_abs_name(dir_txt, key_word + "图片抓取.txt"),
                                              str(a) + ":" + nick_name)
            except:
                pass
        # 找到下一页的按键
        search_button = driver.find_element_by_xpath('//a[@class="page next S_txt1 S_line1"]')
        # 翻到下一页
        try:
            search_button.click()
        except:
            continue

except:
    print("爬取完毕")
