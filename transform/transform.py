"""
ID: whuan2001
LANG: PYTHON2
TASK: transform
"""
def solution():
    fin = open("transform.in", "r")
    fout = open("transform.out", "w")
    N = int(fin.readline().strip())
    original = []
    afterwards = []
    for _ in range(N):
        ori = []
        for o in fin.readline().strip():
            ori.append(o)
        original.append(ori)
    for _ in range(N):
        aft = []
        for a in fin.readline().strip():
            aft.append(a)
        afterwards.append(aft)
    first = transform(original, N)
    if first == afterwards:
        print >>fout, 1
        return
    second = transform(first, N)
    if second == afterwards:
        print >>fout, 2
        return
    third = transform(second, N)
    if third == afterwards:
        print >>fout, 3
        return
    fourth = reflect(original, N)
    if fourth == afterwards:
        print >>fout, 4
        return
    fifth_1 = transform(fourth, N)
    if fifth_1 == afterwards:
        print >>fout, 5
        return
    fifth_2 = transform(fifth_1, N)
    if fifth_2 == afterwards:
        print >>fout, 5
        return
    fifth_3 = transform(fifth_2, N)
    if fifth_3 == afterwards:
        print >>fout, 5
        return
    if original == afterwards:
        print >>fout, 6
        return
    print >>fout, 7
def transform(graph, N):
    middle = []
    for _ in range(N):
        arr = []
        for _ in range(N):
            arr.append('a')
        middle.append(arr)
    for i in range(N):
        for j in range(N):
            middle[j][N-1-i] = graph[i][j]
    return middle
def reflect(graph, N):
    middle = []
    for _ in range(N):
        arr = []
        for _ in range(N):
            arr.append('a')
        middle.append(arr)
    for i in range(N):
        for j in range(N):
            middle[i][N-1-j] = graph[i][j]
    return middle
if __name__ == "__main__":
    solution()
        