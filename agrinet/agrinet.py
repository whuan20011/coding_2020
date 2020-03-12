"""
ID: whuan2001
LANG: PYTHON2
TASK: agrinet
"""
def solution():
    fin = open("agrinet.in", "r")
    fout = open("agrinet.out", "w")
    N = int(fin.readline().strip())
    matrix = []
    arr = []
    for line in fin.readlines():
        arr += map(int, line.strip().split())
        if len(arr) == N:
            matrix.append(arr)
            arr = []
    dis_points = []
    for i in range(N):
        for j in range(i + 1, N):
            dis_points.append([matrix[i][j], (i, j)])
    dis_points = sorted(dis_points)
    mini_lens = []
    for root in range(N):
        visited = set()
        visited.add(root)
        mini_len = 0
        while len(visited) < N:
            for d in dis_points:
                if d[1][0] in visited and d[1][1] not in visited:
                    mini_len += d[0]
                    visited.add(d[1][1])
                    break
                if d[1][0] not in visited and d[1][1] in visited:
                    mini_len += d[0]
                    visited.add(d[1][0])
                    break
        mini_lens.append(mini_len)
    res = mini_lens[0]
    for m in mini_lens:
        res = min(res, m)
    print >>fout, res
if __name__ == "__main__":
    solution()