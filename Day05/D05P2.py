import sys
sys.path.append('..')
import aocutils

data = {}
data["00-raw"] = aocutils.listLines(day="05", part="2")
dataLength = len(data["00-raw"])
splitIndex = data["00-raw"].index('')

data["01-ranges"] = data["00-raw"][:splitIndex]
data["02-ranges"] = [tuple(int(x) for x in item.split('-')) for item in data["01-ranges"]]

data["03-minSortedRanges"] = sorted(data["02-ranges"], key=lambda x: x[0])
data["04-mergedRanges"] = []

for currLower, currUpper in data["03-minSortedRanges"]:
    if not len(data["04-mergedRanges"]):
        data["04-mergedRanges"].append((currLower, currUpper))
        continue

    prevLower, prevUpper = data["04-mergedRanges"][-1]
    if currLower > prevUpper:
        data["04-mergedRanges"].append((currLower, currUpper))
    elif currUpper > prevUpper:
        data["04-mergedRanges"][-1] = (prevLower, currUpper)

output = sum([upper - lower + 1 for lower, upper in data["04-mergedRanges"]])
print(output)

aocutils.outputToTextFile(data)