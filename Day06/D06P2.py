import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLinesWithSpaces(day="06", part="2")
data["01-transpose"] = np.apply_along_axis(lambda x: "".join(x), axis=1, arr=np.array([[c for c in item] for item in data["00-raw"]]).T)
data["02-restored"] = []

storage = []
for item in data["01-transpose"]:
    if item[-1] in "+*":
        storage.append(item[-1])
    
    if item.isspace():
        data["02-restored"].append(storage)
        storage = []
    else:
        storage.append(int(item[:-1]))
data["02-restored"].append(storage)
data["03-answers"] = list(map(lambda x: np.prod(x[1:]) if x[0] == '*' else np.sum(x[1:]), data["02-restored"]))

output = np.sum(data["03-answers"])
print(output)

aocutils.outputToTextFile(data)