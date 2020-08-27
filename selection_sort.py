# python3
import sys


def swap_by_index(values, a, b):
    temp = values[a]
    values[a] = values[b]
    values[b] = temp


def selection_sort(values):
    for i in range(0, len(values)):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] <= values[min_index]:
                min_index = j
        swap_by_index(values, i, min_index)

    return values


if __name__ == '__main__':
    print(selection_sort(
        [4, 3, 2, 20, 18, 14, 1, 4, 3, 2, 20, 18, 14, 1, 4, 3, 2, 20, 18, 14, 1, 4, 3, 2, 20, 18, 14, 1]))
