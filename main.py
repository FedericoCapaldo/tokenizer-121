import re
import string
import myClass
import time

start_time = time.time()

# x = myClass.myClass()
# print(x.myPrint())

text_fetched = ""

# considering opening file with a wildcard if possible
with open('file2.txt', 'r') as file:
    for line in file:
        text_fetched += line



# tokenizing
print(re.sub('\W+', ' ', text_fetched.lower()))

# time result
print("--- %s seconds ---" % (time.time() - start_time))
