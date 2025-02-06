def display_first_half(num):
    print('*' * num)


def display_second_half(num):
    print('#' * num)


def draw_figure(num):
    if num == 0:
        return num

    display_first_half(num)
    draw_figure(num - 1)
    display_second_half(num)


n = int(input())
draw_figure(n)
