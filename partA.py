import re
import operator

def openfile(my_path):
    content = ""
    with open(my_path) as infile:
        for line in infile:
            content += line
    return content

def tokeinze(type, file):
    print("--- tokenizing... ---")
    content = ""
    if type == "path":
        content = openfile(file)
    elif type == "file":
        content = file
    content = content.lower()

    r = re.compile(r'(?P<na>[^ \na-zA-Z0-9]*)(?P<a>[ \na-zA-Z0-9]+)')
    s = len(content)
    counter = 0
    res = ""
    while counter < s:
        m = r.match(content, counter)
        if len(m.group("na")) is not 0:
            res += " "
        res += m.group("a")
        counter += len(m.group("a")) + len(m.group("na"))

    return res.split()


def computeWordFrequencies(list):
    print("--- counting frequency ... ---")
    counted = dict()

    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1

    return counted


def sortFrequencies(frequencyList):
    return sorted(frequencyList.items(), key=operator.itemgetter(1))

def printFrequencies(frequencyList):
    print("--- frequency ordering ... ---")
    sortedByFreq = sortFrequencies(frequencyList)
    listLength = len(sortedByFreq)
    for index in reversed(range(max(listLength-100,0), listLength)):
        print(sortedByFreq[index])

printFrequencies(computeWordFrequencies(tokeinze("path", "file1.txt")))
