def numOfWords(sentance):
    '''
Takes a string as input and returns the number of words, asusming that " "
seperates the words
    '''
    sentance = sentance.split(" ")
    numWords = len(sentance)
    return numWords
