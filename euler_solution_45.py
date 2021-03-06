# -*- coding: utf-8 -*-
########################################################################################
#                           Project Euler Problem 45 Solution
#                               By Mike Kane
#
#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.
#
#Find the next triangle number that is also pentagonal and hexagonal.
########################################################################################

#  create function that generates triangle numbers
#  create function that generates pentagonal numbers
#  create function that generates hexagonal numbers

# populate list of triangle numbers
# populate list of pentagonal numbers
# populate list of hexagonal numbers

#loop through triangle numbers list and check against each number in pentagonal/hexagonal numbers lists
import time
triangleNumbers = []
pentagonalNumbers = []
hexagonalNumbers = []

def getTriangleNumber(number):
    return number*(number + 1) /2

def getPentagonalNumber(number):
    return number*(3 * number - 1) /2
    
def getHexagonalNumber(number):
    return number*(2*number - 1)/2
    
def populateLists(start, stop):
    counter = start
    while len(triangleNumbers) < stop and len(pentagonalNumbers) < stop and len(hexagonalNumbers) < stop:
        triangleNumbers.append(getTriangleNumber(counter))
        pentagonalNumbers.append(getPentagonalNumber(counter))
        hexagonalNumbers.append(getHexagonalNumber(counter))
        
        counter += 1



def getAnswer():
    start = time.time()
    for number in triangleNumbers:
        for numberP in pentagonalNumbers:
            for numberH in hexagonalNumbers:
                if number == numberP and numberP == numberH:
                    print number
    print "Total Runtime: " + str(time.time() - start)
    
    