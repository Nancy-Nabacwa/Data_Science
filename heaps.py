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

# import heapq
# array = [2,4,10,5,15,1,3]
# maxHeap = []
# for num in array:
#     heapq.heappush(maxHeap, -num)
# print("maxHeap:", maxHeap)


# def max_heapify(A, k):
#     l = left(k)
#     r = right(k) 
#     if l < len(A) and A[l] > A[k]:
#         largest = l
#     else:
#         largest = k
#     if r < len(A) and A[r] > A[largest]:
#         largest = r
#     if largest != k:
#         A[k], A[largest] = A[largest], A[k]
#         max_heapify(A, largest)
# def left(k):
#     return 2 * k + 1
# def right(i):
#     return 2 * i + 2 
# def build_max_heap(A):
#     n = int((len(A)//2)-1)
#     for k in range(n, -1, -1):
#         max_heapify(A, k)
# A = [3, 9, 2, 1, 4, 5]
# build_max_heap(A)
# print(A)


# Qn.1 Can you explain heap property maintenance after a delete and insert operation?

# Upward heapify on insertion
# def heapify_upwards(heap, i):# input parameters(heap=list representing heap, i=index of element added to the heap)
    # parent = (i - 1) // 2 #Calculates the index of the parent node.
    # if parent >= 0 and heap[parent] < heap[i]:
    #     heap[parent], heap[i] = heap[i], heap[parent]
    #     heapify_upwards(heap, parent)
    #     print(heap)

#This function is used to insert a new element into the heap.
# def insert_element(heap, element):
#     heap.append(element)
#     heapify_upwards(heap, len(heap) - 1)
#     print(heap)

# heap = [100,5,90,6,30]

# heapify_upwards(heap, 4)
# insert_element(heap, 200)
# heapify_upwards(heap, 5)


# Downward heapify on deletion
#This function ensures that the max-heap property is maintained after a deletion. 
#It checks the left and right children of the node at index i and swaps the node with the largest child if necessary.
def heapify_downwards(heap, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    largest = i

    if left_child < len(heap) and heap[left_child] > heap[largest]:
        largest = left_child
    if right_child < len(heap) and heap[right_child] > heap[largest]:
        largest = right_child

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify_downwards(heap, largest)
        print(heap)

def delete_max(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    deleted_element = heap.pop()
    heapify_downwards(heap, 0)
    return deleted_element

heap = [500,5,90,6,305,2]

heapify_downwards(heap, 4)
