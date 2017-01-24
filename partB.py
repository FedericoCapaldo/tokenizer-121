import partA

lista = { 'one': 2, 'word1': 5, 'the': 1, 'of': 3 }

input1 = "We reviewed the trip and credited the cancellation fee. The driver has been notified"
input2 = "If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply"


input1 = partA.computeWordFrequencies(partA.tokeinze("file", input1))
input2 = partA.computeWordFrequencies(partA.tokeinze("file", input2))

# sort by key the two lists
# now just compare each entry.
  # if two entries are equal then add to the final match counter the lower number



# partA.printFrequencies(lista)
