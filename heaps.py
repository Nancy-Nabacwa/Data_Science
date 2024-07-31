class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = Node(value)
              

            else:
                self.left.insert(value)
        
        else:
            if self.right == None:
                self.right = Node(value)

            else:
                self.right.insert(value)


    def find(self, value):
        if value == self.value:
             return True
        elif value < self.value:
            if self.left == None:
             return False
            else:
             return self.left.find(value)
        else:
            if self.right == None:
             return False
            else:
             return self.right.find(value)


tree = Node(100)

print(tree.insert(9))
print(tree.insert(19))

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


# Qn.1 Can you explain heap property maintenance after a delete and insert operation?

# Upward heapify on insertion
def heapify_upwards(heap, i):# input parameters(heap=list representing heap, i=index of element added to the heap)
    parent = (i - 1) // 2 #Calculates the index of the parent node.
    if parent >= 0 and heap[parent] < heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent]
        heapify_upwards(heap, parent)
        print(heap)

#This function is used to insert a new element into the heap.
def insert_element(heap, element):
    heap.append(element)
    heapify_upwards(heap, len(heap) - 1)
    print(heap)

heap = [100,5,90,6,30]

heapify_upwards(heap, 4)
insert_element(heap, 200)
heapify_upwards(heap, 5)


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

#Qn 2 Describe the algorith for merging sorted arrays using a minimum heap

import heapq

def merge_k_sorted_arrays(arrays):
    result = []
    
    # Initialize min-heap with first element from each array
    heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]#Loop while keeping track of the index of the current item.
    heapq.heapify(heap)
    
    # While heap is not empty, keep track of minimum element
    while heap:
        #The smallest element is popped from the heap, and its value is appended to the result list.
        val, array_index, next_index = heapq.heappop(heap)
        result.append(val)
        next_index += 1
        if next_index < len(arrays[array_index]):
            heapq.heappush(heap, (arrays[array_index][next_index], array_index, next_index))
    
    return result


arrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8, 9]]
merged = merge_k_sorted_arrays(arrays)
print(merged) 

#Qn 3 What is Heap Sort?
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

#Qn 4 Given an integer array, check if it represents min-heap or not.
# Function to check if the given list represents min-heap or not
def checkMinHeap(A, i):
 
    # if `i` is a leaf node, return true as every leaf node is a heap
    if 2*i + 2 > len(A):
        return True
 
    # if `i` is an internal node
 
    # recursively check if the left child is a heap
    left = (A[i] <= A[2*i + 1]) and checkMinHeap(A, 2*i + 1)
 
    # recursively check if the right child is a heap (to avoid the list index out
    # of bounds, first check if the right child exists or not)
    right = (2*i + 2 == len(A)) or (A[i] <= A[2*i + 2]
                                    and checkMinHeap(A, 2*i + 2))
 
    # return true if both left and right child are heaps
    return left and right
 
 
if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5, 6]
 
    # start with index 0 (the root of the heap)
    index = 0
 
    if checkMinHeap(A, index):
        print('The given list is a min-heap')
    else:
        print('The given list is not a min-heap')


