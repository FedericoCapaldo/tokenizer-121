import re
import operator


def tokeinze(my_path):
    print("--- tokenizing... ---")
    content = ""
    with open(my_path) as infile:
        for line in infile:
            content += line
    content = content.lower()

    r = re.compile(r'(?P<na>[^ \na-zA-Z0-9]*)(?P<a>[ \na-zA-Z0-9]+)')
    s = len(content)
    counter = 0
    res = ""
    while counter < s:
        m = r.match(content, counter)
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

def printFrequencies(frequencies):
    print("--- frequency ordering ... ---")
    sortedByFreq = sorted(frequencies.items(), key=operator.itemgetter(1))

    listLength = len(sortedByFreq)

    for index in reversed(range(listLength-100, listLength)):
        print(sortedByFreq[index])

printFrequencies(computeWordFrequencies(tokeinze("file6.txt")))
