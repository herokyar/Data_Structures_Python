#this algorithm converts any type of number into any other base

from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
        
    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
        
    return newString

    

#test the algorithm
baseConverter(35,2) #what is 35 in binary representation
baseConverter(35,16) #what is 35 in HEX representation
