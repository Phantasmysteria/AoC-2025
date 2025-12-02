import sys
sys.path.append('..')
import aocutils

data = {}
data["00-raw"] = aocutils.listLines(day="02", part="1")
dataLength = len(data["00-raw"])

data["01-init"] = [pair.split('-') for pair in data["00-raw"][0].split(',')]
data["02-intLengthGroups1"] = [(small, large, *divmod(len(small), 2), *divmod(len(large), 2)) for small, large in data["01-init"]]
data["03-intLengthGroups2"] = [(int(small), int(large), int('1' + '0'*(divSmall) if modSmall else small[:divSmall]), int('1' + '0'*(divLarge) if modLarge else large[:divLarge])) for small, large, divSmall, modSmall, divLarge, modLarge in data["02-intLengthGroups1"]]
data["04-invalidIDs"] = []

for small, large, preSmall, preLarge in data["03-intLengthGroups2"]:
    ids = []
    for i in range(preSmall, preLarge + 1):
        idNum = int(str(i)*2)
        if (i == preSmall or i == preLarge) and not (small <= idNum <= large):
            continue
        ids.append(idNum)

    data["04-invalidIDs"].append(ids)

data["05-intermediateSum"] = [sum(ids) for ids in data["04-invalidIDs"]]
output = sum(data["05-intermediateSum"])
print(output)

aocutils.outputToTextFile(data)