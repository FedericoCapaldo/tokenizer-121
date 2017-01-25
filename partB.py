import partA

def findCommonWords(input1, input2): # runnint time O(n * n)
    commonWordsCounter = 0
    listOfCommonWords = list()
    input1 = partA.computeWordFrequencies(partA.tokeinze("data", input1))
    input2 = partA.computeWordFrequencies(partA.tokeinze("data", input2))

    for word in input1:
        if word in input2:
            listOfCommonWords.append(word)

    print(listOfCommonWords)
    print(len(listOfCommonWords))

# TEST (expected match 6)
# input1 = "We reviewed the trip and credited the cancellation fee. The driver has been notified"
# input2 = "If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply"
# findCommonWords(input1, input2)
