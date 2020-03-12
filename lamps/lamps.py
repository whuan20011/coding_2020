"""
ID: whuan2001
LANG: PYTHON2
TASK: lamps
"""
def solution():
    fin = open("lamps.in", "r")
    fout = open("lamps.out", "w")
    N = int(fin.readline().strip())
    C = int(fin.readline().strip())
    on = map(int, fin.readline().strip().split())
    on.pop()
    off = map(int, fin.readline().strip().split())
    off.pop()
    states = []
    if C >= 4:
        for num in range(16):
            temp = []
            while num:
                temp.append(num % 2)
                num /= 2
            temp += [0] * (4 - len(temp))
            states.append(temp[::-1])
    if C == 1:
        states = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    if C == 2:
        states = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]]
    if C == 3:
        states = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0],[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    if C == 0:
        states = [[0, 0, 0, 0]]
    res = []
    for state in states:
        lights = [1] * N
        if state[0] == 1:
            for j in range(N):
                if lights[j] == 0:
                    lights[j] = 1
                else:
                    lights[j] = 0
        if state[1] == 1:
            for j in range(N):
                if j % 2 == 0:
                    if lights[j] == 0:
                        lights[j] = 1
                    else:
                        lights[j] = 0
        if state[2] == 1:
            for j in range(N):
                if j % 2 == 1:
                    if lights[j] == 0:
                        lights[j] = 1
                    else:
                        lights[j] = 0
        if state[3] == 1:
            for j in range(N):
                if j % 3 == 0:
                    if lights[j] == 0:
                        lights[j] = 1
                    else:
                        lights[j] = 0
        if is_satisfy(on, off, lights):
            if lights not in res:
                res.append(lights)
    if not res:
        print >>fout, 'IMPOSSIBLE'
    res = sorted(res)
    for l in res:
        string = ""
        for h in range(N):
            string += str(l[h])
        print >>fout, string
def is_satisfy(on, off, lights):
    for i in on:
        if lights[i - 1] == 0:
            return False
    for j in off:
        if lights[j - 1] == 1:
            return False
    return True
if __name__ == "__main__":
    solution()
    