def get_min(array):
    min = array[0]
    for item in array:
        if item < min:
            min = item
    return min


def get_max(array):
    max = array[0]
    for item in array:
        if item > max:
            max = item
    return max


def sort(array, ascend=True):
    sorted = []
    if ascend:
        while array:
            min = get_min(array)
            array.remove(min)
            sorted.append(min)
        return sorted
    elif not ascend:
        while array:
            max = get_max(array)
            array.remove(max)
            sorted.append(max)
        return sorted


print(sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(sort([54, 26, 93, 17, 77, 31, 44, 55, 20], ascend=False))
