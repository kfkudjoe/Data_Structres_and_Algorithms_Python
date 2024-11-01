from exceptions import Empty



class ArrayQueue:
    """
    FIFO Queue implementation using a Python List as underlying storage.
    """
    DEFAULT_CAPACITY =  10      # moderate capacity for all new queues

    def __init__(self):
        # Create an empty queue.
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size

    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0

    def first(self):
        # Return (but do not remove) the element from the front of the queue.
        # Raise empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty.")
        
        return self._data[self._front]

    def dequeue(self):
        # Remove and return the first element of the queue (i.i, FIFO)
        # Raise empty exception  if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is  empty")

        answer = self._data[self._front]
        self._data[self._front] =  None     # Collect garbage
        self._size -=  1

        return answer

    def enqueue(self, e):
        # Add an element to the back of the queue.
        if self._size == len(self._data):       #  If not enough room in current array size
            self._resize(2 * len(self.data))        # Double the array size
        
        availablle = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def _resize(self, cap):     # we assume  cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data        # keep track of existing list
        self._data  =  [None] * cap     # allocate list with new capacity
        walk = self._front

        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk  = (1 + walk) % len(old)   # use old size as modulus
        
        self._front = 0     # front has been realigned