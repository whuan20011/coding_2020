"""
ID: whuan2001
LANG: PYTHON2
TASK: sort3
"""
def solution():
    fin = open("sort3.in", "r")
    fout = open("sort3.out", "w")
    num = int(fin.readline().strip())
    numbers = []
    count1 = 0
    count2 = 0
    count3 = 0
    for line in fin.readlines():
        numbers.append(int(line.strip()))
        if int(line.strip()) == 1:
            count1 += 1
        if int(line.strip()) == 2:
            count2 += 1
        if int(line.strip()) == 3:
            count3 += 1
    exchange_times = 0
    temp = []
    for i in range(num - 1, num - 1 - count3, -1):
        if numbers[i] != 3:
            exchange_times += 1
            temp.append(numbers[i])
    temp = sorted(temp)
    for j in range(count1 + count2):
        if numbers[j] == 3:
            numbers[j] = temp.pop(0)
    for k in range(count1):
        if numbers[k] == 2:
            exchange_times += 1
    print >>fout, exchange_times
if __name__ == "__main__":
    solution()
        