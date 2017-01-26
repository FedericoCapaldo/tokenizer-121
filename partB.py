import partA

def findCommonWords(type, input1, input2): # runnint time O(n * n)
    commonWordsCounter = 0
    listOfCommonWords = list()
    input1 = partA.computeWordFrequencies(partA.tokeinze(type, input1))
    input2 = partA.computeWordFrequencies(partA.tokeinze(type, input2))

    for word in input1:
        if word in input2:
            listOfCommonWords.append(word)

    print(listOfCommonWords)
    print(len(listOfCommonWords))

# TEST
def testPartB(input1, input2):
    # (expected match 6)
    findCommonWords("data", input1, input2)
    # OR (expected match 30440)
    # findCommonWords("path", "file1.txt", "file1.txt")
input1 = "We reviewed the trip and credited the cancellation fee. The driver has been notified"
input2 = "If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply"
# testPartB(input1, input2)
