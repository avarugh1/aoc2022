def readInput(f):
    with open(f) as fBuff:
        lines = fBuff.read()
    return lines

## for part 2
## restructures input to allow us to reuse code from part 1
def prepareInput(txt):
    lossDrawWinMap = {
        'A': ['Z', 'X', 'Y'],
        'B': ['X', 'Y', 'Z'],
        'C': ['Y', 'Z', 'X']
    }

    newOutput = []
    for line in txt:
        playerA, result = line.split(' ')
        playerB = lossDrawWinMap[playerA][ord(result) - 88]
        newOutput.append(f'{playerA} {playerB}')

    return newOutput

def getScore(txt):
    winnerMap = { 'A': ['B', 1], 'B': ['C', 2], 'C': ['A', 3] }

    runningScore = 0
    for line in txt:
        playerA, playerB = line.split(' ')
        normalizedPlayerB = chr(ord(playerB) - 23)
        if(playerA == normalizedPlayerB): ## draw
            runningScore += 3
        elif(normalizedPlayerB == winnerMap[playerA][0]): ## win
            runningScore += 6

        runningScore += winnerMap[normalizedPlayerB][1] ## always add hand score

    return runningScore

def main():
    txt = readInput('input2.txt').splitlines()
    runningScore = getScore(txt)
    print(f'Part 1: {runningScore}')
    newInput = prepareInput(txt)
    print(f'Part 2: {getScore(newInput)}')

main()