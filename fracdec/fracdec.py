"""
ID: whuan2001
LANG: PYTHON2
TASK: fracdec
"""
def solution():
    fin = open("fracdec.in", "r")
    fout = open("fracdec.out", "w")
    N, D = map(int, fin.readline().strip().split())
    if N % D == 0:
        print >>fout, str(N / D) + ".0"
    else:
        tag = 0
        arr = []
        extras = set()
        while N:
            arr.append(N / D)
            N %= D
            if N not in extras:
                extras.add(N)
                N *= 10
            else:
                tag = 1
                first = N * 10 / D
                for i in range(1, len(arr)):
                    if arr[i] == first:
                        for j in range(len(arr)):
                            arr[j] = str(arr[j])
                        res = arr[0] + "." + "".join(arr[1:i]) + "(" + "".join(arr[i:]) + ")"
                        if len(res) < 76:
                            print >>fout, res
                        elif len(res) % 76 == 0:
                            for p in range(len(res) / 76):
                                print >>fout, res[(p * 76):(p * 76 + 76)]
                        elif len(res) > 76 and len(res) % 76 != 0:
                            for p in range(len(res) / 76):
                                print >>fout, res[(p * 76):(p * 76 + 76)]
                            print >>fout, res[(len(res) / 76) * 76:]
                        break
                break
        if tag == 0:
            for k in range(len(arr)):
                arr[k] = str(arr[k])
            res = arr[0] + "." + "".join(arr[1:])
            if len(res) < 76:
                print >>fout, res
            elif len(res) % 76 == 0:
                for p in range(len(res) / 76):
                    print >>fout, res[(p * 76):(p * 76 + 76)]
            elif len(res) > 76 and len(res) % 76 != 0:
                for p in range(len(res) / 76):
                    print >>fout, res[(p * 76):(p * 76 + 76)]
                print >>fout, res[(len(res) / 76) * 76:]
if __name__ == "__main__":
    solution()
        