import re
import string


sentence = "This is The sentence's To Tokenize New Work's? hi!I am Go0!DDD"


print(re.sub(r'\W+',' ',sentence.lower()))

