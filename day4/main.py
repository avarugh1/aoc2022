def readInput(f):
    with open(f) as fBuff:
        lines = fBuff.read()
    return lines

def anyOverlap(range1, range2):
    range1 = [ int(x) for x in range1.split('-') ]
    range2 = [ int(x) for x in range2.split('-') ]

    if range1[0] >= range2[0] and range1[0] <= range2[1]:
        return True
    if range1[1] <= range2[1] and range1[1] >= range2[0]:
        return True

    if range2[0] >= range1[0] and range2[0] <= range1[1]:
        return True
    if range2[1] <= range1[1] and range2[1] >= range1[0]:
        return True

    return False

def encomposses(range1, range2):
    range1 = [ int(x) for x in range1.split('-') ]
    range2 = [ int(x) for x in range2.split('-') ]

    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True

    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True

    return False
    
def main():
    txt = readInput('input2.txt').splitlines()

    ctr = 0
    ctrPart2 = 0
    for l in txt:
        elf1, elf2 = l.split(',')
        if(encomposses(elf1, elf2)):
            ctr += 1
        if anyOverlap(elf1, elf2):
            ctrPart2 += 1

    print(f'Part 1: {ctr}')
    print(f'Part 2: {ctrPart2}')

main()