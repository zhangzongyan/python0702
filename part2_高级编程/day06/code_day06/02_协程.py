# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02_协程
   Description :
   Author :       zongyanzhang
   date：          2018/8/10
-------------------------------------------------
   Change Activity:
                   2018/8/10:
-------------------------------------------------
"""
__author__ = 'admin'

# coroutine

# 协程
def foo(n):
    index = 0

    while index < n:
        print("index:%d" % index)
        m = yield index
        index += m

if __name__ == '__main__':
    f = foo(10)
    # print(type(f))
    # print(next(f))
    # print(next(f))
    next(f) # f.send(None)
    ret = f.send(5)
    #print(ret)

