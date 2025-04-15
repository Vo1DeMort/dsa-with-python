from typing import Optional  # sort of nullable

""" with types """
# class Node:
#     def __init__(self,data:Optional[str]=None) -> None:
#         self.data :Optional[str] = data
#         self.next :Optional[Node] = None

""" without types """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# NOTE:
# threee types of linked list
# - singly linked list
# - doubly linked list
# - circular linked list

# NOTE:
# operation of a linked list
# traversing the list (travel across through)
# inserting a data item in the list (at the biginning,middle and end of the list)
# deleting an item from the list

# NOTE:
# list : data elements are stored in different memory location
# array : data elements are stored in contiguous memory location
