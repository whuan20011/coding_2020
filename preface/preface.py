"""
ID: whuan2001
LANG: PYTHON2
TASK: preface
"""
import math
def solution():
    fin = open("preface.in", "r")
    fout = open("preface.out", "w")
    N = int(fin.readline().strip())
    dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    res = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0, 'D':0, 'M':0}
    for num in range(1, N + 1):
        arr = roman(dic, num)
        #print arr
        for a in arr:
            res[a] += 1
    if res['I'] != 0:
        print >>fout, 'I', res['I']
    if res['V'] != 0:
        print >>fout, 'V', res['V']
    if res['X'] != 0:
        print >>fout, 'X', res['X']
    if res['L'] != 0:
        print >>fout, 'L', res['L']
    if res['C'] != 0:
        print >>fout, 'C', res['C']
    if res['D'] != 0:
        print >>fout, 'D', res['D']
    if res['M'] != 0:
        print >>fout, 'M', res['M']
def roman(dic, num):
    brr = []
    while num:
        brr.append(num % 10)
        num /= 10
    crr = []
    for i in range(len(brr)):
        if brr[i] == 0:
            continue
        p = int(math.pow(10, i))
        if brr[i] == 1:
            crr.append(dic[p])
        if brr[i] == 2:
            crr.append(dic[p])
            crr.append(dic[p])
        if brr[i] == 3:
            crr.append(dic[p])
            crr.append(dic[p])
            crr.append(dic[p])
        if brr[i] == 4:
            crr.append(dic[p])
            crr.append(dic[p * 5])
        if brr[i] == 5:
            crr.append(dic[p * 5])
        if brr[i] == 6:
            crr.append(dic[p * 5])
            crr.append(dic[p])
        if brr[i] == 7:
            crr.append(dic[p * 5])
            crr.append(dic[p])
            crr.append(dic[p])
        if brr[i] == 8:
            crr.append(dic[p * 5])
            crr.append(dic[p])
            crr.append(dic[p])
            crr.append(dic[p])
        if brr[i] == 9:
            crr.append(dic[p])
            crr.append(dic[p * 10])
    return crr
if __name__ == "__main__":
    solution()
        