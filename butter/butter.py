"""
ID: whuan2001
LANG: PYTHON2
TASK: butter
"""
def solution():
    fin = open("butter.in", "r")
    fout = open("butter.out", "w")
    N, P, C = map(int, fin.readline().strip().split())
    cow_in_pasture = []
    for _ in range(N):
        cow_in_pasture.append(int(fin.readline().strip()))
    graph = {}
    for line in fin.readlines():
        a, b, dis = map(int, line.strip().split())
        if a not in graph:
            graph[a] = {}
        graph[a][b] = dis
        if b not in graph:
            graph[b] = {}
        graph[b][a] = dis
    res = float('inf')
    for i in range(1, P + 1):
        distances = dijkstra(graph, i)
        cur_dis = 0
        for j in cow_in_pasture:
            cur_dis += distances[j]
        res = min(res, cur_dis)
    print >>fout, res
def dijkstra(graph, src):
    if not graph:
        return 0
    nodes = []
    for k in range(len(graph)):
        nodes.append(k + 1)
    distance = {}
    for node in nodes:
        distance[node] = float('inf')
    distance[src] = 0
    while nodes:
        mid_distance = float('inf')
        mid_idx = src
        for d in nodes:
            if distance[d] < mid_distance:
                mid_distance = distance[d]
                mid_idx = d
        for v in graph[mid_idx]:
            distance[v] = min(distance[v], distance[mid_idx] + graph[mid_idx][v])
        if not mid_idx:
            break
        nodes.remove(mid_idx)
    return distance
if __name__ == "__main__":
    solution()
       