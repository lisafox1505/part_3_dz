import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import reduce


def factorial_num(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x*y, range(1, n+1))


def funk_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        result_time = time.time() - start
        print(f"Time: {result_time}\n")
    return wrapper


@funk_time
def funk_start(func, arg):
    print("---Запуск через Threads---")
    thread_list = []
    for i in range(arg+1):
        thread = threading.Thread(target=func, args=(i,))
        thread.start()
        thread_list.append(thread)
    for thr in thread_list:
        thr.join()


@funk_time
def funk_start_with_concurrent_futures(func, arg):
    print("---Запуск через ThreadPoolExecutor---")
    with ThreadPoolExecutor() as executor:
        for _ in executor.map(func, range(arg+1)):
            pass


args_for_funk = [5, 100, 1000, 5000, 10000]

def check_speed(value):
    print(f"Значення: {value}")
    funk_start(factorial_num, value)
    funk_start_with_concurrent_futures(factorial_num, value)
    print("-"*30)


for arg in args_for_funk:
    check_speed(arg)
