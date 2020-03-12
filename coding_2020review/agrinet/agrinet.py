"""
ID: whuan2001
LANG: PYTHON2
TASK: agrinet
"""
def solution():
    fin = open("agrinet.in", "r")
    fout = open("agrinet.out", "w")
    N = int(fin.readline().strip())
    all_input = []
    for _ in range(N):
        arr = []
        while len(arr) < N:
            arr += map(int, fin.readline().strip().split())
        all_input.append(arr)
    points_dis = []
    for i in range(N):
        for j in range(i + 1, N):
            points_dis.append((all_input[i][j], (i, j)))
    points_dis = sorted(points_dis)
    all_lens = []
    for root in range(N):
        visited = set()
        visited.add(root)
        mini_len = 0
        while len(visited) < N:
            for item in points_dis:
                if item[1][0] not in visited and item[1][1] in visited:
                    mini_len += item[0]
                    visited.add(item[1][0])
                    break
                if item[1][1] not in visited and item[1][0] in visited:
                    mini_len += item[0]
                    visited.add(item[1][1])
                    break
        all_lens.append(mini_len)
        all_lens = sorted(all_lens)
    print >>fout, all_lens[0]
if __name__ == "__main__":
    solution()
                    