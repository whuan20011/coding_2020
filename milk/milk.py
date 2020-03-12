"""
ID: whuan2001
LANG: PYTHON2
TASK: milk
"""
def solution():
    fin = open("milk.in", "r")
    fout = open("milk.out", "w")
    N, M = map(int, fin.readline().strip().split(" "))
    price_production = []
    for _ in range(M):
        price_production.append(map(int, fin.readline().strip().split(" ")))
    price_production = sorted(price_production)
    cost = 0
    for p in price_production:
        if p[1] <= N:
            cost += p[0] * p[1]
            N -= p[1]
        else:
            cost += p[0] * N
            break
    print >>fout, cost
if __name__ == "__main__":
    solution()
    