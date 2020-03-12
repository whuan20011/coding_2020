"""
ID: whuan2001
LANG: PYTHON2
TASK: runround
"""
def solution():
    fin = open("runround.in", "r")
    fout = open("runround.out", "w")
    M = int(fin.readline().strip())
    for i in xrange(M + 1, M + 1000000):
        arr = []
        tag = 0
        num = i
        while num:
            k = num % 10
            if k == 0:
                tag = 1
                break
            if k in arr:
                tag = 1
                break
            arr.append(k)
            num /= 10
        if tag == 1:
            continue
        arr = arr[::-1]
        if is_runround(i, arr):
            print >>fout, i
            break
def is_runround(num, arr):
    brr = [arr[0]]
    idx = arr[0] % len(arr)
    while idx != 0 and arr[idx] not in brr:
        brr.append(arr[idx])
        idx = (idx + arr[idx]) % len(arr)
    if idx == 0 and set(brr) == set(arr):
        return True
    else:
        return False
if __name__ == "__main__":
    solution()
        