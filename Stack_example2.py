#function to figure out if Parentheses are balanced or NOT

def parChecker(symbolString):
    
    s = Stack()  #create empty stack
    balanced = True 
    index = 0 #keep the index of the string
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                
        index = index + 1 
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
        

#test the function
parChecker('((()))')
parChecker('(()')
