# Uses python3
import sys


def euclidean_gcd(a, b):
    if b == 1:
        return 1

    if b == 0:
        return a

    a1 = a % b

    return euclidean_gcd(b, a1)


def lcm(a, b):
    return int(a * b / euclidean_gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(max(a, b), min(a, b)))
