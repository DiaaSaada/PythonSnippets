# python3
import sys


def fill_knapsack(knapsack, weights, values):
    units = {}
    for i in range(len(values)):
        factor = values[i] / weights[i]
        if factor not in units:
            units[factor] = []
        units[factor].append(i)
    print(units)

    sorted_keys = sorted(units.keys(), reverse=True)
    print(sorted_keys)
    amountW = 0
    amountV = 0
    for i in sorted_keys:
        for j in units[i]:
            if amountW < knapsack :
                amountW += weights[j]
                amountV += values[j]
                print("{amountW} => {amountV}")


    return amountV


if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.readline().split())
    print(fill_knapsack(5, [4, 3, 2], [20, 18, 14]))
