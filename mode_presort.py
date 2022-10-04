from turtle import mode
from typing import Counter


# def find_mode(arr):
#     mode = max(set(arr), key=arr.count)
#     return mode


def mode_presort(arr):
    arr.sort()
    i = 0
    mode_frequency = 0
    while i < len(arr):
        run_length = 1
        run_value = arr[i]
        while i + run_length < len(arr) and arr[i + run_length] == run_value:
            run_length += 1
        if run_length > mode_frequency:
            mode_frequency = run_length
            mode_value = [run_value]
        elif run_length == mode_frequency:
            mode_value.append(run_value)
        i += run_length
    return mode_value


arr = [1, 1, 1, 2, 3, 3]
print(find_mode(arr))
