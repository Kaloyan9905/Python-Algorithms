def solution(index, target, strings_count, strings_positions, used_words):
    if index >= len(target):
        print(*used_words, sep=' ')
        return

    if index not in strings_positions:
        return

    for word in strings_positions[index]:
        if strings_count[word] == 0:
            continue

        used_words.append(word)
        strings_count[word] -= 1

        solution(index + len(word), target, strings_count, strings_positions, used_words)

        used_words.pop()
        strings_count[word] += 1


strings = input().split(', ')
target = input()

strings_count = {}
strings_positions = {}

for string in strings:
    if string in strings_count:
        strings_count[string] += 1
        continue

    strings_count[string] = 1

    try:
        index = 0

        while True:
            index = target.index(string, index)

            if index not in strings_positions:
                strings_positions[index] = []

            strings_positions[index].append(string)
            index += len(string)
    except ValueError:
        pass

solution(0, target, strings_count, strings_positions, [])
