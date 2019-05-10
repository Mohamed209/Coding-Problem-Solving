def binary_search(item, array):  # assume array is sorted
    # base case
    if len(array) == 1:
        return array[0] == item
    else:
        mid = len(array) // 2
        if item == array[mid]:
            return True
        elif item > array[mid]:
            return binary_search(item, array[mid:])
        elif item < array[mid]:
            return binary_search(item, array[:mid])


print(binary_search(5, [5, 6, 7, 8, 9]))
print(binary_search(50, [5, 6, 7, 8, 9]))
