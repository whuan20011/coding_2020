"""
ID: whuan2001
LANG: PYTHON2
TASK: subset
"""
def solution():
    fin = open("subset.in", "r")
    fout = open("subset.out", "w")
    N = int(fin.readline().strip())
    total = N * (N + 1) / 2
    if total % 2 != 0:
        print >>fout, 0
    else:
        dic = {}
        res = dp(N, total, 0, 0, dic)
        print >>fout, res / 2
def dp(N, total, idx, cur_sum, dic):
    if (idx, cur_sum) in dic:
        return dic[(idx, cur_sum)]
    if cur_sum == total / 2:
        return 1
    if cur_sum > total / 2:
        return 0
    if idx == N:
        return 0
    res = dp(N, total, idx + 1, cur_sum + idx + 1, dic)
    res += dp(N, total, idx + 1, cur_sum, dic)
    dic[(idx, cur_sum)] = res
    return res
if __name__ == "__main__":
    solution()
        