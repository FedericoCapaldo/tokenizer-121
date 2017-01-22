import re
import time

start_time = time.time()

x = ""
with open("file1.txt") as infile:
    for line in infile:
        x += line

r = re.compile(r'(?P<na>[^ \na-zA-Z0-9]*)(?P<a>[ \na-zA-Z0-9]+)')
s = len(x)
c = 0
res = ""
while c < s:
    m = r.match(x, c)
    res += m.group("a")
    c += len(m.group("a")) + len(m.group("na"))
# print res

print("---- %s seconds " % (time.time() - start_time))
