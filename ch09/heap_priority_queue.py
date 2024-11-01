from priority_queue_base import PriorityQueueBase
from exceptions import Exception



class HeapPriorityQueue(PriorityQueueBase):     # Base class defines _Item
    """
    A min-oriented priority queue implemented with a binary heap.
    """

    #------------------------------ Nonpublic Methods ------------------------------#
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)      # Is index beyond the end of the list?

    def _has_right(self, i):
        return self._right(i) < len(self._data)     # Is index beyond the end of the list?

    def _swap(self, i, j):
        # Swap the elmeents at indices i and j of array
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent = self._parent()

        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)        # recurse at position of parent

    def _downheap(self, i):
        if self._has_left(i):
            left = self._left(i)
            small_child = left      # although right may be smaller

            if self._has_right(i):
                right = self._right(i)
            
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[i]:
                self._swap(i, small_child)
                self._downheap(small_child)     # recurse at position of small child

    #------------------------------ Public Methods ------------------------------#
    def __init__(self):
        # Create a new empty Priority Queue
        self._data = []

    def __len__(self):
        # Return the number of items in the Priority Queue
        return len(self._data)

    def add(self, key, value):
        # Add a key-value pair to the priority queue
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)       # uphead newly added position

    def min(self):
        # Return but do not remove (k, v) tuple with minimum key.
        # Raise Empty exception if empty.
        if self.is_empty():
            raise Empty("Priority queue is empty")

        item = self._data[0]
        
        return (item._key, item._value)

    def remove_min(self):
        # Remove and return (k, v) tuple with minimum key.
        # Raise Empty exception if empty.
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        self._swap(0, len(self._data) - 1)      # put minimum item at the end
        
        item = self._data.pop()     # remove minimum item from the list
        
        self._downheap(0)       # fix the new root

        return (item._key, item._value)