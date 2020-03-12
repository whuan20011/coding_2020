"""
ID: whuan2001
LANG: PYTHON2
TASK: skidesign
"""
def solution():
    fin = open("skidesign.in", "r")
    fout = open("skidesign.out", "w")
    N = int(fin.readline().strip())
    hills = []
    for hill in fin.readlines():
        hills.append(int(hill.strip()))
    hills = sorted(hills)
    res = 100000000
    for left in range(84):
        right = left + 17
        cost = 0
        for h in hills:
            if h < left:
                cost += (left - h) * (left - h)
            if h > right:
                cost += (h - right) * (h - right)
        res = min(res, cost)
    print >>fout, res
if __name__ == "__main__":
    solution()
                