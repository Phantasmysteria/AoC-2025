import sys
sys.path.append('..')
import aocutils
import numpy as np
from PIL import Image

data = {}
data["00-raw"] = aocutils.listLines(day="09", part="2")

# it's numpy time
data["01-parsed"] = np.array([line.split(',') for line in data["00-raw"]]).astype(int)
dataLength = data["01-parsed"].shape[0]

data["unique"] = np.unique(data["01-parsed"])
data["intMap"] = {int(v): k[0] for k, v in np.ndenumerate(data["unique"])}
data["intReverseMap"] = {v: k for k, v in data["intMap"].items()}
data["02-compressed"] = np.array(list(map(lambda x: data["intMap"][x], data["01-parsed"].flatten()))).reshape(data["01-parsed"].shape)

# Visualization of coords
imgArray = np.zeros((500, 500))

for i in range(data["02-compressed"].shape[0] - 1):
    diff = data["02-compressed"][i+1] - data["02-compressed"][i]
    xNegative = -1 if diff[1] < 0 else 1
    yNegative = -1 if diff[0] < 0 else 1

    for j in range(abs(diff[1]) + 1):
        imgArray[data["02-compressed"][i][0], data["02-compressed"][i][1] + j * xNegative] = 127

    for k in range(abs(diff[0]) + 1):
        imgArray[data["02-compressed"][i][0] + k * yNegative, data["02-compressed"][i][1]] = 127

for item in data["02-compressed"]:
    imgArray[*item] = 255

img = Image.fromarray(imgArray.astype(np.uint8)).convert("L")
img.save('outputImg.png')

# Outliers at (433, 239) and (433, 244)
# Only check potential rectangles which have those outliers as a corner

data["03-compressedEliminated"] = data["02-compressed"][data["02-compressed"][:,0] < 433]

data["04a-leftSide"] = data["03-compressedEliminated"][data["03-compressedEliminated"][:,1] < 239]
data["04b-rightSide"] = data["03-compressedEliminated"][data["03-compressedEliminated"][:,1] > 244]

data["04a-leftSide"] = data["04a-leftSide"][data["04a-leftSide"][:,1] > 170]
data["04b-rightSide"] = data["04b-rightSide"][data["04b-rightSide"][:,1] < 310]

data["04c-leftSideUncompressed"] = np.array(list(map(lambda x: data["intReverseMap"][x], data["04a-leftSide"].flatten()))).reshape(data["04a-leftSide"].shape)
data["04d-rightSideUncompressed"] = np.array(list(map(lambda x: data["intReverseMap"][x], data["04b-rightSide"].flatten()))).reshape(data["04b-rightSide"].shape)

data["05a-leftSideAreas"] = np.prod(np.abs(data["04c-leftSideUncompressed"] - np.array([data["intReverseMap"][433], data["intReverseMap"][239]])) + 1, axis=1)
data["05b-rightSideAreas"] = np.prod(np.abs(data["04d-rightSideUncompressed"] - np.array([data["intReverseMap"][433], data["intReverseMap"][244]])) + 1, axis=1)

data["06-sideMax"] = []
for i in np.argsort(data["05a-leftSideAreas"])[::-1]:
    data["06-sideMax"].append((int(data["05a-leftSideAreas"][i]), data["04a-leftSide"][i][::-1], "left"))

for i in np.argsort(data["05b-rightSideAreas"])[::-1]:
    data["06-sideMax"].append((int(data["05b-rightSideAreas"][i]), data["04b-rightSide"][i][::-1], "right"))

data["06-sideMax"] = sorted(data["06-sideMax"], key=lambda x: x[0])

# By looking at the visualization and checking each point from highest to lowest, (308, 60) is in bounds
output = 1644094530
print(output)

aocutils.outputToTextFile(data)
