from collections import deque
from bisect import bisect_left, bisect_right
import math
import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


data = deque([2, 3, 4])
data.popleft()
data.appendleft(1)
print(data)

math.factorial(5)
math.sqrt(7)
math.gcd(21, 14)
math.pi
