#import typing

def test(x:int)-> str:
    return f"this is just a {x}"

# print(test('hello there'))
# print(test('hello'))
print(test(45))

class Car():
    def __init__(self) -> None:
        print('this is a car')


def isCar(car:Car)->None:
    if isinstance(car,Car):
        print('this is actually a car')

testCar = Car()
print(isCar(testCar))
#print(isCar('hi'))

