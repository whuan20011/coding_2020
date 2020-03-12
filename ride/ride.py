"""
ID: whuan2001
LANG: PYTHON2
TASK: ride
"""
def solution():
    fin = open("ride.in", "r")
    fout = open("ride.out", "w")
    group = str(fin.readline().strip())
    comet = str(fin.readline().strip())
    a = 1
    b = 1
    for g in group:
        a = (a * (ord(g) - 64)) % 47
    for c in comet:
        b = (b * (ord(c) - 64)) % 47
    if a == b:
        print >>fout, "GO"
    else:
        print >>fout, "STAY"
if __name__ == "__main__":
    solution()      
