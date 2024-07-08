# explanation by Kylie Ying on YouTube
# Binary Search vs Linear Search (or naive search)

# The list [1, 3, 6, 7, 9, 12, 13] (the list variable will be named 'L',
# and the target which is 12 will be named as 'target')

import random
import time

# Implement naive search
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i

    return -1 # we will return -1 if the target is not found

# Implement binary search
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0 # meaning index starts at 0
    if high is None:
        high = len(l) - 1
        # meaning index for the last element has lower number than the length of the list

    if high < low: # if the target is not found
        return -1

    midpoint = (low + high) // 2 # two slash means floor division (round the number)

    if l[midpoint] == target:
        return midpoint # target found
    elif target < l[midpoint]:
        new_high = midpoint - 1
        # use recursion
        return binary_search(l, target, low, new_high)
    else:
        # target > l[midpoint]
        new_low = midpoint + 1
        return binary_search(l, target, new_low, high)

if __name__ == '__main__':
    ''' l = [1, 3, 6, 7, 9, 12, 13]
    target = 12
    print(naive_search(l, target))

    print(binary_search(l, target)) '''

    length = 10000
    sorted_list = set() # using set to avoid duplicate numbers
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    target_list = [random.randint(-3*length, 3*length) for _ in range(length)]

    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")
    #result: 5.109922409057617 seconds

    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")
    # result: 0.05025172233581543 seconds