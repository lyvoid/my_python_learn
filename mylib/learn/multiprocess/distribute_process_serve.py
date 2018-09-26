#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import Queue
from multiprocessing.managers import BaseManager


class Master:
    task = Queue()
    result = Queue()

    @staticmethod
    def get_task():
        return Master.task

    @staticmethod
    def get_result():
        return Master.result

    def start(self):
        BaseManager.register('get_task', callable=self.get_task)
        BaseManager.register('get_result', callable=self.get_result)
        manage = BaseManager(address=('192.168.1.128', 5000), authkey=b'123')
        manage.start()
        # 派发任务
        # -----
        print(BaseManager.get_task)
        # -----
        task = manage.get_task()
        result = manage.get_result()
        for i in range(10):
            task.put(i)
        # 获取结果
        for i in range(10):
            r = result.get(timeout=200)
            print('result:%s' % r)


if __name__ == "__main__":
    master = Master()
    master.start()
