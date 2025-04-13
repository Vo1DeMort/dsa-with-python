#NOTE: this one is ineresting

#NOTE:
# a hashable obj is one whose hash value will remain the 
# same during it's life time in the program
# 'Counter' is used to count the number of hashable object
# 'key' is a hashable obj and 'value' is the count of that obj

from collections import Counter

inventory = Counter('hello there')
print(inventory)
print(inventory['l'])
print(inventory['e'])
print(inventory['o'])


