#a function that uses a stack to reverse the chars in a string

def revstring(mystr):
    
    s = Stack() #create a new stack
    
    for ch in mystr:
        s.push(ch)
    
    reverse_string = ''  #create an empty string
    
    for i in range(len(mystr)):
        reverse_string = reverse_string + s.pop()
    
    return reverse_string
    
    
#test the function
revstring('hel')
revstring('abcdefg')
