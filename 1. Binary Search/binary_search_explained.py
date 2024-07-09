# low and high keep track of which part of the list you’ll search in.
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

# While you haven’t narrowed it down to one element . . .
    while low <= high:
        # . . . check the middle element.
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item: # Found the item.
            return mid
        elif guess > item: # The guess was too high.
            high = mid - 1
        else: # The guess was too low.
            low = mid + 1
    return None # The item doesn’t exist.

my_list = [1, 3, 5, 7, 9]

# Remember, lists start at 0. The second slot has index 1.
print(binary_search(my_list, 3)) # 1

# None means null in Python. It indicates that the item wasn’t found.
print(binary_search(my_list, -1)) # None