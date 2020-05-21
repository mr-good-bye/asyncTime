from time import time
from threading import Thread
import asyncio

def print_time_main(func, b):
    a = time()
    func(b)
    print("Main Thread: %.4f s" % (time()-a))


def hard_func(a):
    for i in range(int(a)):
        #print(((i/a)*100)//1)
        c = i/a


async def a_hard_func(a):
    for i in range(int(a)):
        #print(((i/a)*100)//1)
        c = i/a


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


def async_time_2(func,b):
    a = time()
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(func(b//2)),
        ioloop.create_task(func(b//2))
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
    print("Asyncio 2 tasks: %.4f s" % (time() - a))


if __name__ == "__main__":
    #print_time_main(hard_func, 200000000)
    #print_time_threading_2(hard_func, 200000000)
    #print_time_threading_5(hard_func, 200000000)
    #async_time_2(a_hard_func, 200000000)
