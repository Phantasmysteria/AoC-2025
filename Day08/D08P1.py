import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="08", part="1")
dataLength = len(data["00-raw"])

# it's numpy time
data["01-parsed"] = np.array([line.split(',') for line in data["00-raw"]]).astype(int)

# (N, 3) => (N, N)
data["02-squared"] = np.sum(data["01-parsed"]**2, axis=1)
data["03-allPairsDist"] = np.triu(data["02-squared"] - 2*np.matmul(data["01-parsed"], data["01-parsed"].T) + data["02-squared"][:, np.newaxis]).flatten()

data["04-pairs"] = [(*divmod(x, dataLength), data["03-allPairsDist"][x]) for x in np.argsort(data["03-allPairsDist"]) if data["03-allPairsDist"][x] > 0]

data["05-boxes"] = aocutils.UnionFindSize(dataLength)

for i in range(1000):
    data["05-boxes"].union(data["04-pairs"][i][0], data["04-pairs"][i][1])

data["06-largestSizes"] = sorted(data["05-boxes"].sizes, reverse=True)[:3]

output = np.prod(data["06-largestSizes"])
print(output)

aocutils.outputToTextFile(data)