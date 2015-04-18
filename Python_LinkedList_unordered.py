#unordered list : linked list implementation
#first create a node class

class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext
        

#linked list implementation
class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        
        while current != None:
            count = count + 1
            current = current.getNext()
            
        return count
    
    def search(self,item):
        
        current = self.head
        found = False
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        return found
                
        
        
    def remove(self,item):
        
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self,item):
        
        current = self.head
        found = False #to find the last element in the linked list
                         
        while not found:
            if current.getNext() != None:
                current = current.getNext()
            else:
                found = True
        
        temp = Node(item) #create a new node
        current.setNext(temp) #point to the appended node
        
                

    
    def pop(self):
        current = self.head
        previous = None
        found = False
    
        while not found:
            if current.getNext() == None:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
            return current.getData()
        else:
            previous.setNext(current.getNext())
            return current.getData()
                

#test the linked list
mylist.add(31) #add item to the linked list
mylist.add(77) #add item to the linked list
mylist.add(17)

print(mylist.size())  #get the size
print(mylist.search(93)) #search for item

mylist.remove(54) #remove item from the linked list

mylist.append(10) #append to the end of the linked list

mylist.pop() #pop the latest element from the linked list and return the value
