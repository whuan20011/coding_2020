"""
ID: whuan2001
LANG: PYTHON2
TASK: pprime
"""
import math
def solution():
    fin = open("pprime.in", "r")
    fout = open("pprime.out", "w")
    a, b = map(int, fin.readline().strip().split(" "))
    res = []
    if a < 10:
        for num in range(a, 10):
            if is_prime(num):
                res.append(num)
    palindromes = form_palindrome(a, b)
    for pal in palindromes:
        if is_prime(pal):
            res.append(pal)
    for r in res:
        print >>fout, r
def is_prime(num):
    mid = int(math.sqrt(num))
    for i in range(2, mid + 1):
        if num % i == 0:
            return False
    return True
def form_palindrome(a, b):
    palindromes = []
    for i in range(1, 10000):
        p = int(str(i) + str(i)[::-1])
        if p >= a and p <= b:
            palindromes.append(p)
        for j in range(10):
            q = int(str(i) + str(j) + str(i)[::-1])
            if q >= a and q <= b:
                palindromes.append(q)
    return palindromes
if __name__ == "__main__":
    solution()
     