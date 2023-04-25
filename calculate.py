import asyncio
import time
import math
import json
import multiprocessing as mp
from threading import Thread

res = {}
nums = {
    '10e1': int(10e1),
    '10e2': int(10e2),
    '10e3': int(10e3),
    '10e4': int(10e4),
    '10e5': int(10e5),
    '10e6': int(10e6),
    '10e7': int(10e7),
    '10e8': int(10e8)
}


def test(n, start=0):
    for i in range(start, n):
        _ = math.sqrt(i) + math.sin(i)
        _ += 1


async def atest(n, start=0):
    for i in range(start, n):
        _ = math.sqrt(i) + math.sin(i)
        _ += 1


def run_single():
    for n in nums:
        start = time.time()
        test(nums[n])
        end = time.time()-start
        print(f'one {n} - {end}'.rjust(32))
        res[f'one {n}'] = end


def run_2_threads():
    for n in nums:
        start = time.time()
        a1 = nums[n]//2
        t1 = Thread(target=test, args=(a1,))
        t2 = Thread(target=test, args=(nums[n], a1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end = time.time()-start
        print(f't2 {n} - {end}'.rjust(32))
        res[f't2 {n}'] = end


def run_6_threads():
    for n in nums:
        t = []
        for i in range(6):
            start = (nums[n]//6) * i
            end = (nums[n]//6) * (i+1)
            t.append(Thread(target=test, args=(end, start)))
        start = time.time()
        for _t in t:
            _t.start()
        for _t in t:
            _t.join()
        end = time.time()-start
        print(f't6 {n} - {end}'.rjust(32))
        res[f't6 {n}'] = end


async def run_asyncio():
    for n in nums:
        ioloop = asyncio.get_event_loop()
        t = []
        for i in range(6):
            start = (nums[n]//6) * i
            end = (nums[n]//6) * (i+1)
            task = atest(end, start)
            t.append(task)
        start = time.time()
        await asyncio.gather(*t)
        end = time.time()-start
        print(f'async_6 {n} - {end}'.rjust(32))
        res[f'async_6 {n}'] = end


def run_mp_2():
    for n in nums:
        pr = []
        for i in range(2):
            start = (nums[n]//2) * i
            end = (nums[n]//2) * (i+1)
            pr.append(mp.Process(target=test, args=(end, start)))
        start = time.time()
        for p in pr:
            p.start()
        for p in pr:
            p.join()
        end = time.time()-start
        print(f'mp_2 {n} - {end}'.rjust(32))
        res[f'mp_2 {n}'] = end


def run_mp_6():
    for n in nums:
        pr = []
        for i in range(6):
            start = (nums[n]//6) * i
            end = (nums[n]//6) * (i+1)
            pr.append(mp.Process(target=test, args=(end, start)))
        start = time.time()
        for p in pr:
            p.start()
        for p in pr:
            p.join()
        end = time.time()-start
        print(f'mp_6 {n} - {end}'.rjust(32))
        res[f'mp_6 {n}'] = end


if __name__ == "__main__":
    run_single()
    run_2_threads()
    run_6_threads()
    mp.freeze_support()
    run_mp_2()
    run_mp_6()
    asyncio.run(run_asyncio())
    with open('res.json', 'w') as file:
        json.dump(res, file)
    print(res)
