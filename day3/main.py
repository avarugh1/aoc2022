def readInput(f):
    with open(f) as fBuff:
        lines = fBuff.read()
    return lines


def charPrio(char):
    if(ord(char) > 96):
        prio = ord(char) - 96
    else:
        prio = ord(char) - 64 + 26

    return prio

def getPrio(l):
    seen = set()

    for i in range(len(l) // 2):
        seen.add(l[i])

    char = ''
    for i in range(len(l)//2 , len(l)):
        if l[i] in seen:
            char = l[i]
            break

    return charPrio(char)

def part2(txt):
    sumPrio = 0
    for i in range(0, len(txt), 3):
        commonChar = set(txt[i]).intersection(set(txt[i+1])).intersection(set(txt[i+2]))
        sumPrio += charPrio(list(commonChar)[0])

    return sumPrio

def main():
    txt = readInput('input2.txt').splitlines()
    sumPrio = 0
    for l in txt:
        sumPrio += getPrio(l)
    ## print(f'Part 1: {sumPrio}')

    print(f'Part 2: {part2(txt)}')

main()