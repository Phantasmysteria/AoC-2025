import sys
sys.path.append('..')
import aocutils
import re
from functools import lru_cache

data = {}
data["00-raw"] = aocutils.listLines(day="11", part="2")
data["01-parsed"] = [[re.findall("\\w+", item) for item in line.split(": ")] for line in data["00-raw"]]
data["02-adjList"] = {line[0][0]: tuple(line[1]) for line in data["01-parsed"]}
data["02-adjList"]["out"] = tuple()

@lru_cache
def findAllPaths(src, dest):
    return sum([findAllPaths(neighbour, dest) for neighbour in data["02-adjList"][src]]) if src != dest else 1

output = findAllPaths("svr", "fft") * findAllPaths("fft", "dac") * findAllPaths("dac", "out") + findAllPaths("svr", "dac") * findAllPaths("dac", "fft") * findAllPaths("fft", "out")
print(output)

aocutils.outputToTextFile(data)