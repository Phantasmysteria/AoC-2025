import sys
sys.path.append('..')
import aocutils
import numpy as np
import re

data = {}
data["00-raw"] = aocutils.listLines(day="07", part="2")
data["01-parsed"] = [list(m.start() for m in re.finditer("[S^]", line)) for line in data["00-raw"] if re.findall("[S^]", line)]
data["02a-rays"], data["02b-splitters"] = [{data["01-parsed"][0][0]: 1}], data["01-parsed"][1:]

for iter in range(len(data["02b-splitters"])):
    nextRays = {}
    for ray in data["02a-rays"][iter].keys():
        if ray in data["02b-splitters"][iter]:
            aocutils.addToCounter(nextRays, ray+1, data["02a-rays"][iter][ray])
            aocutils.addToCounter(nextRays, ray-1, data["02a-rays"][iter][ray])
        else:
            aocutils.addToCounter(nextRays, ray, data["02a-rays"][iter][ray])
    data["02a-rays"].append(nextRays)

output = sum(data["02a-rays"][-1].values())
print(output)

aocutils.outputToTextFile(data)