#!/usr/bin/env python3
#
# p. 127
#
from functions import *
"""
4.1 Create a list with the following five items: `7, 9, 'a', 'cat',
False`. Assign this list to the variable `myList`
"""
myList = [7,9,'a','cat',False]


"""
4.2 Write Python statements to do the following:

(a) Append 3.14 and 7 to the list.
(b) Insert the value 'dog' at position 3.
(c)Find the index of 'cat'.
(d) Count the number of 7s in the list.
(e) Remove the first 7 from the list.
(f) Remove 'dog' from the list, using `pop()` and `index()`
"""

myList.extend([3.14,7])
myList.insert(3, 'dog')
print(myList.index('cat'))
print(myList.count(7))
myList.remove(7)
myList.pop(myList.index('dog'))
print(myList)

"""
4.3 Split the string 'The quick brown fox' into a list of words.
"""

string = 'The quick brown fox'

listString = string.split(" ")

print(listString)
"""
4.4 Split the string 'mississippi' into a list using 'i' as the split
point.
"""
string = 'mississippi'

listString = string.split("i")

print(listString)
"""
4.5 Write a function that takes a sentence as a parmeter and returns the
number of words in the sentence.
"""

print(numOfWords("Hello Bob, this is your Mother"))

"""
4.6 Although Python provides us with many list methods, it is good
practice and very instructive to think about how they are
implemented. Implement a python function that works like the
following:

(a) `count`
(b) `in` - return `True` if item is in list
(c) `reverse`
(d) `index` - return -1 if not in the list
(e) insert

"""



"""
4.7 Write a function `shuffle()` that takes a list and returns a new list
with the elements shuffled into a random order. (Don't use
`random.shuffle()`)
"""



"""
4.8 Write a function `shuffle_ip()` that takes a list as a parameter and
shuffles the list in place. (Hint: This is like a mutator method)
"""



"""
4.9 * Draw a reference diagram to illustrate the differences between the
previous two exercises.
"""



"""
4.10 Suppose you initialize the following list: `myList = [[]]*3`.
Evaluate the expression and describe the result.
"""

myList = [[]]*3

#Creates a list with 3 empty items, each being '[]'

"""
4.11 Now evaluate the expression `myList[1].append(2)`, and describe the
result.
"""
