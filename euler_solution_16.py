#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 21000?

def main():
    number = 0
    sumOfDigits = 0
    
    number = str(2**1000)
    
    for x in number:
        sumOfDigits += int(x)
    print sumOfDigits