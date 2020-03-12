"""
ID: whuan2001
LANG: PYTHON2
TASK: palsquare
"""
def solution():
    fin = open("palsquare.in", "r")
    fout = open("palsquare.out", "w")
    B = int(fin.readline().strip())
    for num in range(1, 301):
        square = num * num
        pal = transfer(square, B)
        if is_palindrome(pal):
            print >>fout, transfer(num, B), pal
def transfer(number, B):
    string = ""
    dic = {10: 'A', 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K"}
    while number:
        if number % B < 10:
            string += str(number % B)
        else:
            string += dic[number % B]
        number /= B
    return string[::-1]
def is_palindrome(s):
    lens = len(s)
    for i in range(lens / 2):
        if s[i] != s[lens - 1 - i]:
            return False
    return True
if __name__ == "__main__":
    solution()
           