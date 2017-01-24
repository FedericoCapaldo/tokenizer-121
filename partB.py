import partA

lista = { 'one': 2, 'word1': 5, 'the': 1, 'of': 3 }

input1 = "We reviewed the trip and credited the cancellation fee. The driver has been notified"
input2 = "If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply"

commonWordsCounter = 0
input1 = partA.computeWordFrequencies(partA.tokeinze("file", input1))
input2 = partA.computeWordFrequencies(partA.tokeinze("file", input2))


print(input1)
list1 = sorted(list(input1.keys()))
list2 = sorted(list(input2.keys()))
print(sorted(list(input1.keys())))
print(sorted(list(input2.keys())))
print(input1, input2)
pointer1 = 0
pointer2 = 0

length1 = len(list1)
length2 = len(list2)


while pointer1 < length1 | pointer2 < length2:
    print("something")
    currentWord1 = list1[pointer1]
    currentWord2 = list2[pointer2]

    if currentWord1 <= currentWord2:
        print("INSIDE")
        while currentWord1 < list2[pointer2]:
            pointer2 += 1
        if currentWord1 is list2[pointer2]:
            if input1[currentWord1] < input2[currentWord1]:
                commonWordsCounter += input1[currentWord1]
            else:
                commonWordsCounter += input2[currentWord1]
    elif currentWord2 < currentWord1:
        print("inside")
        while currentWord2 < list1[pointer1]:
            pointer1 += 1
        if currentWord2 == list1[pointer1]:
            if input1[currentWord2] < input2[currentWord2]:
                commonWordsCounter += input2[currentWord2]
            else:
                commonWordsCounter += input1[currentWord2]

print(commonWordsCounter)

# sort by key the two lists
# now just compare each entry.
  # if two entries are equal then add to the final match counter the lower number



# partA.printFrequencies(lista)
