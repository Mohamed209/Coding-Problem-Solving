def validMountainArray(arr):
    # loop to find max
    if len(arr) < 3:
        return False
    validp1 = False
    validp2 = False
    top = arr.index(max(arr))
    for i in range(top):
        if arr[i] < arr[i+1]:
            validp1 = True
            continue
        else:
            return False
    for j in range(top, len(arr)-1):
        if arr[j] > arr[j+1]:
            validp2 = True
            continue
        else:
            return False

    return (validp1 and validp2)


print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
