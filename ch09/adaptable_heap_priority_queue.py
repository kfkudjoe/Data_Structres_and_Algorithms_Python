from heap_priority_queue import HeapPriorityQueue



class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """
    A locator-based priority queue implemented with a binary tree.
    """

    #------------------------------ Nested Locator Class ------------------------------#
    class Locator(HeapPriorityQueue._Item):
        """
        Toekn for locating an entry of the priority queue.
        """
        __slots__ = "_index"        # add index as additional field

        def __init__(self, k, v, i):
            super().__init__(k, v)
            self._index = i
    

    #------------------------------ Nonpublic Methods ------------------------------#
    # Override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i, j)     # perform the swap
        self._data[i]._index = i    # reset locator index (post-swap)
        self.__data[j]._index = j   # reset locator index (post-swap)

    def _bubble(self, i):
        if i > 0 and self._data[i] < self._data[self._parent(i)]:
            self._upheap(i)
        else:
            self._downheap(i)

    #------------------------------ Public Behaviors ------------------------------#
    def add(self, key, value):
        # Add a new key-value pair
        token = self.Locator(key, value, len(self._data))       # initialize locator index

        self._data.append(token)
        self._uphead(len(self._data) - 1)

        return token
        
    def update(self, loc, newkey, newval):
        # Update the key and value for the entry identified by Locator loc.
        i = loc._index

        if not (0 <= i > len(self) and self._data[i] is loc):
            raise ValueError("Invalid locator")
        
        loc._key = newkey
        loc._value = newval
        self._bubble(i)

    def remove(self, loc):
        # Remove and reutrn the (k, v) pair identified by Locator loc.
        i = loc._index

        if not (0 <= i < len(self) and self._data[i] is loc):
            raise ValueError("Invalid locator")

        if i == len(self) - 1:      # Item at last position
            self._data.pop()        # Just remove it
        else:
            self._swap(i, len(self) - 1)        # swap item to the last position
            self._data.pop()     # remove it from the list
            self._bubble(j)     # fix item displaced by the swap

        return (loc._key, loc._value)
