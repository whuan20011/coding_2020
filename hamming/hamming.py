"""
ID: whuan2001
LANG: PYTHON2
TASK: hamming
"""
def solution():
    fin = open("hamming.in", "r")
    fout = open("hamming.out", "w")
    N, B, D = map(int, fin.readline().strip().split())
    res = [0]
    for i in range(1, 1<<B):
        tag = 0
        for num in res:
            if not distance(num, i, B, D):
                tag = 1
                break
        if tag == 0:
            res.append(i)
        if len(res) == N:
            break
    for j in range(len(res)):
        res[j] = str(res[j])
    if N <= 10:
        print >>fout, " ".join(res)
    else:
        for h in range(N / 10):
            print >>fout, " ".join(res[(h * 10):(h * 10 + 10)])
        if N % 10 != 0:
            print >>fout, " ".join(res[((h + 1) * 10):])
def distance(x, y, B, D):
    bx = binary(x, B)
    by = binary(y, B)
    count = 0
    for i in range(B):
        if bx[i] != by[i]:
            count += 1
        if count >= D:
            return True
    return False
def binary(num, B):
    if num == 0:
        return [0] * B
    else:
        arr = []
        while num:
            arr.append(num % 2)
            num /= 2
        if len(arr) < B:
            arr += [0] * (B - len(arr))
        return arr[::-1]
if __name__ == "__main__":
    solution()
