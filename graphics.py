import matplotlib.pyplot as plt
import main
from tqdm import tqdm


num_mt, time_mt, num_t2, time_t2, num_t5, time_t5, num_a4, \
time_a4, num_mp1, time_mp1, num_mp2, time_mp2, num_mp4, \
time_mp4 = list(), list(), list(), list(), list(), \
           list(), list(), list(), list(), list(), \
           list(), list(), list(), list()

if __name__ == "__main__":
    for i in tqdm(range(10)):
        num = 500000 * i
        num_mt.append(num)
        time_mt.append(main.print_time_main(main.hard_func, num))
        num_t2.append(num)
        time_t2.append(main.print_time_threading_2(main.hard_func, num))
        num_t5.append(num)
        time_t5.append(main.print_time_threading_5(main.hard_func, num))
        #num_a4.append(num)
        #time_a4.append(main.async_time_4(main.a_hard_func, num))
        num_mp1.append(num)
        time_mp1.append(main.mp_time_1(main.hard_func, num))
        num_mp2.append(num)
        time_mp2.append(main.mp_time_2(main.hard_func, num))
        num_mp4.append(num)
        time_mp4.append(main.mp_time_4(main.hard_func, num))


    plt.plot(num_mt, time_mt, 'b', label='Main Thread')
    plt.plot(num_t2, time_t2, 'g', label='2 Threads')
    plt.plot(num_t5, time_t5, 'r', label='5 Thread')
    #plt.plot(num_a4, time_a4, 'c', label='asyncio 4 tasks')
    plt.plot(num_mp1, time_mp1, 'm', label='multiprocessing 1 process')
    plt.plot(num_mp2, time_mp2, 'y', label='multiprocessing 2 processes')
    plt.plot(num_mp4, time_mp4, 'k', label='multiprocessing 4 processes')
    plt.legend()
    plt.savefig('graphicBIGNUM.png', format='png')
    plt.savefig('graphicBIGNUM.pdf', format='pdf')
    plt.show()
