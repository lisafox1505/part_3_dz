import functools
import time

#2.
def function_running_time(funk):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funk(*args, **kwargs)
        end = time.time()
        run_time = end - start
        return f"{result}\nЧас виконання: {run_time}\n"
    return wrapper

#3-4.

def fibonacci_non_cach(n):
    if n < 2:
        return n
    return fibonacci_non_cach(n - 1) + fibonacci_non_cach(n - 2)

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper


@cache
def fibonacci_cache_without_limitation(n):
    if n < 2:
        return n
    return fibonacci_cache_without_limitation(n - 1) + fibonacci_cache_without_limitation(n - 2)


@functools.lru_cache(maxsize=10)
def fibonacci_cache_max10(n):
    if n < 2:
        return n
    return fibonacci_cache_max10(n - 1) + fibonacci_cache_max10(n - 2)


@functools.lru_cache(maxsize=16)
def fibonacci_cache_max16(n):
    if n < 2:
        return n
    return fibonacci_cache_max16(n - 1) + fibonacci_cache_max16(n - 2)

@function_running_time
def function_run(funk, x):
    result_list = list()
    for i in range(x):
        result_list.append(funk(i))
    return f"Результат функції {funk.__name__}: {result_list}"

print(function_run(fibonacci_non_cach, 25))
print(function_run(fibonacci_cache_without_limitation, 25))
print(function_run(fibonacci_cache_max10, 25))
print(function_run(fibonacci_cache_max16, 25))
