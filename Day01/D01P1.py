import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["raw"] = aocutils.listLines(day="01", part="1")
dataLength = len(data["raw"])

data["toNum"] = [int(item[1:]) * (-1 if item[0] == 'L' else 1) for item in data["raw"]]

data["spinCheckpoints"] = [50]
for i in range(0, dataLength):
    data["spinCheckpoints"].append((data["toNum"][i] + data["spinCheckpoints"][i] + 100) % 100)

output = np.count_nonzero(np.array(data["spinCheckpoints"]) == 0)
print(output)