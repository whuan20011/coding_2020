"""
ID: whuan2001
LANG: PYTHON2
TASK: sprime
"""
import math
def solution():
    fin = open("sprime.in", "r")
    fout = open("sprime.out", "w")
    N = int(fin.readline().strip())
    arr = [2, 3, 5, 7]
    if N == 1:
        for num in arr:
            print >>fout, num
    res = []
    res.append(arr)
    i = 0
    while i < N - 1:
        brr = []
        for p in res[i]:
            for d in range(1, 10, 2):
                if is_prime(p * 10 + d):
                    brr.append(p * 10 + d)
        res.append(brr)
        i += 1
    for r in res[i]:
        print >>fout, r
def is_prime(num):
    mid = int(math.sqrt(num))
    for x in range(2, mid + 1):
        if num % x == 0:
            return False
    return True
if __name__ == "__main__":
    solution()
    