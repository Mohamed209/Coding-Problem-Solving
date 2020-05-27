# problem : https://www.hackerrank.com/challenges/missing-numbers/problem
def missingNumbers(arr, brr):
    arr.extend(brr)
    frequency_map = {}
    missing = []
    for element in arr:
        if element in frequency_map:
            frequency_map[element] += 1
        else:
            frequency_map[element] = 1
    for key in frequency_map:
        if frequency_map[key] % 2 != 0:
            missing.append(key)
    return sorted(missing)


print(missingNumbers([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3]))
