"""
ID: whuan2001
LANG: PYTHON2
TASK: wormhole
"""
def solution():
    fin = open("wormhole.in", "r")
    fout = open("wormhole.out", "w")
    N = int(fin.readline().strip())
    points = []
    for line in fin.readlines():
        x, y = line.strip().split(" ")
        points.append((x, y))
    all_pairs = []
    form_pairs(points, {}, all_pairs)
    points = sorted(points, key = lambda m: (m[1], m[0]))
    right = {}
    for i in range(len(points) - 1):
        if points[i][1] == points[i + 1][1]:
            right[points[i]] = points[i + 1]
    res = 0
    for pairs in all_pairs:
        if has_circle(pairs, right):
            res += 1
    print >>fout, res
def form_pairs(points, prefix, all_pairs):
    if len(prefix) == len(points):
        all_pairs.append(prefix)
        return
    for i in range(len(points)):
        if points[i] not in prefix:
            break
    for j in range(i + 1, len(points)):
        if points[j] not in prefix:
            new_prefix = prefix.copy()
            new_prefix[points[i]] = points[j]
            new_prefix[points[j]] = points[i]
            form_pairs(points, new_prefix, all_pairs)
def has_circle(pairs, right):
    for pair in pairs:
        visited = set()
        while pair in right:
            if pair not in visited:
                visited.add(pair)
            else:
                return True
            pair = pairs[right[pair]]
    return False
if __name__ == "__main__":
    solution()
         