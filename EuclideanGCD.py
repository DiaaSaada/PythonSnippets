def euclidean_gcd(a, b):
    if b <= 1:
        return a
    a1 = a % b

    return euclidean_gcd(b, a1)


print(euclidean_gcd(32, 24))
