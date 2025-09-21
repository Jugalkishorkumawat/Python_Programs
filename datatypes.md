 #object types/ Data types in Python
# int, float, str, bool, list, tuple, set, dict
# mutable vs immutable
# mutable - can be changed
# immutable - cannot be changed
# int, float, str, bool, tuple - immutable
# list, set, dict - mutable
# everything in python is an object
# everything in python has a type       
# type() function to check the type of an object
# id() function to check the memory address of an object
# memory address of an object is unique and constant for the object during its lifetime
# two objects with same value will have different memory address
# if we change the value of an object, its memory address will change
# if we assign a new value to a variable, its memory address will change                                                            
# if we change the value of a mutable object, its memory address will not change
# if we change the value of an immutable object, its memory address will change
# variables are just labels to refer to objects in memory
# we can assign multiple variables to the same object
#-Number : 123, 12.34, -56, 0
#-String : "Hello", 'World', """Python""", '''Programming'''
#-Boolean : True, False
#-List : [1, 2, 3], ['a', 'b', 'c'], [1, 'a', 2.5]
#-Tuple : (1, 2, 3), ('a', 'b', 'c'), (1, 'a', 2.5)
#-Set : {1, 2, 3}, {'a', 'b', 'c'}, {1, 'a', 2.5}
#-Dictionary : {'name': 'Alice', 'age': 25}, {1: 'a', 2: 'b', 3: 'c'}

#-File : open('file.txt', 'r'), open('file.txt', 'w')
#-Function : def func(): pass, lambda x: x+1
#-Module : import math, import os
#-Class : class MyClass: pass
#-Instance : obj = MyClass()
#-Exception : try: pass except Exception as e: pass
#-Range : range(10), range(1, 10), range(1, 10, 2)
#-Bytes : b'Hello', bytes([65, 66, 67])
#-Bytearray : bytearray(b'Hello'), bytearray([65,
# special data types : None, Ellipsis