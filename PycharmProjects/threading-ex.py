from threading import Thread
import os
import math

def calc():
    for i in range(0,40000000):
        if i % 10000000 == 0:
            print(i , math.sqrt(i))
        math.sqrt(i)

if __name__ == '__main__':
    threads = []

    for i in range(os.cpu_count()):
        print('thread 등록 %d' % i)
        threads.append(Thread(target=calc))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()