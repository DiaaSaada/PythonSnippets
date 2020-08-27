# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    units = {}
    for i in range(len(values)):
        factor = values[i] / weights[i]

        units[factor] = i

    sorted_keys = sorted(units.keys(), reverse=True)

    total_weight = 0
    total_value = 0

    for key in sorted_keys:
        item = units[key]
        if weights[item] + total_weight <= capacity:
            total_weight += weights[item]
            total_value += values[item]
        else:
            total_value += (values[item] / weights[item]) * (capacity - total_weight)

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
