"""
ID: whuan2001
LANG: PYTHON2
TASK: comehome
"""
def solution():
    fin = open("comehome.in", "r")
    fout = open("comehome.out", "w")
    P = int(fin.readline().strip())
    graph = {}
    for _ in range(P):
        p1, p2, num = fin.readline().strip().split()
        if p1 not in graph:
            graph[p1] = {}
        if p2 not in graph:
            graph[p2] = {}
        length = int(num)
        length = min(length, graph[p1].get(p2, float('inf')))
        graph[p1][p2] = length
        graph[p2][p1] = length
    distance = dijkstra(graph, "Z")
    shortest = float('inf')
    for k in distance:
        if k.isupper() and k != "Z" and distance[k] < shortest:
            shortest = distance[k]
            fastest_cow = k
    print >>fout, fastest_cow, shortest
def dijkstra(graph, src):
    if not graph:
        return 0
    nodes = [node for node in graph]
    distance = {}
    for n in nodes:
        distance[n] = float('inf')
    distance[src] = 0
    while nodes:
        mid_dis = float('inf')
        mid_idx = src
        for d in nodes:
            if distance[d] < mid_dis:
                mid_dis = distance[d]
                mid_idx = d
        for v in graph[mid_idx]:
            distance[v] = min(distance[v], distance[mid_idx] + graph[mid_idx][v])
        if mid_idx not in nodes:
            break
        nodes.remove(mid_idx)
    return distance
if __name__ == "__main__":
    solution()
