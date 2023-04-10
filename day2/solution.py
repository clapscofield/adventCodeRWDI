"""
--- Day 2: Rock Paper Scissors ---
"""

"""PART 1"""
def rockPaperScissorsGame(gameLines):
    total = 0
    for line in gameLines:
        x, y = line.split()

        x = ord(x) - 65
        y = ord(y) - ord("X")

        if x == y:
            total += 3
        elif (y - x) % 3 == 1:
            total += 6
        
        total += y + 1
    return total


"""PART 2 - Adapted Logic"""
def rockPaperScissorsGamePart2(gameLines):
    total = 0
    for line in gameLines:
        x, y = line.split()

        x = ord(x) - 65
        if y == "X":
            total += (x - 1) % 3 + 1
        elif y == "Y":
            total += 3 + x + 1
        else:
            total += 6 + (x + 1) % 3 + 1
    return total


SAMPLE_INPUT = [
    "A Y",
    "B X",
    "C Z"
]
#Test for the Sample Input
print(rockPaperScissorsGame(SAMPLE_INPUT))
print(rockPaperScissorsGamePart2(SAMPLE_INPUT))

#Test for the given Input
# open a file
inputFile = open("input.txt", "r")
# read the file
lines = inputFile.readlines()
print(rockPaperScissorsGame(lines))
print(rockPaperScissorsGamePart2(lines))