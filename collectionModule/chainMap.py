#NOTE: list of dics
from collections import ChainMap

dict1 = {'data':1,'structure':2}
dict2 = {'python':3,'language':4}
chain = ChainMap(dict1,dict2)

print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain['data'])
print(chain['language'])

