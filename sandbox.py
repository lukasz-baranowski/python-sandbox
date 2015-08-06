__author__ = 'lucek'

import json

JSON_FILEPATH = "/home/lucek/workspace_py/sample.json"


def main():
    print("Hello, World!")

    # testJsonRead()
    # testLambda()
    # testFor()
    testDict()

def testDict():
    dict = {1: "a", 2: "b", 3: "c"}
    print(dict)
    print(dict.items())

    for o in dict.items():
        print(o[1])




def testFor():
    colletion = range(1, 6)
    print [str(x) for x in colletion]

    col = []
    for x in colletion:
        col.append(str(x))
    print col

    print map(lambda x: str(x), colletion)

    print [str(x) for x in colletion if (x != 3)]

    colletion = range(1, 6)
    colletion.append("LOL")
    print(colletion)
    print [(x * "lucek ")[:-1] for x in colletion if isinstance(x, int)]


def testLambda():
    collection = [1, 2, 3, 4, 5]
    print(collection)
    f = lambda x: x + 1
    mapped = map(f, collection)
    print(mapped)
    mapped2 = map(lambda x: (x * "lucek ")[:-1], collection)
    print(mapped2)

    print("Moving far far on...")
    collection.append("LOL")
    print(collection)
    print(map(lambda x: ((int(x) if isinstance(x, int) else len(str(x))) * "lucek ")[:-1], collection))

    jsonData = readJson()


def testJsonRead():
    jsonData = readJson()
    print(jsonData)
    baselines = jsonData['baselines'].items()
    for b in baselines:
        print(str(b[0]) + ", " + str(b[1]))
    print("Moving on...")
    for b in baselines:
        baselineName = b[0]
        print(baselineName + ": " + b[1]['continentName'] + ", " + b[1]['version'])


def readJson():
    with open(JSON_FILEPATH) as json_file:
        json_data = json.loads(json_file.read())
    return json_data


if __name__ == '__main__':
    main()