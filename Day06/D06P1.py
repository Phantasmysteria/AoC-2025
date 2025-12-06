import sys
sys.path.append('..')
import aocutils
import numpy as np
import re

data = {}
data["00-raw"] = aocutils.listLines(day="06", part="1")
data["01-parsed"] = np.array([re.findall("[\\d+*]+", line) for line in data["00-raw"]]).T
data["02-answers"] = np.apply_along_axis(lambda x: np.prod(x[:-1].astype(int)) if x[-1] == '*' else np.sum(x[:-1].astype(int)), axis=1, arr=data["01-parsed"])

output = np.sum(data["02-answers"])
print(output)

aocutils.outputToTextFile(data)