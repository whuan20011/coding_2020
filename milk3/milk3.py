"""
ID: whuan2001
LANG: PYTHON2
TASK: milk3
"""
def solution():
    fin = open("milk3.in", "r")
    fout = open("milk3.out", "w")
    capacity = map(int, fin.readline().strip().split(" "))
    milk = (0, 0, capacity[2])
    visited = set()
    recursive(capacity, milk, visited)
    res = []
    for v in visited:
        if v[0] == 0:
            res.append(v[2])
    res = sorted(res)
    res = map(str, res)
    print >>fout, " ".join(res)
def recursive(capacity, milk, visited):
    if milk in visited:
        return
    else:
        visited.add(milk)
        for i in range(3):
            for j in range(3):
                if i != j:
                    new_milk = list(milk)
                    pour = min(milk[i], capacity[j] - milk[j])
                    new_milk[i] -= pour
                    new_milk[j] += pour
                    recursive(capacity, tuple(new_milk), visited)
if __name__ == "__main__":
    solution()
                      