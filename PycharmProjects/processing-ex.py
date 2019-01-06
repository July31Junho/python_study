from multiprocessing import Process
import os
import math

def calc():
    for i in range(0,40000000):
        if i % 10000000 == 0:
            print(i , math.sqrt(i))
        math.sqrt(i)


if __name__ == '__main__':
    processes = []

    for i in range(os.cpu_count()):
        print('process 등록 %d ' % i)
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()