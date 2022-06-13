import type
import numpy as np

def sum(data):
    total = 0

    for i in data:
        if i is not None:
            total += i

    return total

def _sum(data):
    count = 0
    types  = set()

    for x in data:
        count += 1

    if None in data:
        total = data[None]
    else:
        total = sum(data)

    return (total, count)

def mean(data):
    if n < 1:
        print("data is empty")
    else:
        total, n = _sum(data)

    return (total / n)

def min(data):
    min_value = INT_MAX

    for i in data:
        if min_value > i:
            min_value = i

    return min_value

def max(data):
    max_value = INT_MIN

    for i in data:
        if max_value < i:
            max_value = i

    return max_value

def median(data):
    n = len(data)

    if n == 0:
        print("예외처리")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2


def variance(data):
    mean_value = mean(data)
    variance_arr = np.zeros(len(data))
    variance = 0

    for i in range(10):
        variance_arr[i] = data[i] - mean_value

    for i in variance_arr:
        variance += pow(i, 2)

    return variance / (len(data)-1)

