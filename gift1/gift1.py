"""
ID: whuan2001
LANG: PYTHON2
TASK: gift1
"""
def solution():
    fin = open("gift1.in", "r")
    fout = open("gift1.out", "w")
    NP = int(fin.readline().strip())
    dic = {}
    names = []
    for _ in range(NP):
        name = fin.readline().strip()
        names.append(name)
        dic[name] = 0
    for _ in range(NP):
        giver = fin.readline().strip()
        money, receiver_number = map(int, fin.readline().strip().split())
        dic[giver] -= money
        if receiver_number != 0:
            dic[giver] += money % receiver_number
        for _ in range(receiver_number):
            receiver = fin.readline().strip()
            if receiver_number != 0:
                dic[receiver] += money / receiver_number
    for name in names:
        #print name, dic[name]
        print >>fout, name, dic[name]
if __name__ == "__main__":
    solution()
    