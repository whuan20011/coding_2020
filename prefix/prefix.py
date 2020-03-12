"""
ID: whuan2001
LANG: PYTHON2
TASK: prefix
"""
def solution():
    fin = open("prefix.in", "r")
    fout = open("prefix.out", "w")
    primitives = set()
    all_inputs = fin.readlines()
    longest_pri = 0
    for i, line in enumerate(all_inputs):
        if line.strip() == '.':
            break
        for primitive in line.strip().split():
            primitives.add(primitive)
            longest_pri = max(longest_pri, len(primitive))
    S = ""
    for j in range(i + 1, len(all_inputs)):
        S += all_inputs[j].strip()
    dic = {}
    for idx in range(len(S), -1, -1):
        dp(primitives, S, longest_pri, idx, dic)
    print >>fout, dic[0]
def dp(primitives, S, longest_pri, idx, dic):
    if idx in dic:
        return dic[idx]
    max_pri = idx
    for i in range(1, longest_pri + 1):
        if idx + i <= len(S):
            if S[idx:idx + i] in primitives:
                res = dp(primitives, S, longest_pri, idx + i, dic)
                max_pri = max(max_pri, res)
    dic[idx] = max_pri
    return max_pri
if __name__ == "__main__":
    solution()
                      