import partA

def find_common_words(type, input1, input2): # runnint time O(n * n)
    list_of_common_words = list()
    input1 = partA.compute_word_frequencies(partA.tokeinze(type, input1))
    input2 = partA.compute_word_frequencies(partA.tokeinze(type, input2))

    for word in input1:
        if word in input2:
            list_of_common_words.append(word)

    print(list_of_common_words)
    print(len(list_of_common_words))

# TEST
def test_part_B(input1, input2):
    # (expected match 6)
    find_common_words("data", input1, input2)
    # OR (expected match 30440)
    # findCommonWords("path", "file1.txt", "file1.txt")
input1 = "We reviewed the trip and credited the cancellation fee. The driver has been notified"
input2 = "If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply"
# test_part_B(input1, input2)
