import sys
sys.path.append('..')
import aocutils
import numpy as np
import re

data = {}
data["00-raw"] = aocutils.listLines(day="12", part="1")

data["01a-presentShapes"] = [0, 0, 0, 0, 0, 0]
currPresent = 0
for i in range(29):
    if data["00-raw"][i] == '':
        currPresent += 1
    data["01a-presentShapes"][currPresent] += len(re.findall('#', data["00-raw"][i]))

data["01a-presentShapes"] = np.array(data["01a-presentShapes"])
data["01b-formations"] = np.array([list(map(int, re.findall("\\d+", item))) for item in data["00-raw"][30:]])

data["02a-formationAreas"] = np.sum(data["01b-formations"][:,2:] * data["01a-presentShapes"], axis=1)
data["02b-formationRegions"] = np.prod(data["01b-formations"][:,0:2], axis=1)

# I love how the straightforward approach, i.e. my first instinct, actually works here...
data["03-fits"] = data["02a-formationAreas"][data["02a-formationAreas"] < data["02b-formationRegions"]]

output = len(data["03-fits"])
print(output)

aocutils.outputToTextFile(data)