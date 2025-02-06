def sum_array(nums, index):
    if index == len(nums) - 1:
        return nums[index]

    return nums[index] + sum_array(nums, index + 1)


numbers = [int(num) for num in input().split()]
print(sum_array(numbers, 0))
