
import multiprocessing


def childjob(n, l, d, ls):
    n  = 100
    for i in range(len(l)):
        l[i] += 1
    d['name'] = "python"
    d['age'] = 20
    ls.append(10)
    ls.append(20)

if __name__ == '__main__':
    # 创建一个进程间共享的整型变量
    num = multiprocessing.Value('i', 1)
    l = multiprocessing.Array('i', [1,3,4])
    mng = multiprocessing.Manager()

    dt = mng.dict()
    ls = mng.list()

    p = multiprocessing.Process(target=childjob, args=(num, l, dt, ls))

    p.start()
    p.join()

    print(num.value)

    for i in l:
        print(i)

    print(dt)
    print(ls)