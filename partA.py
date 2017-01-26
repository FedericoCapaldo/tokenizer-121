import re
import operator

def openfile(my_path):
    content = ""
    with open(my_path) as infile:
        for line in infile:
            content += line
    return content

def tokeinze(type, file): # running time: O(k + n) k=number of lines in the file n = number of words
    print("--- tokenizing... ---")
    content = ""
    if type == "path":
        content = openfile(file)
    elif type == "data":
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


def computeWordFrequencies(list): # running time: O(n * n) n = length of list
    print("--- counting frequency ... ---")
    counted = dict()
    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted


def sortFrequencies(frequencyList):
    print("--- frequency sorting ... ---")
    return sorted(frequencyList.items(), key=operator.itemgetter(1))

def printFrequencies(frequencyList): # running time: O(n log n)
    sortedByFreq = sortFrequencies(frequencyList)
    listLength = len(sortedByFreq)
    for index in reversed(range(max(listLength-100,0), listLength)):
        print(sortedByFreq[index])

def printFrequenciesToFile(frequencyList):
    sortedByFreq = sortFrequencies(frequencyList)
    listLength = len(sortedByFreq)
    output = open("output.txt", "w")
    for index in reversed(range(0, listLength)):
        myTuple = sortedByFreq[index]
        output.write("(" + myTuple[0] + ", " + str(myTuple[1]) + ")\n")
    output.close()


# TEST (requires a file1.txt in utf-8 encoding in the same folder)
def testPartA(type, filename):
    printFrequenciesToFile(computeWordFrequencies(tokeinze(type, filename)))
    print("--- finished program ---")
# testPartA("path", "file4.txt")
