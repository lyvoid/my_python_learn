import yang.crwaler.my_requests as my_request
import re
from urllib import parse
import time
from datetime import datetime, timedelta
from pymongo import MongoClient


class MongoCache:
    """
    使用mongo记录缓存
    """

    def __init__(self, client=None, expires=timedelta(days=30)):
        if client is None:
            self.client = MongoClient('localhost', 27017)
        else:
            self.client = client

        self.db = self.client.cache
        # 设置记录过期时间为expires
        self.db.webpage.create_index('timestamp', expireAfterSenconds=expires.total_seconds())

    def __getitem__(self, url):
        # 通过index的形式获取record，如果不存在则抛出KeyError异常
        record = self.db.webpage.find_one({'_id': url})
        if record:
            return record['result']
        else:
            raise KeyError(url + " does not exist.")

    def __setitem__(self, url, result):
        record = {'result': result, 'timestamp': datetime.now()}
        self.db.webpage.update({'_id': url}, {'$set': record}, upsert=True)


class Downloader:
    def __init__(self, delay=1, num_retries=1, cache=MongoCache(), **kwargs):
        """

        :param delay: 每一次抓取的延迟
        :param num_retries: 如果抓取失败会重复抓取多少次
        :param cache: mongoCache对象,如果有的话
        :param kwargs:抓取参数（headers信息等）
        """
        self.throttle = Throttle(delay)
        self.cache = cache
        self.num_retries = num_retries
        self.kwargs = kwargs

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
        if result is None:
            self.throttle.wait(url)
            return self.download(url)
        return result

    def download(self, url):
        """

        :param url:
        :return:
        """
        n = self.num_retries
        content = None
        while not content and n > 0:
            content = my_request.get_content_str(url, **self.kwargs)
            n -= 1
        self.cache[url] = content
        return content


class Throttle:
    """
    Add a delay between downloads to the same domain
    """

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = parse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_sces = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_sces > 0:
                time.sleep(sleep_sces)
        self.domains[domain] = datetime.now()


class ScrapeCallback:
    def __call__(self, url, html):
        print("visit:" + url + str(len(html)))


# print(get_content_str(url))

def link_crawler(url, link_regex=".*", delay=0, max_depth=-1, num_retries=1, scrape_callback=None,
                 cache=MongoCache(), **kwargs):
    """

    :param url: 起始url
    :param link_regex: 如果发现的link满足该正则表达式，才会进行访问
    :param delay: 每一次访问间隔时间
    :param max_depth: 访问的最大深度
    :param num_retries: 如果访问失败会继续尝试的次数
    :param scrape_callback: 回调函数，对返回的url，html做对应处理
    :param cache: 缓存文件，需要满足dict的访问及记录方式
    :param kwargs: 访问参数
    :return:null
    """
    crawl_queue = [url]
    crawl_visited_list = dict()
    crawl_visited_list[url] = 0
    link_regex = re.compile(link_regex)
    downloader = Downloader(delay=delay, num_retries=num_retries, cache=cache, **kwargs)
    while crawl_queue:
        url = crawl_queue.pop()
        html = downloader(url)
        depth = crawl_visited_list[url]
        # 如果取到了正常的内容
        if html:
            if scrape_callback:
                scrape_callback(url, html)
            # 如果深度足够的话
            if depth != max_depth:
                for link in get_links(html):
                    if link not in crawl_visited_list and link_regex.match(html):
                        crawl_queue.append(link)
                        crawl_visited_list[link] = depth + 1
                        # print("visited", len(crawl_visited_list), ", queue", len(crawl_queue))


def get_links(html):
    """

    :param html:
    :return: 返回html中的link
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


if __name__ == "__main__":
    cache = MongoCache()
    url = 'http://www.douban.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    link_crawler(url, delay=0, max_depth=5, num_retries=1, scrape_callback=ScrapeCallback(), cache=cache,
                 headers=headers)
