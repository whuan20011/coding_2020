"""
ID: whuan2001
LANG: PYTHON2
TASK: numtri
"""
def solution():
    fin = open("numtri.in", "r")
    fout = open("numtri.out", "w")
    N = int(fin.readline().strip())
    triangle = []
    for line in fin.readlines():
        triangle.append(map(int, line.strip().split(" ")))
    sums = []
    recursive(0, 0, triangle, triangle[0][0], sums)
    biggest = 0
    for s in sums:
        biggest = max(biggest, s)
    print >>fout, biggest
def recursive(row, col, triangle, pre_sum, sum):
    if row == len(triangle) - 1:
        sum.append(pre_sum)
        return
    else:
        recursive(row + 1, col, triangle, pre_sum + triangle[row + 1][col], sum)
        recursive(row + 1, col + 1, triangle, pre_sum + triangle[row + 1][col + 1], sum)
if __name__ == "__main__":
    solution()
        