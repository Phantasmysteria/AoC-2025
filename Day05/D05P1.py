import sys
sys.path.append('..')
import aocutils

data = {}
data["00-raw"] = aocutils.listLines(day="05", part="1")
dataLength = len(data["00-raw"])
splitIndex = data["00-raw"].index('')

data["01a-ranges"], data["01b-ingredients"] = data["00-raw"][:splitIndex], data["00-raw"][splitIndex+1:]
data["02a-ranges"], data["02b-ingredients"] = [tuple(int(x) for x in item.split('-')) for item in data["01a-ranges"]], [int(x) for x in data["01b-ingredients"]]

def freshnessCheck(ingrId):
    for lower, upper in data["02a-ranges"]:
        if lower <= ingrId <= upper:
            return True
    return False

data["03-freshIngredients"] = list(filter(freshnessCheck, data["02b-ingredients"]))

output = len(data["03-freshIngredients"])
print(output)

aocutils.outputToTextFile(data)