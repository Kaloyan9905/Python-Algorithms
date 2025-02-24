def insertion_sort(numbers):
    for index in range(len(numbers)):
        reduce_index = index

        while reduce_index > 0 and numbers[reduce_index] < numbers[reduce_index - 1]:
            numbers[reduce_index], numbers[reduce_index - 1] \
                = numbers[reduce_index - 1], numbers[reduce_index]
            reduce_index -= 1

    return ' '.join(str(x) for x in numbers)


numbers = [int(x) for x in input().split()]
print(insertion_sort(numbers))

# 3 2 1 5 7 4
# 2 3 1
# 1 2 3
