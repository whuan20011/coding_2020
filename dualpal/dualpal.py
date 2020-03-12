"""
ID: whuan2001
LANG: PYTHON2
TASK: dualpal
"""
def solution():
    fin = open("dualpal.in", "r")
    fout = open("dualpal.out", "w")
    N, S = map(int, fin.readline().strip().split(" "))
    num = S + 1
    res = []
    while num <= 1<<32 - 1:
        if is_dualpal(num):
            res.append(num)
        if len(res) == N:
            break
        num += 1
    for r in res:
        print >>fout, r
def is_dualpal(num):
    B = 2
    count = 0
    while B <= 10:
        if transfer(num, B):
            count += 1
        if count == 2:
            return True
        B += 1
    return False
def transfer(num, B):
    arr = []
    while num:
        arr.append(num % B)
        num /= B
    lens = len(arr)
    for i in range(lens / 2):
        if arr[i] != arr[lens - 1 - i]:
            return False
    return True
if __name__ == "__main__":
    solution()
              