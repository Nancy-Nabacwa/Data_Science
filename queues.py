
#Using a list
queue1 = []

# Enqueue
queue1.append('Love')
queue1.append('lace')
queue1.append('lab')
queue1.append('is')
queue1.append('good')
print("Queue1: ", queue1)#output['Love','lace','lab','is','good']

# Dequeue
element = queue1.pop(0)
print("Dequeue: ", element)# Love

# Peek
frontElement = queue1[0]
print("Peek: ", frontElement)# lace

# isEmpty
isEmpty = not bool(queue1)
print("isEmpty: ", isEmpty)# false

# Size
print("Size: ", len(queue1))#4


#implementing using class Queue
class Queue:# create class called queue
    def __init__(self):#constructor ie invoked when we create a new queue.self which referes to obejct being created.
        self.queue = []#created list wrapper ie empty list
    
    def enqueue(self, elements):
        self.queue.append(elements)#
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue object i.e myQueue
myQueue = Queue()

myQueue.enqueue('Love')
myQueue.enqueue('lace')
myQueue.enqueue('lab')
print("Queue: ", myQueue.queue)
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

#Implementing Queues using stacks. i.e two stacks.
class Queue: 
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
 
    def enQueue(self, element):
         
        # Move all elements from stack1 to stack2 
        while len(self.stack1) != 0: #while stack1 is not empty
            self.stack2.append(self.stack1[-1]) #push the elements to stack2 push from last element in stack1
            self.stack1.pop()#remove elements from stack1
 
        # Push items into self.stack1 
        self.stack1.append(element) 
 
        # Push everything back to stack1 
        while len(self.stack2) != 0: #while stack2 is not empty
            self.stack1.append(self.stack2[-1]) #push the elements to stack1 from last element in stack2
            self.stack2.pop()# remove elements from stack2
 
    # Dequeue an item from the queue 
    def deQueue(self):
         
        # if stack1 is empty 
        if len(self.stack1) == 0: 
            return -1;
     
        # Return top of self.stack1 
        element = self.stack1[-1] 
        self.stack1.pop() 
        return element
 

stackQueue = Queue()

stackQueue.enQueue("Love") 
stackQueue.enQueue("lace") 
stackQueue.enQueue("lab") 

print("StackQueue2: ", stackQueue.stack2)
print("StackQueue1: ", stackQueue.stack1)

print(stackQueue.deQueue())
print(stackQueue.deQueue())
print(stackQueue.deQueue())