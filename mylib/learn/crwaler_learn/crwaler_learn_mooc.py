from yang.crwaler.my_requests import *
from bs4 import BeautifulSoup


def get_list(list, text):
    pass


if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    text = get_response_use_mozilla(url).text
    soup = BeautifulSoup(text, 'html.parser')
    soup.find_all()
