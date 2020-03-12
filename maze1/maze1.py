"""
ID: whuan2001
LANG: PYTHON2
TASK: maze1
"""
def solution():
    fin = open("maze1.in", "r")
    fout = open("maze1.out", "w")
    W, H = map(int, fin.readline().strip().split())
    maze = []
    for line in fin.readlines():
        maze.append(list(line.strip("/n")))
    exits = []
    for col in range(2 * W + 1):
        if maze[0][col] == " ":
            exits.append((0, col))
        if maze[2 * H][col] == " ":
            exits.append((2 * H, col))
    for row in range(2 * H + 1):
        if maze[row][0] == " ":
            exits.append((row, 0))
        if maze[row][2 * W] == " ":
            exits.append((row, 2 * W))
    dis = {}
    for exit in exits:
        queue = []
        visited = set()
        if exit[0] == 0:
            queue.append([(1, exit[1]), 1])
            dis[(1, exit[1])] = 1
        elif exit[0] == 2 * H:
            queue.append([(2 * H - 1, exit[1]), 1])
            dis[(2 * H - 1, exit[1])] = 1
        elif exit[1] == 0:
            queue.append([(exit[0], 1), 1])
            dis[(exit[0], 1)] = 1
        elif exit[1] == 2 * W:
            queue.append([(exit[0], 2 * W - 1), 1])
            dis[(exit[0], 2 * W -1)] = 1
        while queue:
            cur = queue.pop(0)
            if cur[0] in visited:
                continue
            visited.add(cur[0])
            for neighboor in find_neighboors(maze, W, H, cur):
                queue.append([neighboor, cur[1] + 1])
                if neighboor not in dis:
                    dis[neighboor] = cur[1] + 1
                else:
                    dis[neighboor] = min(dis[neighboor], cur[1] + 1)
    res = 0
    for d in dis:
        res = max(res, dis[d])
    print >>fout, res   
def find_neighboors(maze, W, H, cur):
    x = cur[0][0]
    y = cur[0][1]
    neighboors = []
    if x - 1 >= 1 and maze[x - 1][y] == " ":
        neighboors.append((x - 2, y))
    if x + 1 <= 2 * H - 1 and maze[x + 1][y] == " ":
        neighboors.append((x + 2, y))
    if y - 1 >= 1 and maze[x][y - 1] == " ":
        neighboors.append((x, y - 2))
    if y + 1 <= 2 * W - 1 and maze[x][y + 1] == " ":
        neighboors.append((x, y + 2))
    return neighboors
if __name__ == "__main__":
    solution()
        