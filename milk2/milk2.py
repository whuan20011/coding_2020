"""
ID: whuan2001
LANG: PYTHON2
TASK: milk2
"""
def solution():
    fin = open("milk2.in", "r")
    fout = open("milk2.out", "w")
    N = int(fin.readline().strip())
    times = []
    for _ in range(N):
        times.append(tuple(map(int, fin.readline().strip().split())))
    times = list(set(times))
    times = sorted(times)
    new_times = [list(times[0])]
    for time in times:
        if time[0] <= new_times[-1][1] and time[1] > new_times[-1][1]:
            new_times[-1][1] = time[1]
        elif time[0] <= new_times[-1][1] and time[1] <= new_times[-1][1]:
            continue
        else:
            new_times.append(list(time))
    longest_feeding = 0
    no_feeding = 0
    if len(new_times) == 1:
        print >>fout, new_times[0][1] - new_times[0][0], 0
    else:
        for t in new_times:
            longest_feeding = max(longest_feeding, t[1] - t[0])
        for i in range(1, len(new_times)):
            no_feeding = max(no_feeding, new_times[i][0] - new_times[i - 1][1])
        print >>fout, longest_feeding, no_feeding
if __name__ == "__main__":
    solution()
        