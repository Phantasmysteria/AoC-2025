from typing import List, Any
import itertools
import pprint

# Quick way to convert input file into list of lines
def listLines(day: str, part: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [item.rstrip() for item in f.readlines()]

# Quick way to convert input file into list of lines (without removing end spaces)
def listLinesWithSpaces(day: str, part: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [item[:-1] if item[-1] == '\n' else item for item in f.readlines()]

# Quick way to convert input file into list of list of lines separated by delimiter
def listLinesWithGroup(day: str, part: str, groupSep: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [list(group) for key, group in itertools.groupby([item.rstrip() for item in f.readlines()], lambda x: x == groupSep) if not key]

# Output pretty print to output.txt
def outputToTextFile(data: Any) -> None:
    with open("output.txt", "w") as f:
        f.write(pprint.pformat(data))

# Get slice of dict from [start, end]
def sliceView(data: dict, start: int, end: int) -> dict:
    ret = {}
    for k, v in data.items:
        try:
            ret[k] = v[start:end+1]
        except (TypeError, IndexError):
            ret[k] = v
    return ret

# Yes I know Counter class exists
def addToCounter(data: dict[Any, int], key: Any, val: int) -> None:
    if key not in data:
        data[key] = 0
    data[key] += val

# I have never implemented union-find until now
class UnionFindSize:
    def __init__(self, length):
        self.parents = list(range(length))
        self.sizes = [1 for _ in range(length)]

    def find(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        return self.find(self.parents[x])

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        if self.sizes[xRoot] < self.sizes[yRoot]:
            xRoot, yRoot = yRoot, xRoot

        self.parents[yRoot] = xRoot
        self.sizes[xRoot] += self.sizes[yRoot]

    def __repr__(self):
        return str([(x, y) for x, y in zip(self.parents, self.sizes)])

if __name__ == '__main__':
    print("Why are you running this file?")