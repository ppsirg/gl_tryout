"""
Write a python program in an object-oriented way to achieve the following:
Below there’s an example of how it should work, see it carefully:
> mylist = List()
> mylist.append(1).append(2).append(3).append(4).append(5)
> list(mylist.items())
[1,2,3,4,5]
> list(mylist.map(lambda x: x*x).items())
[1, 4, 9, 16, 25]
> list(mylist.map(lambda x: x*x).filter(lambda x: x > 3 and x < 25).items())
[4,9,16]
> list(mylist.map(lambda x: x*x).filter(lambda x: x > 3 and x < 25).reduce(lambda x,y:
x+y).items())
[29]
> list(mylist.items())
[1,2,3,4,5]
The class “List” allows you to work with any number of items.
Functionality:
Implement the map, filter and reduce functions from scratch.
Write a program that validates how it works. It could be a function inside of the same
program.
Add some tests to validate this functionality.
Note:
● Don’t use the map, filter and reduce that are built-in in Python.
● Don’t use any sequence type included in Python such as str, tuple, list, dict, set or
any other to handle the List’s items. To get it done you’ll need to implement your
sequence type, you could try with a Linked List or something else.
"""

class List(object):

    def __next__(self):
        pass
    
    def append(self, item):
        pass

    def map(self, func):
        pass

    def items(self):
        pass

    def filter(self, func):
        pass

    def reduce(self, func):
        pass