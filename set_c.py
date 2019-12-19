#!/usr/bin/env python3
#
# pp. 139, 145
#
from functions import *
"""
4.24 You have been given the following list of students and their test
scores

	`names = ['joe', 'tom', 'barb', 'sue', 'sally']`
	`scores = [10, 23, 13, 18, 12]`

Write a function, `makeDictionary()` that takes
the two lists and returns a dictionary with the names as the key and
the scores as the values. Assign the result of `makeDictionary()` to
`scoreDict`, which will be used in the exercises that follow.
"""
names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]
scoreDict = makeDictionary(names,scores)
"""
4.25 Using `scoreDict`, find the score for 'barb'.
"""
print(scoreDict['barb'])


"""
4.26 Add a score of 19 for 'jon'.
"""

scoreDict['jon']=19

"""
4.27 Create a sorted list of all the scores in `scoreDict`.
"""
list = list(scoreDict.values())
list.sort()
print(list)

"""
4.28 Calculate the average of all the scores in `scoreDict`.
"""

print(mean(list))

"""
4.29 Update the score for `sally` to be 13.
"""

scoreDict['sally']=13
print(scoreDict)
"""
4.30 Tom has just dropped this class. Delete 'tom' and his score from
`scoreDict`.
"""



"""
4.31 Print out a table of students and their scores with the students
listed in alphabetical order.
"""



"""
4.32 Write a function called `getScore()` that takes a name and a
dictionary as parameters and returns the score for that name if it is
in the dictionary. If the name is not in the dictionary, print an
error message and return -1.
"""



"""
4.34 Modify `frequencyTableAlt()` so that it returns a list of key-count
tuples.
"""



"""
4.35 Suppose you have a list of key-score values like the
following:

	[('john',10), ('bob',8), ('john',5), ('bob',17), ...]

Write a function that takes such a list as a parameter and
prints out a table of average scores for each person.
"""
