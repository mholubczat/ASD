import math

NOT_FOUND = -1


def find(array, key):
    length = len(array)
    leap = int(math.sqrt(length))
    index = leap - 1
    while 0 <= index < length:
        if array[index] == key:
            return index
        if array[index] > key:
            return iterate(array, index - leap + 1, index, key)
        else:
            index += leap
    return iterate(array, index - leap + 1, index, key)


def iterate(array, start, end, key):
    for i in range(start, min(end, len(array))):
        if array[i] == key:
            return i
        if array[i] > key:
            return NOT_FOUND
    return NOT_FOUND
