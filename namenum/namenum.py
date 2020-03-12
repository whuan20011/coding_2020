"""
ID: whuan2001
LANG: PYTHON2
TASK: namenum
"""
def solution():
    fin = open("namenum.in", "r")
    fout = open("namenum.out", "w")
    finc = open("dict.txt", "r")
    cows = finc.readlines()
    cow_names = set()
    for cow in cows:
        cow_names.add(cow.strip())    
    numbers = []
    for num in fin.readline().strip():
        numbers.append(num)
    key = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'],
    '7': ['P', 'R','S'],'8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y']}
    generate_names = []
    dfs(numbers, key, "", generate_names)
    res = []
    for name in generate_names:
        if name in cow_names:
            res.append(name)
    if not res:
        print >>fout, 'NONE'
    for r in res:
        print >>fout, r 
def dfs(numbers, key, pre, arr):
    if len(pre) == len(numbers):
        arr.append(pre)
        return
    for k in key[numbers[len(pre)]]:
        dfs(numbers, key, pre + k, arr)
if __name__ == "__main__":
    solution()  
       