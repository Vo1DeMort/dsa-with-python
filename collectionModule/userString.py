#NOTE: can add custom functions

from collections import UserString

class MyString (UserString):
    def append(self,value):
        self.data += value

s1 = MyString("data")
print("original :",s1)
s1.append('h')
print("agter append: ",s1)
