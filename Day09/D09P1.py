import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="09", part="1")

# it's numpy time
data["01-parsed"] = np.array([line.split(',') for line in data["00-raw"]]).astype(int)
dataLength = data["01-parsed"].shape[0]

data["02-allPairsDiff"] = (data["01-parsed"] - np.expand_dims(data["01-parsed"] + 1, axis=1)).reshape((dataLength**2, 2))
data["03-allPairsArea"] = np.abs(np.prod(data["02-allPairsDiff"], axis=1))

output = np.max(data["03-allPairsArea"])
print(output)

aocutils.outputToTextFile(data)