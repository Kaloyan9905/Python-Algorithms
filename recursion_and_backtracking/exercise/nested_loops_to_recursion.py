def solution(number, index, array):
    if index == len(array):
        print(' '.join(str(x) for x in array))
        return

    for num in range(1, number + 1):
        array[index] = num
        solution(number, index + 1, array)


n = int(input())
solution(n, 0, [None] * n)
