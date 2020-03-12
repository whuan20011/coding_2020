"""
ID: whuan2001
LANG: PYTHON2
TASK: beads
"""
def solution():
    fin = open("beads.in", "r")
    fout = open("beads.out", "w")
    N = int(fin.readline().strip())
    beads = fin.readline().strip()
    max_count = 0
    tag = 0
    for i in range(N):
        new_necklace = beads[i:] + beads[:i]
        left_count = count_beads(new_necklace)
        right_count = count_beads(new_necklace[::-1])
        if left_count + right_count < len(beads):
            max_count = max(max_count, left_count + right_count)
        else:
            tag = 1
            break
    if tag == 1:
        print >>fout, len(beads)
    else:
        print >>fout, max_count
def count_beads(necklace):
    count = 0
    for i in range(len(necklace)):
        if necklace[i] != 'w':
            first_color = necklace[i]
            for color in necklace[i:]:
                if color == first_color or color == 'w':
                    count += 1
                else:
                    break
            break
        else:
            count += 1
    return count
if __name__ == "__main__":
    solution()
                        