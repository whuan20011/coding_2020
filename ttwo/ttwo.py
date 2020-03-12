"""
ID: whuan2001
LANG: PYTHON2
TASK: ttwo
"""
def solution():
    fin = open("ttwo.in", "r")
    fout = open("ttwo.out", "w")
    grid = []
    for line in fin.readlines():
        grid.append(list(line.strip()))
    dic = {}
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'F':
                farmer = ((i, j), 'N')
            if grid[i][j] == 'C':
                cows = ((i, j), 'N')
    dic[farmer] = set()
    dic[farmer].add(cows)
    time = 0
    while farmer[0] != cows[0]:
        farmer_next = find_next_step(grid, farmer)
        cows_next = find_next_step(grid, cows)
        if farmer_next in dic and cows_next in dic[farmer_next]:
            time = 0
            break
        else:
            if farmer_next not in dic:
                dic[farmer_next] = set()
                dic[farmer_next].add(cows_next)
            else:
                if cows_next not in dic[farmer_next]:
                    dic[farmer_next].add(cows_next)
        time += 1
        farmer = farmer_next
        cows = cows_next
    print >>fout, time
def find_next_step(grid, current):
    if current[1] == 'N':
        if current[0][0] - 1 >= 0 and grid[current[0][0] - 1][current[0][1]] != '*':
            current_next = ((current[0][0] - 1, current[0][1]), 'N')
        else:
            current_next = ((current[0][0], current[0][1]), 'E')
    if current[1] == 'E':
        if current[0][1] + 1 < 10 and grid[current[0][0]][current[0][1] + 1] != '*':
            current_next = ((current[0][0], current[0][1] + 1), 'E')
        else:
            current_next = ((current[0][0], current[0][1]), 'S')
    if current[1] == 'S':
        if current[0][0] + 1 < 10 and grid[current[0][0] + 1][current[0][1]] != '*':
            current_next = ((current[0][0] + 1, current[0][1]), 'S')
        else:
            current_next = ((current[0][0], current[0][1]), 'W')
    if current[1] == 'W':
        if current[0][1] - 1 >= 0 and grid[current[0][0]][current[0][1] - 1] != '*':
            current_next = ((current[0][0], current[0][1] - 1), 'W')
        else:
            current_next = ((current[0][0], current[0][1]), 'N')
    return current_next
if __name__ == "__main__":
    solution()
     