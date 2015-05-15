# -*- coding: utf-8 -*-
########################################################################################################################################################################################################################
#                                                       Project Euler Problem 42 Solution -- Coded Triangle Numbers
#                                                                           By Mike Kane
#
#
#  The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
#  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#  By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
#
#  If the word value is a triangle number then we shall call the word a triangle word.
#
#  Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
#
########################################################################################################################################################################################################################

def getTriangleNumber(n):
    return int((n + 1) * (n * .5))
    
def alphaIndex(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if letter in alphabet:
        return alphabet.index(letter) + 1
    else:
        return 0

def getWordValue(word):
    total = 0
    for letter in word:
        
        total += alphaIndex(letter)
    return total

def getWords():
    f = open('p042_words.txt', 'r')
    wordList = f.readline()
    wordList = wordList.split(',')
    for item in wordList:
        item = item.strip('"')
    f.close()
   
    return wordList
    
def getAnswer():
    triangleNumberList = []
    triangleNumber = 0
    counter = 0
    
    for x in xrange(1, 500):
        triangleNumber = getTriangleNumber(x)
        if triangleNumber < 1000:
            triangleNumberList.append(triangleNumber)
    
    wordList = getWords()
    
    for word in wordList:
        if getWordValue(word) in triangleNumberList:
            counter += 1
    return counter 
    
        
        
        

    

    
    
    