import sys
sys.path.append('..')
import aocutils
import numpy as np
import re
from collections import deque

data = {}
data["00-raw"] = aocutils.listLines(day="10", part="1")

data["01-processed"] = [item.split(" ") for item in data["00-raw"]]
data["02-processed"] = [([0 if i == '.' else 1 for i in item[0] if i == '.' or i == '#'], [list(map(int, re.findall("\\d", i))) for i in item[1:-1]], item[-1]) for item in data["01-processed"]]
data["03-processed"] = [(np.array(item[0]), np.array([[1 if k in j else 0 for k in range(len(item[0]))] for j in item[1]]), item[-1]) for item in data["02-processed"]]

# BFS brute force, because I tried linear programming but it doesn't work here...
data["04-fewestButtonPresses"] = []
for item in data["03-processed"]:

    queue = deque([(i, 1) for i in item[1]])

    while len(queue) > 0:
        currConfig, depth = queue.popleft()
        if np.array_equal(item[0], currConfig):
            data["04-fewestButtonPresses"].append(depth)
            break
        else:
            queue.extend(tuple([(currConfig + j) % 2, depth+1]) for j in item[1])
    
output = sum(data["04-fewestButtonPresses"])
print(output)

aocutils.outputToTextFile(data)