import sys
sys.path.append('..')
import aocutils

data = {}
data["00-raw"] = aocutils.listLines(day="02", part="2")
dataLength = len(data["00-raw"])

factors = ((), (), (1, ), (1, ), (1, 2), (1, ), (1, 2, 3), (1, ), (1, 2, 4), (1, 3), (1, 2, 5))

data["01-init"] = [pair.split('-') for pair in data["00-raw"][0].split(',')]
data["02-intLengthGroups1"] = [(int(small), int(large), len(small), len(large)) for small, large in data["01-init"]]
data["03-invalidIDs"] = []

for small, large, lenSmall, lenLarge in data["02-intLengthGroups1"]:
    ids = []
    for length in range(lenSmall, lenLarge + 1):
        for factor in factors[max(2, length)]:
            for substr in range(pow(10, factor - 1) - 1, pow(10, factor)):
                idNum = int(str(substr)*(length // factor))
                if (idNum > 10) and (small <= idNum <= large) and (idNum not in ids):
                    ids.append(idNum)

    data["03-invalidIDs"].append(ids)

data["04-intermediateSum"] = [sum(ids) for ids in data["03-invalidIDs"]]
output = sum(data["04-intermediateSum"])
print(output)

aocutils.outputToTextFile(data)