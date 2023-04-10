"""
Day 3 - Rucksack Reorganization
"""

"""PART 1"""
def rucksackReorganization(itemsList):
    total = 0

    for rucksack in itemsList:
        middle = len(rucksack) // 2 #the middle
        a = rucksack[:middle] #first part
        b = rucksack[middle:] #second part
        
        for item in set(a).intersection(b):
            if "a" <= item <= "z":
                total += ord(item) - ord("a") + 1
            if "A" <= item <= "Z":
                total += ord(item) - ord("A") + 27

    return total

#Test on Sample Input
SAMPLE_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
print(rucksackReorganization(SAMPLE_INPUT))

#Test on given input
inputFile = open("input.txt", "r")
# read the file
lines = inputFile.readlines()
print(rucksackReorganization(lines))