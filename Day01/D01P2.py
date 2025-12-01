import sys
sys.path.append('..')
import aocutils
import numpy as np
import math

data = {}
data["raw"] = aocutils.listLines(day="01", part="2")
dataLength = len(data["raw"])

data["toNum"] = [int(item[1:]) * (-1 if item[0] == 'L' else 1) for item in data["raw"]]

data["spinCheckpoints"] = [50]
data["spinCount"] = []
for i in range(0, dataLength):
    spinDifference = data["spinCheckpoints"][i] + data["toNum"][i]
    spinDifference -= 100 if (spinDifference <= 0 and data["spinCheckpoints"][i] != 0) else 0
    data["spinCount"].append(math.floor(abs(spinDifference/100)))
    data["spinCheckpoints"].append((spinDifference + 100) % 100)

output = sum(data["spinCount"])
print(output)
