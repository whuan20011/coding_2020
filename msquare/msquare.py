"""
ID: whuan2001
LANG: PYTHON2
TASK: msquare
"""
def solution():
    fin = open("msquare.in", "r")
    fout = open("msquare.out", "w")
    arr = map(int, fin.readline().strip().split())
    init = [[1, 2, 3, 4,], [8, 7, 6, 5]]
    dst = [[arr[0], arr[1], arr[2], arr[3]], [arr[7], arr[6], arr[5], arr[4]]]
    visited = set()
    queue = [(init, "")]
    while queue:
        cur = queue.pop(0)
        x = tuple(cur[0][0])
        y = tuple(cur[0][1])
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if cur[0] == dst:
            res = cur[1]
            print >>fout, len(res)
            print >>fout, res
            return
        else:
            for char in "ABC":
                temp = transformation(cur[0], char)
                queue.append((temp, cur[1] + char))  
def transformation(brr, char):
    if char == "A":
        return [brr[1], brr[0]]
    if char == "B":
        return [[brr[0][3], brr[0][0], brr[0][1], brr[0][2]], [brr[1][3], brr[1][0], brr[1][1], brr[1][2]]]
    if char == "C":
        return [[brr[0][0], brr[1][1], brr[0][1], brr[0][3]], [brr[1][0], brr[1][2], brr[0][2], brr[1][3]]]
if __name__ == "__main__":
    solution()
       