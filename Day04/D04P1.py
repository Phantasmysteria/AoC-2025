import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="04", part="1")
dataLength = len(data["00-raw"])

data["01-grid"] = np.array([[1 if c == '@' else 0 for c in item] for item in data["00-raw"]])
gridY, gridX = np.shape(data["01-grid"])

data["02-resultGrid"] = np.zeros_like(data["01-grid"])

def visit(y, x, grid, resGrid):
    total = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (not (0 <= y+dy < gridY)) or (not (0 <= x+dx < gridX)) or (dx == 0 and dy == 0):
                continue
            total += grid[y+dy, x+dx]
    resGrid[y, x] = total < 4

for y, x in np.array(np.nonzero(data["01-grid"] == 1)).T:
    visit(y, x, data["01-grid"], data["02-resultGrid"])

output = np.sum(data["02-resultGrid"])
print(output)

aocutils.outputToTextFile(data)