from exceptions import Empty



class LinkedQueue:
    """
    FIFO queue implementation using a singly linked list for storage.
    """

    #-------------------------- Nested Node Class --------------------------#
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked list.
        """

        def __init__(self, element, next):
            self._element = element
            self._next = next

    
    #-------------------------- Queue Methods --------------------------#
    def __init__(self):
        # Create an empty queue.
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        # Return the number of elements in the queue.
        return self._size

    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0

    def first(self):
        # Return (but do not remove) the elemtn at the front of the queue.
        # Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._head._element      # front aligned with the head of the list

    def dequeue(self):
        # Remove and return the first element of the queue (FIFO)
        # Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return answer

    def enqueue(self, element):
        # Add an element to the back of the queue.
        newest = self._Node(element, None)      # node will be new tail node

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest       # special case: previously empty

        self._tail._next = newest       # update reference to tail mode
        self._size += 1