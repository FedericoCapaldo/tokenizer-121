import re
import operator

def open_file(my_path):
    content = ""
    with open(my_path) as infile:
        for line in infile:
            content += line
    return content

def tokeinze(type, file): # running time: O(k + n) k=number of lines in the file n = number of words
    print("--- tokenizing... ---")
    content = ""
    if type == "path":
        content = open_file(file)
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


def compute_word_frequencies(list): # running time: O(n * n) n = length of list
    print("--- counting frequency ... ---")
    counted = dict()
    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted


def sort_frequencies(frequencyList):
    print("--- frequency sorting ... ---")
    return sorted(frequencyList.items(), key=operator.itemgetter(1))

def print_frequencies(frequencyList): # running time: O(n log n)
    sorted_by_freq = sort_frequencies(frequencyList)
    list_length = len(sorted_by_freq)
    for index in reversed(range(max(list_length-100,0), list_length)):
        print(sorted_by_freq[index])

def print_frequencies_to_file(frequencyList):
    sorted_by_freq = sort_frequencies(frequencyList)
    list_length = len(sorted_by_freq)
    output = open("output.txt", "w")
    for index in reversed(range(0, list_length)):
        my_tuple = sorted_by_freq[index]
        output.write("(" + my_tuple[0] + ", " + str(my_tuple[1]) + ")\n")
    output.close()


# TEST (requires a file1.txt in utf-8 encoding in the same folder)
def test_part_A(type, filename):
    print_frequencies_to_file(compute_word_frequencies(tokeinze(type, filename)))
    print("--- finished program ---")
# test_part_A("path", "file3.txt")
