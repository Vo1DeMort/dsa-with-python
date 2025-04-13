from collections import UserList

#NOTE: can add custom functionality to the list
class MyList(UserList):
    def push(self,key):
        raise RuntimeError("cannot inset into the list")

d = MyList([11,12,13])
d.push(2)
