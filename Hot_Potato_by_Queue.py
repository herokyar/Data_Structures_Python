#famous hot potato problem , an algorithm using python queue data class

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    
    simqueue = Queue() #create a new queue
    
    for name in namelist:
        simqueue.enqueue(name)
        
    while simqueue.size() > 1 :
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) #the first in queue leaves the queue and enters again.
        
        #simqueue.dequeue()
        break
        
    return simqueue.dequeue()

#test the code
hotPotato(["Anna","Chelsea","Jean","Jane","Aaron","Tom"],1)
