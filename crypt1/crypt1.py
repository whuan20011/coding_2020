"""
ID: whuan2001
LANG: PYTHON2
TASK: crypt1
"""
def solution():
    fin = open("crypt1.in", "r")
    fout = open("crypt1.out", "w")
    N = int(fin.readline().strip())
    digits = []
    for d in fin.readline().strip().split(" "):
        digits.append(d)
    arr = []
    dfs(digits, "", arr)
    res = 0
    for a in arr:
        first_num = int(a[0]) * 100 + int(a[1]) * 10 + int(a[2])
        first_production = first_num * int(a[4])
        second_production = first_num * int(a[3])
        if first_production / 1000 == 0 and is_in_digits(first_production, a, digits):
            if second_production / 1000 == 0 and is_in_digits(second_production, a, digits):
                if is_in_digits(second_production * 10 + first_production, a, digits):
                    res += 1
    print >>fout, res
def is_in_digits(production, a, digits):
    numbers = []
    while production:
        numbers.append(production % 10)
        production /= 10
    for num in numbers:
        if str(num) not in digits:
            return False
    return True
def dfs(digits, pre, arr):
    if len(pre) == 5:
        arr.append(pre)
        return
    for d in digits:
        dfs(digits, pre + d, arr)
if __name__ == "__main__":
    solution()
    