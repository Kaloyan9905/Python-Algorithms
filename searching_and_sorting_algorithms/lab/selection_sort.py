def selection_sort(numbers):
    index = 0

    while index < len(numbers):
        candidate = numbers[index]
        candidate_index = None

        for start_index in range(index + 1, len(numbers)):
            if numbers[start_index] < candidate:
                candidate = numbers[start_index]
                candidate_index = start_index

        if candidate_index is not None:
            tmp = numbers[index]
            numbers[index] = candidate
            numbers[candidate_index] = tmp

        index += 1

    return ' '.join(str(x) for x in numbers)


numbers = [int(x) for x in input().split()]
print(selection_sort(numbers))
