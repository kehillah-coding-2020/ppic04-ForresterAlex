#!/usr/bin/env python3
#
# pp. 131, 132, 134
#
from functions import *
"""
4.14 Implement the `getMin()` function using iteration by index.
"""
numbers = [17,12,4,32]
print(gitMin(numbers))

"""
4.15 Implement the `getMin()` function using iteration by item.
"""

print(gitMinIndex(numbers))

"""
4.16 Rewrite the `getRange()` function using `getMin()` and `getMax()`.
"""
print(getRange(numbers))


"""
4.17 Create a list of the number of students in each of your classes. Use
the `mean()` function on that list.
"""
numOfStudents = [10,15,17,13,11,12,14]
print(mean(numOfStudents))


"""
4.18 Replace the call to the `sum()` function with an iteration that
computes the total of the values in `alist`.
"""
print(sumByIteration(numOfStudents))


"""
4.19 Why is it important to make a copy of a list before sorting?
"""

#Creating a copy of a list allows you to reference the origional list before it
#was sorted, therefore giving you a reference, and preserving the origional data
#set.

"""
4.20 Find the mean age of ten people near you.
"""



"""
4.21 Find the mean age of ten people near you and your professor, who is
41 years old.
"""



"""
4.22 Find the median age of ten people near you.
"""



"""
4.23 Find the median age of ten people near you, plus your
professor.
"""
