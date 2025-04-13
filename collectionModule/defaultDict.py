#NOTE: sub class of normal dict
# the only difference is no KeyError

from collections import defaultdict

# NOTE: creates default value 0 , if the key does not exist
# without raising error which a normal dic would
dd = defaultdict(int)

words = str.split(('data python data data structure data python'))

for word in words:
    dd[word]+=1

print(dd)
