# python3
import sys


# # Distribute N black balls among 10 boxes so that every two boxes have different number of balls (you can put 0
# balls in some box if you want to). Fill in numbers of black balls in each box below.

def balls(n):
    my_list = []

    max = (n / 10) * 2
    if isinstance(max, int):
        return -1

    for i in range(5):
        my_list.append(i)
        my_list.append(max - i)

    # print(my_list)
    return my_list


if __name__ == '__main__':
    print(balls(31))
