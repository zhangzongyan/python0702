# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03_异步io
   Description :
   Author :       zongyanzhang
   date：          2018/8/10
-------------------------------------------------
   Change Activity:
                   2018/8/10:
-------------------------------------------------
"""
__author__ = 'admin'
import threading
import asyncio
import time

#将hello函数作为一个协程函数
#@asyncio.coroutine
async def hello(n):
    print("start hello....%s" % threading.current_thread())
    # 调用协程函数
    #yield from asyncio.sleep(n)
    await asyncio.sleep(n)
    print("end hello....%s" % threading.current_thread())

if __name__ == '__main__':
    # 循环事件对象
    print(time.ctime())

    asy = asyncio.get_event_loop()
    loop = [hello(10), hello(5)]
    asy.run_until_complete(asyncio.wait(loop))
    asy.close()
    print(time.ctime())
