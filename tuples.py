y = 2345,4321,'hello!'
print(y) #output tuples are enclosed in paratheses()so that nested tuples are interpreted correctly.

y = (2345,5432,'hello')
print(y)

y = 'hello', #single tuple constructed followed by a comma
print(y)

y = () #empty tuple
print(y)

t = 8,9,10
z = 11,12,13
x = t + z # concatenating two tuples
print(x)

y = ('DAS','thursday')
x = (998079)
p = (y,x)#nested lists y and x
print(p)

#Accessing elements in a tuple
t = 234,567,'time','for','DAS',678
print(t)
print(t[4])#output 'DAS'
print(t[2:5])#output ('time','for','DAS'). This is slicing in tuple




tuple_dict = {('DAS', 1): 'Sharon', ('HTML', 2): 'Hunter', ('AkiraChix', 3): 'Linda'}
print(tuple_dict[('DAS', 1)])  # outputs 'Sharon'
print(tuple_dict[('HTML', 2)])  # outputs 'Hunter'
print(tuple_dict[('AkiraChix', 3)])  # outputs 'Linda'

#deleting items in a tuple. 
tupleTOEdit = (10, 'Fred', 'Design', 500, 50)

# convert the tuple to a list
turnedList= list(tupleTOEdit)
print (turnedList)  # output: [10, 20, 30, 40, 50]

# deleting second element "Fred"
turnedList.pop(1) # output: [10,'Design',500,50]


#  removing the element "500"
turnedList.remove(500) # output: [10,'Design', 50]

#converting the my_list back to my_tuple
tupleTOEdit = tuple(turnedList)


print (tupleTOEdit)# output: (10,'Design', 50)

