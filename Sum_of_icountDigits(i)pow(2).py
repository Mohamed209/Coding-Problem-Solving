# problem : https://www.geeksforgeeks.org/sum-of-i-countdigitsi2-for-all-i-in-range-l-r/
def count_digits(n):
    digits=0
    while(n>0):
        digits=digits+1
        n=n//10
    return digits
def sum_of_i_count_digits(l,r):
    array=list(range(l,r+1))
    result=0
    for i in range(len(array)):
        result=result+array[i]*count_digits(array[i])**2
    return result
print(sum_of_i_count_digits(98,102))