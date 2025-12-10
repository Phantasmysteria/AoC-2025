import sys
sys.path.append('..')
import aocutils
import numpy as np
import re
from scipy.optimize import linprog

data = {}
data["00-raw"] = aocutils.listLines(day="10", part="2")

data["01-processed"] = [item.split(" ") for item in data["00-raw"]]
data["02-processed"] = [([0 if i == '.' else 1 for i in item[0] if i == '.' or i == '#'], [list(map(int, re.findall("\\d", i))) for i in item[1:-1]], list(map(int, re.findall("\\d+", item[-1])))) for item in data["01-processed"]]
data["03-processed"] = [([1 for _ in range(len(item[1]))], np.array([[1 if k in j else 0 for k in range(len(item[0]))] for j in item[1]]).T, item[-1]) for item in data["02-processed"]]

# Linear programming my beloved
# I tried to do this in part 1, thankfully I didn't delete my code...
data["04-fewestButtonPresses"] = [linprog(item[0], A_eq=item[1], b_eq=item[2], integrality=1).fun for item in data["03-processed"]]

output = int(sum(data["04-fewestButtonPresses"]))
print(output)

aocutils.outputToTextFile(data)