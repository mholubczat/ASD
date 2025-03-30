NOT_FOUND = -1


def find(array, key):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if array[middle] == key:
            return middle
        if array[middle] > key:
            right = middle
        else:
            left = middle + 1
    return NOT_FOUND
