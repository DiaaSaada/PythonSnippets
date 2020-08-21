def fib(n):
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])

    return res


print(fib(110))