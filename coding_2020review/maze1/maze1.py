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
    for _ in range(2 * H + 1):
        maze.append(list(fin.readline().strip("/n")))
    exits = []
    for i in range(2 * H + 1):
        if maze[i][0] == " ":
            exits.append((i, 0))
        if maze[i][2 * W] == " ":
            exits.append((i, 2 * W))
    for j in range(2 * W + 1):
        if maze[0][j] == " ":
            exits.append((0, j))
        if maze[2 * H][j] == " ":
            exits.append((2 * H, j))
    dis = {}
    for exit in exits:
        visited = set()
        queue = []
        if exit[0] == 0:
            queue.append([(1, exit[1]), 1])
            dis[(1, exit[1])] = 1
        if exit[0] == 2 * H:
            queue.append([(exit[0] - 1, exit[1]), 1])
            dis[(exit[0] - 1, exit[1])] = 1
        if exit[1] == 0:
            queue.append([(exit[0], 1), 1])
            dis[(exit[0], 1)] = 1
        if exit[1] == 2 * W:
            queue.append([(exit[0], exit[1] - 1), 1])
            dis[(exit[0], exit[1] - 1)] = 1
        while queue:
            cur = queue.pop(0)
            if cur[0] in visited:
                continue
            visited.add(cur[0])
            neighboors = find_all_neighboors(maze, H, W, cur)
            for neighboor in neighboors:
                queue.append([neighboor, cur[1] + 1])
                if neighboor not in dis:
                    dis[neighboor] = cur[1] + 1
                else:
                    dis[neighboor] = min(dis[neighboor], cur[1] + 1)
    longest = 0
    for d in dis:
        longest = max(longest, dis[d])
    print >>fout, longest
def find_all_neighboors(maze, H, W, cur):
    neighboors = []
    x = cur[0][0]
    y = cur[0][1]
    if x >= 2 and maze[x - 1][y] == " ":
        neighboors.append((x - 2, y))
    if x <= 2 * H - 2 and maze[x + 1][y] == " ":
        neighboors.append((x + 2, y))
    if y >= 2 and maze[x][y - 1] == " ":
        neighboors.append((x, y - 2))
    if y <= 2 * W - 2 and maze[x][y + 1] == " ":
        neighboors.append((x, y + 2))
    return neighboors
if __name__ == "__main__":
    solution()
            