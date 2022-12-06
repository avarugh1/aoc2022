import copy

def readInput(f):
    with open(f) as fBuff:
        lines = fBuff.read()
    return lines

def cutArray(instructions, stacks):
    for instruction in instructions:
        count = instruction[0]
        startingStack = instruction[1] - 1
        destinationStack = instruction[2] - 1
    
        
        stacks[destinationStack].extend(stacks[startingStack][-count:])
        stacks[startingStack] = stacks[startingStack][:-count]

    return ''.join(l[-1] for l in stacks)

def moveAround(instructions, stacks):
    for instruction in instructions:
        count = instruction[0]
        startingStack = instruction[1] - 1
        destinationStack = instruction[2] - 1

        for i in range(count):
            removedEle = stacks[startingStack].pop()
            stacks[destinationStack].append(removedEle)

        
    # for l in stacks:
    #     print(*l)

    return stacks


## do I really want to write a parser for this
def startingPoint():
    ll = [
        ['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'],
        ['W', 'P', 'Q', 'G', 'S'],
        ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
        ['F', 'Z', 'P', 'C', 'G', 'D', 'L'],
        ['T', 'P', 'S'],
        ['H', 'D', 'F', 'W', 'R', 'L'],
        ['Z', 'N', 'D', 'C'],
        ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'],
        ['R', 'M', 'S', 'G', 'Z', 'W', 'V']
    ]

    return ll

    
def main():
    txt = readInput('input.txt').splitlines()
    start = startingPoint()
    instructions = []
    for l in txt:
        tmp = [int(s) for s in l.split() if s.isdigit()]
        instructions.append(tmp)

    part1Start = copy.deepcopy(start)
    ans = moveAround(instructions, part1Start)
    print(f'Part 1: {ans}')

    ans = cutArray(instructions, start)
    print(f'Part 2: {ans}')
 
main()