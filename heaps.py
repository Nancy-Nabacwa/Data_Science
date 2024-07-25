# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if value <= self.value:
#             if self.left == None:
#                 self.left = Node(value)
              

#             else:
#                 self.left.insert(value)
        
#         else:
#             if self.right == None:
#                 self.right = Node(value)

#             else:
#                 self.right.insert(value)


#     def find(self, value):
#         if value == self.value:
#              return True
#         elif value < self.value:
#             if self.left == None:
#              return False
#             else:
#              return self.left.find(value)
#         else:
#             if self.right == None:
#              return False
#             else:
#              return self.right.find(value)


# tree = Node(100)

# print(tree.insert(9))
# print(tree.insert(19))

import heapq
array = [2,4,10,5,15,1,3]
maxHeap = []
for num in array:
    heapq.heappush(maxHeap, -num)
print("maxHeap:", maxHeap)


def max_heapify(A, k):
    l = left(k)
    r = right(k) 
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
def left(k):
    return 2 * k + 1
def right(i):
    return 2 * i + 2 
def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k)
A = [3, 9, 2, 1, 4, 5]
build_max_heap(A)
print(A)