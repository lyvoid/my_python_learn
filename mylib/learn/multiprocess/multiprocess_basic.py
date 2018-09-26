#!urs/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process, Queue
import time


# 定义子进程任务
def get_value(q):
    while True:
        v = q.get()
        print("get" + v)


def put_value(q):
    for i in range(10):
        q.put(str(i))
        print("put" + str(i))
        time.sleep(0.5)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=put_value, args=(q,))
    p2 = Process(target=get_value, args=(q,))
    p.start()
    p.join()
    p2.start()
    print("---")
