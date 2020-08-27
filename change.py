# Uses python3
import sys


def get_change(amount):
    coins = [10, 5, 1]
    res = {}
    res_count = 0
    remain = amount
    for coin in coins:
        res[str(coin)] = int(remain / coin)
        res_count += int(remain / coin)
        remain = remain % coin
        if remain == 0:

            return res_count
    print(res)
    return res_count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
