def reverse_array(arr, first_index, last_index):
    if first_index >= last_index:
        return

    arr[first_index], arr[last_index] = arr[last_index], arr[first_index]
    return reverse_array(arr, first_index + 1, last_index - 1)


numbers = [int(x) for x in input().split()]
reverse_array(numbers, 0, len(numbers) - 1)

print(' '.join(str(x) for x in numbers))
