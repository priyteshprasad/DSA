from email.policy import default


import random


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(10):
    print(fibonacci(i), end=',')

puzzle_nums = random.sample(range(100), 5)
print(puzzle_nums)
