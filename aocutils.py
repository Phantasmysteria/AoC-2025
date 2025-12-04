from typing import List, Any
import itertools
import pprint

# Quick way to convert input file into list of lines
def listLines(day: str, part: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [item.rstrip() for item in f.readlines()]

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



if __name__ == '__main__':
    print("Why are you running this file?")