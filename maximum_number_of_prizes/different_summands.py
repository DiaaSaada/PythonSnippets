# Uses python3
import sys


def optimal_summands(n):
    summands = []
    total = 0
    if n < 3:
        return [n]

    for i in range(1, n):
        if total + i < n:
            total += i
            summands.append(i)
        elif total + i == n:
            summands.append(i)
            return summands
        else:
            rem = total+i-n
            summands.remove(rem)
            total -= rem
            total += i
            summands.append(i)
            return summands

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
