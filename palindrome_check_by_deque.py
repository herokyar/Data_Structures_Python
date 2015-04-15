#palindrome checking algorithm using deque data structure (works by comparing the first and the last item in the deque)

from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque() #create a deque object
    
    for ch in aString:
        chardeque.addRear(ch)
        
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
            
    return stillEqual
    


#test the algorithm
palchecker('madam')
palchecker('test')


