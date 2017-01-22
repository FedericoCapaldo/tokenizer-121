import re
import string
import time

start_time = time.time()


text_fetched = ""
# alphanum = re.compile('[ a-zA-Z0-9]*')
# alphanumsub = re.compile('\W+')

# considering opening file with a wildcard if possible
with open('file1.txt') as file:
    for line in file:
        text_fetched += line

# subsititue text_fetched with what you want to 'tokenize'
#resultTokenized = alphanum.findall(text_fetched.lower())
# print(alphanum.findall(text_fetched.lower()))
# print(alphanumsub.sub(' ', text_fetched.lower()))

# the other way, and this works.
result = re.sub('\W+', ' ', text_fetched.lower())


# time result
print("--- %s seconds ---" % (time.time() - start_time))
