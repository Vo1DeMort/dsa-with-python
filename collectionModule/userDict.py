from collections import UserDict

#NOTE: can add custom functions to the dictionary
class MyDict(UserDict):
    def push(self,key,value):
        raise RuntimeError("cannot insert")

d = MyDict({'ab':1,'bc':2,'cd':3})
d.push('b',2)
