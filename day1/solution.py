"""
Day 1: Counting Calories
"""

SAMPLE_INPUT = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]

"""PART 1"""
def countingCalories(elvesCalories):
    sumsCalories = []
    current = 0
    for cal in elvesCalories:
        cal = cal.strip()
        if cal:
            current += int(cal)
        else:
            sumsCalories.append(current)
            current = 0
    sumsCalories.append(current)
    return sumsCalories

def maxCounting(sumsCalories):
    return max(sumsCalories)

"""PART 2"""
def maxTopThree(sumsCalories):
    return sum(sorted(sumsCalories)[-3:])

#Test for the Sample Input
sumsCalories = countingCalories(SAMPLE_INPUT)
print(maxCounting(sumsCalories))
#part 2
print(maxTopThree(sumsCalories))


#Test for the given Input
# open a file
inputFile = open("input.txt", "r")
# read the file
lines = inputFile.readlines()
sumsCalories = countingCalories(lines)
print(maxCounting(sumsCalories))

#part 2
print(maxTopThree(sumsCalories))
