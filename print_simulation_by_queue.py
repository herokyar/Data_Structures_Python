#python printing queue simulation

import random
from pythonds.basic.queue import Queue


class Printer:
    
    def __init__(self, ppm): #ppm=pages per minute
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
        
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <= 0:
                self.currentTask = None
                
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
        
        


class Task:
    
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
        
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
        


from pythonds.basic.queue import Queue

import random

def simulation(numSeconds, pagesPerMinute):
    
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
            
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
            
        labprinter.tick()
        
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
    
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    


#test the simulation
for i in range(10): #run 10 simulation
    simulation(3600, 10)  #3600 secs=1 hour and 10pages/minute

