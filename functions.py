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
Takes an input of a string and returns the minimum number
    '''
    min = list[0]
    for item in list[1:]:
        if item < min:
            min = item
    return min
