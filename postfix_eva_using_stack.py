#evaluate a postfix expression and return the answer

from pythonds.basic.stack import Stack #import the Stack library

def postfixEval(postfixExpr):
    operandStack = Stack() #create a new stack
    tokenList = postfixExpr.split()  #split the expression by space
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    
    return operandStack.pop()

def doMath(op, op1, op2): #helper math function to to the math
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2
    

#test the function

print(postfixEval('2 8 + 4 2 + /'))
