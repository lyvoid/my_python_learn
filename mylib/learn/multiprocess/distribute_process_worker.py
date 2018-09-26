#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import Queue
import time
from multiprocessing.managers import BaseManager

class Worker:
    task = Queue()
    result = Queue()

    @staticmethod
    def start():
        print(BaseManager)
        BaseManager.register('get_task')
        BaseManager.register('get_result')
        print(BaseManager.get_task)
        server_addr = '192.168.1.128'
        manage = BaseManager((server_addr, 5000), authkey=b'123')
        manage.connect()
        task = manage.get_task()
        result = manage.get_result()
        for i in range(10):
            try:
                time.sleep(10)
                n = task.get(timeout=1)
                print(n)
                r = n * n
                result.put(r)
            except Queue.Empty:
                print('task empty')


if __name__ == "__main__":
    Worker.start()
