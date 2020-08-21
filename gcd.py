# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def euclidean_gcd(a, b):

    if b == 1:
        return 1

    if b == 0:
        return a

    a1 = a % b

    return euclidean_gcd(b, a1)


if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    min = min(a, b)
    max = max(a, b)
    print(euclidean_gcd(max, min))
