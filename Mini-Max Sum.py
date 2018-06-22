import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_list=[0,0,0,0,0]
    for i in range(5):
        for j in range(i,i+4):
            sum_list[i]+=arr[j%5]
    print(min(sum_list),max(sum_list))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
