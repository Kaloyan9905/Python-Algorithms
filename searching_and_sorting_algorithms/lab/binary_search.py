def binary_search(numbers, target, left, right):
    while left <= right:
        middle_index = (left + right) // 2
        middle_element = numbers[middle_index]

        if middle_element == target:
            return middle_index

        if middle_element > target:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return -1


# def binary_search(numbers, target, left, right):
#     middle_index = (left + right) // 2
#     middle_element = numbers[middle_index]
#
#     if left > right:
#         return -1
#
#     if middle_element == target:
#         return middle_index
#
#     if middle_element > target:
#         return binary_search(numbers, target, left, right - 1)
#
#     return binary_search(numbers, target, left + 1, right)


numbers = [int(x) for x in input().split()]
target = int(input())

left = 0
right = len(numbers) - 1

print(binary_search(numbers, target, left, right))
