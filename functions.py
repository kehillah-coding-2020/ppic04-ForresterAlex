def numOfWords(sentance):
    '''
Takes a string as input and returns the number of words, asusming that " "
seperates the words
    '''
    sentance = sentance.split(" ")
    numWords = len(sentance)
    return numWords

def gitMin(list):
    '''
Takes an input of a list of ints and returns the minimum number
    '''
    min = list[0]
    for item in list[1:]:
        if item < min:
            min = item
    return min

def gitMinIndex(list):
    '''
Takes an input of a list of ints and returns the min by item
    '''
    min = list[0]
    for pos in range(1,len(list)):
        if list[pos] < min:
            min = list[pos]

    return min

def getMax(alist):
    '''
Textbook issued getMax Function
    '''
    maxSoFar = alist[0]
    for item in alist[1:]:
        if item > maxSoFar:
            maxSoFar = item

    return maxSoFar

def getRange(list):
    '''
Gets range of values on a list using gitMin and getMax
    '''
    return getMax(list)-gitMin(list)

def mean(alist):
    '''
Textbook issued mean Function
    '''
    mean = sum(alist)/len(alist)
    return mean

def sumByIteration(list):
    '''
Sum function using accumulator pattern
    '''
    total = 0
    for x in range(len(list)):
        total = total + list[x]

    return total
