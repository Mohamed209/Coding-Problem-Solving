# problem : https://www.geeksforgeeks.org/c-program-check-given-string-palindrome/
# solution using recursion with dequeu data structure
from collections import deque


def check_palindrom(deque_string, _palindrom=True):
    if len(deque_string) == 0 or len(deque_string) == 1 and _palindrom:
        return _palindrom
    elif deque_string.pop() != deque_string.popleft():
        _palindrom = False
        return _palindrom
    else:
        return check_palindrom(deque_string)


input_string = input()
de = deque(input_string)
print(check_palindrom(de))
