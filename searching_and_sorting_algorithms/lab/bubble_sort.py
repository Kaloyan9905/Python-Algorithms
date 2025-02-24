def bubble_sort(numbers):
    reduce_index = 0

    while True:
        sort_performed = False

        for index in range(len(numbers) - 1 - reduce_index):
            first_number = numbers[index]
            next_number = numbers[index + 1]

            if first_number > next_number:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                sort_performed = True

        reduce_index += 1

        if not sort_performed:
            break

    return ' '.join(str(x) for x in numbers)


numbers = [int(x) for x in input().split()]
print(bubble_sort(numbers))
