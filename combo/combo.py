"""
ID: whuan2001
LANG: PYTHON2
TASK: combo
"""
def solution():
    fin = open("combo.in", "r")
    fout = open("combo.out", "w")
    N = int(fin.readline().strip())
    farmer = map(int, fin.readline().strip().split(" "))
    maker = map(int, fin.readline().strip().split(" "))
    if N <= 5:
        print >>fout, N * N * N
    else:
        same_num = []
        for i in range(3):
            a = farmer[i] + 1
            b = farmer[i] + 2
            if a > N:
                a %= N
            if b > N:
                b %= N
            c = farmer[i] - 1
            d = farmer[i] - 2
            if c <= 0:
                c += N
            if d <= 0:
                d += N
            p = maker[i] + 1
            q = maker[i] + 2
            if p > N:
                p %= N
            if q > N:
                q %= N
            x = maker[i] - 1
            y = maker[i] - 2
            if x <= 0:
                x += N
            if y <= 0:
                y += N
            valid_farmer = [a, b, c, d, farmer[i]]
            valid_maker = [p, q, x, y, maker[i]]
            same = 0
            for f in valid_farmer:
                if f in valid_maker:
                    same += 1
            same_num.append(same)
        print >>fout, 250 - same_num[0] * same_num[1] * same_num[2]
if __name__ == "__main__":
    solution()            
