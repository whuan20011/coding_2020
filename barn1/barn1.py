"""
ID: whuan2001
LANG: PYTHON2
TASK: barn1
"""
def solution():
    fin = open("barn1.in", "r")
    fout = open("barn1.out", "w")
    max_purchase, total_stalls, occupied_stalls = map(int, fin.readline().strip().split(" "))
    stalls = []
    for stall in fin.readlines():
        stalls.append(int(stall.strip()))
    stalls = sorted(stalls)
    gaps = []
    for i in range(1, len(stalls)):
        gap = stalls[i] - stalls[i - 1] - 1
        if gap:
            gaps.append(gap)
    gaps = sorted(gaps, reverse=True)
    print >>fout, stalls[-1] - stalls[0] + 1 - sum(gaps[:(max_purchase - 1)])
if __name__ == "__main__":
    solution()
                