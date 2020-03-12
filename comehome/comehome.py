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
        src, dst, length = fin.readline().strip().split()
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        length = min(int(length), graph[src].get(dst, float('inf')))
        graph[src][dst] = int(length)
        graph[dst][src] = int(length)
    dic = dijkstra(graph, "Z")
    shortest_path = float("inf")
    for dst in dic:
        if dst.isupper() and dst != "Z" and dic[dst] < shortest_path:
            shortest_path = dic[dst]
            nearest_cow = dst
    print >>fout, nearest_cow, shortest_path
def dijkstra(graph, src):
    if not graph:
        return 0
    nodes = [char for char in graph]
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
        if mid_idx not in nodes:
            break
        nodes.remove(mid_idx)
    return distance
if __name__ == "__main__":
    solution()
    