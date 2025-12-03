import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="03", part="2")
dataLength = len(data["00-raw"])

data["01-grid"] = np.array([[c for c in item] for item in data["00-raw"]])
gridY, gridX = np.shape(data["01-grid"])

data["02-currentLargest"] = [["".join(data["01-grid"][i][0:12]) for _ in range(12)] for i in range(gridY)]

for y in range(gridY):
    for x in range(12, gridX):
        stringCheck = data["02-currentLargest"][y][x-1] + data["01-grid"][y, x]
        # this is the first time i've unironically used for-else
        for pos in range(0, 12):
            if stringCheck[pos] < stringCheck[pos+1]:
                data["02-currentLargest"][y].append(stringCheck[0:pos] + stringCheck[pos+1:])
                break
        else:
            data["02-currentLargest"][y].append(data["02-currentLargest"][y][x-1])
            
data["03-largestJoltages"] = [int(item[-1]) for item in data["02-currentLargest"]]

output = sum(data["03-largestJoltages"])
print(output)

aocutils.outputToTextFile(data)