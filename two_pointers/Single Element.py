nums = [3, 3, 7, 7, 10, 11]


def find_the_single(nums):
    # using two pointers (sliding window fixed size 2)
    # edge case single element in nums
    if len(nums) == 1:
        return nums[0]
    left_pointer = 0
    right_pointer = 1
    while left_pointer < len(nums)-1 and right_pointer < len(nums):
        if nums[left_pointer] != nums[right_pointer]:
            return nums[left_pointer]
        left_pointer += 2
        right_pointer += 2
    # case no signle element
    return -1


print(find_the_single(nums))
