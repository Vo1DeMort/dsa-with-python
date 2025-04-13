from collections import namedtuple

#NOTE: nt= namedtuple(typename, field_names)
Book = namedtuple('BookType',['name','ISBN','quantity'])
Book1 = Book('hands on data structure and algorithm',
             '19837410948',
             '50'
             )

print(Book)
print(Book1)
print('using index ISBN : '+Book1[1])
print('using key ISBN : '+Book1.ISBN)
