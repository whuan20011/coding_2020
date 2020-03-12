"""
ID: whuan2001
LANG: PYTHON2
TASK: friday
"""
def solution():
    fin = open("friday.in", "r")
    fout = open("friday.out", "w")
    N = int(fin.readline().strip())
    month = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    week = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(N):
        year = 1900 + i
        for m in range(12):
            if m == 0 and year == 1900:
                tag = 6
                week[6] += 1  
            elif m == 2:
                if is_leap_year(year):
                    if tag == 7:
                        tag = 1
                        week[tag] += 1
                    else:
                        tag += 1
                        week[tag] += 1
                else:
                    week[tag] += 1
            else:
                if month[m] % 7 + tag <= 7:
                    tag = month[m] % 7 + tag
                    week[tag] += 1
                else:
                    tag = (month[m] % 7 + tag) % 7
                    week[tag] += 1
    print >>fout, week[6], week[7], week[1], week[2], week[3], week[4], week[5]
def is_leap_year(year):
    if year % 100 != 0 and year % 4 == 0:
        return True
    if year % 100 ==0 and year % 400 == 0:
        return True
    return False
if __name__ == "__main__":
    solution()
