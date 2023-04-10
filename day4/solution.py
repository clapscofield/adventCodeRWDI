"""
Day 4 - Camp Cleanup
"""

"""Part 1"""
def campCleanup(sections):
    count = 0

    for line in sections:
        start1, end1, start2, end2 = map(int, line.replace(",", "-").split("-"))
        if start1 <= start2 and end1 >= end2 or start1 >= start2 and end1 <= end2:
            count += 1
    return count


#Test on sample input
SAMPLE_INPUT = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
print(campCleanup(SAMPLE_INPUT))


#Test on given input
inputFile = open("input.txt", "r")
# read the file
lines = inputFile.readlines()
print(campCleanup(lines))