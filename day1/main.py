def readInput(f):
    with open(f) as fBuff:
        lines = fBuff.read()
    return lines

def elvesCalories():
    lines = readInput('input2.txt')

    eles = lines.splitlines()

    accumulator = []
    currCount = 0
    for ele in eles:
        if(ele != ''):
            currCount += int(ele)
        else:
            accumulator.append(currCount)
            currCount = 0
        
    return accumulator

def sumOfElves(calorieCounts, numElves):
    if(len(calorieCounts) < numElves): ## just in case
        print('Not enough elves')

    return sum(sorted(calorieCounts, reverse=True)[:numElves])

def main():
    accumulator = elvesCalories()
    print(f'Part 1: {max(accumulator)}')
    print(f'Part 2: {sumOfElves(accumulator, 3)}')

main()