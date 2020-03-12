"""
ID: whuan2001
LANG: PYTHON2
TASK: holstein
"""
import copy
def solution():
    fin = open("holstein.in", "r")
    fout = open("holstein.out", "w")
    V = int(fin.readline().strip())
    requirements = map(int, fin.readline().strip().split())
    F = int(fin.readline().strip())
    scoops = []
    for line in fin.readlines():
        arr = map(int, line.strip().split())
        scoops.append(arr)
    feeds = []
    dfs(V, F, requirements, scoops, [0] * V, [], feeds)
    feeds = sorted(feeds)
    print feeds
    min_scoop = F
    brr = []
    for feed in feeds:
        if sum(feed) < min_scoop:
            min_scoop = sum(feed)
            brr[:] = []
            arr = []
            for i in range(len(feed)):
                if feed[i] == 1:
                    arr.append(i + 1)
            brr.append(arr)
        elif sum(feed) == min_scoop:
            arr = []
            for j in range(len(feed)):
                if feed[j] == 1:
                    arr.append(j + 1)
            brr.append(arr)
    brr = sorted(brr)
    res = [str(min_scoop)]
    for k in brr[0]:
        res.append(str(k))
    print >>fout, " ".join(res)
def dfs(V, F, requirements, scoops, cur, prefix, feeds):
    if is_satisfy(requirements, cur):
        feeds.append(copy.deepcopy(prefix))
        return
    else:
        if len(prefix) == F:
            return
        for i in range(2):
            if i == 0:
                prefix.append(0)
                dfs(V, F, requirements, scoops, cur, prefix, feeds)
                prefix.pop()
            else:
                for j in range(V):
                    cur[j] += scoops[len(prefix)][j]
                prefix.append(1)
                dfs(V, F, requirements, scoops, cur, prefix, feeds)
                prefix.pop()
                for j in range(V):
                    cur[j] -= scoops[len(prefix)][j]
def is_satisfy(requirements, cur):
    for i in range(len(requirements)):
        if cur[i] < requirements[i]:
            return False
    return True
if __name__ == "__main__":
    solution()
    