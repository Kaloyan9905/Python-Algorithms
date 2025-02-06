def generate_vector(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generate_vector(index + 1, vector)


n = int(input())
vector = [0] * n
generate_vector(0, vector)
