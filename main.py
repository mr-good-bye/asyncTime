from time import time
from threading import Thread
import asyncio
import multiprocessing as mp


NUM = 2000000


def print_time_main(func, b):
    a = time()
    func(b)
    print("Main Thread: %.4f s" % (time()-a))


def hard_func(a):
    for i in range(a):
        yfff = i**2 + i**4 - i**3


async def a_hard_func(a):
    for i in range(a):
        yfff = i**2 + i**4 - i**3


def print_time_threading_2(func,b):
    a = time()
    t1 = Thread(target=func, args=(int(b//2),))
    t2 = Thread(target=func, args=(int(b//2),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Two Threads: %.4f s" % (time() - a))


def print_time_threading_5(func,b):
    a = time()
    t1 = Thread(target=func, args=(int(b//5),))
    t2 = Thread(target=func, args=(int(b//5),))
    t3 = Thread(target=func, args=(int(b // 5),))
    t4 = Thread(target=func, args=(int(b // 5),))
    t5 = Thread(target=func, args=(int(b // 5),))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print("Five Threads: %.4f s" % (time() - a))


def async_time_4(func,b):
    a = time()
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(func(b//4)),
        ioloop.create_task(func(b//4)),
        ioloop.create_task(func(b//4)),
        ioloop.create_task(func(b//4))
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
    print("Asyncio 4 tasks: %.4f s" % (time() - a))


def mp_time_1(func, b):
    a = time()
    pr = list()
    for i in range(1):
        proc = mp.Process(target=func,args=(b//2,))
        pr.append(proc)
        proc.start()
    for i in pr:
        i.join()
    print("Multiprocessing 1: %.4f s" % (time()-a))


def mp_time_2(func, b):
    a = time()
    pr = list()
    for i in range(2):
        proc = mp.Process(target=func,args=(b//2,))
        pr.append(proc)
        proc.start()
    for i in pr:
        i.join()
    print("Multiprocessing 2: %.4f s" % (time()-a))


def mp_time_4(func, b):
    a = time()
    pr = list()
    for i in range(4):
        proc = mp.Process(target=func,args=(b//4,))
        pr.append(proc)
        proc.start()
    for i in pr:
        i.join()
    print("Multiprocessing 4: %.4f s" % (time()-a))


if __name__ == "__main__":
    print_time_main(hard_func, NUM)
    print_time_threading_2(hard_func, NUM)
    print_time_threading_5(hard_func, NUM)
    async_time_4(a_hard_func, NUM)
    mp_time_1(hard_func, NUM)
    mp_time_2(hard_func, NUM)
    mp_time_4(hard_func, NUM)

