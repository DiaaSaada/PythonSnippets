# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    refils = 0
    last_refile_km = 0
    for i in range(0, len(stops)):

        if stops[i] > last_refile_km + tank:
            return -1

        for j in range(i, len(stops) - 1):

            if stops[j + 1] > last_refile_km + tank:
                last_refile_km = stops[j]
                refils += 1
                i = j

                break

    return refils


if __name__ == '__main__':
    distance1, tank1, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(distance1, tank1, stops))
