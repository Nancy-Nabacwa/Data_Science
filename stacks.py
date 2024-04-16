#Implementing stack in a list

stack = []

#pushing elements into a stack
stack.append('Lovelace')
stack.append('good')
stack.append(2024)
stack.append('class')

print(stack)#prints elements in list form. output ['Lovelace' , 'good' , 2024 , 'class']

#stack.pop() works in LIFO principle(Last In First Out).
stack.pop()#removes item 'class'
print(stack)# result is ['Lovelace' , 'good' , 2024]

#repeating the process removes all elements until the stack remains empty.
stack.pop()
stack.pop()
stack.pop()
print(stack)#result is []

#popping an empty stack returns an error as stack is now empty and does not have
#elements to pop
#stack.pop()
#print(stack)# output //pop from empty list



#Python stack can be implemented using the deque class from the collections module.
# Deque is preferred over the list in the cases where we need quicker append and pop operations 
#from both the ends of the container
from collections import deque

stack = deque()

#pushing elements into a stack
stack.append('Love')
stack.append('good')
stack.append(2023)
stack.append('classrooom')

print(stack) #prints deque(['Love , 'good' , 2023 , 'classroom'])

# Python stack can also be implemented using the Queue module. elements are inserted into Queue 
#using the put() function and get() takes data out from the Queue.  
from queue import LifoQueue


stack = LifoQueue(maxsize=4) #This states the maximum elements to be in the stack. ie 4
#using the put() method to insert elements in a stack.
stack.put('Nancy')
stack.put('good')
stack.put(2002) 

print(stack.qsize())# printing the size of the stack. ie stack has 3 elements.

# get() function pops elements from stack in LIFO order.

print(stack.get())# output 2002
print(stack.get())# output 'good'
print(stack.get())# output 'Nancy'

#the result of the operation above is an empty stack.

x = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

for sublist in x:
    for number in sublist:print(number)
       
