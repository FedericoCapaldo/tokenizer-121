import re
import time

# start_time = time.time()

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


# print("---- %s seconds " % (time.time() - start_time))

def computeWordFrequencies(list):
    counted = dict()

    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1

    return counted



print(computeWordFrequencies(tokeinze("file1.txt")))
