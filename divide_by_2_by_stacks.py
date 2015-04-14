#this algorithm converts a decimal number into a binary number by using Divide by 2 algorithm

from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack() #create an empty stack
    
    while decNumber > 0:
        rem = decNumber % 2 #get the remainder
        remstack.push(rem) #push the remainder into the stack
        decNumber = decNumber // 2  #updata decNumber
    
    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
        
    return binString
    

#test the function
divideBy2(25)
