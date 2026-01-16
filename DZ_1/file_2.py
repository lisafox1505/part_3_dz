#5.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list)))
# print(result)

#6.
# def fibo_decorator(func):
#     def wrapper(*args):
#         result = func(*args)
#         for num in result:
#             if num % 2 == 0:
#                 yield num
#     return wrapper
#
# @fibo_decorator
# def fibonacci(n):
#     value_1, value_2 = 0, 1
#     for _ in range(n):
#         value_1, value_2 = value_2, value_1 + value_2
#         yield value_1
#
# fibonacci_iter = fibonacci(50)
# for i in fibonacci_iter:
#     print(i)

#7.
import functools

def multiplicar(a, b):
    return a * b

def multiplicar_curr(a):
    def multiplicar_curr_arg_2(b):
        return a * b
    return multiplicar_curr_arg_2

result_1 = functools.partial(multiplicar, b=2)
print(result_1(6))

result_2 = multiplicar_curr(6)
print(result_2(6))

print(multiplicar_curr(3)(6))