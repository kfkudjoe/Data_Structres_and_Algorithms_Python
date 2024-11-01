import ctypes



class DynamicArray:
    """
    A dynamic array class akin to a symplified Python list.
    """
    
    def __init__(self):
        # Create an empty array.
        self._n = 0     # count of actual elements
        self._capacity = 1      # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        # Return the number of elements in the array.
        return  self._n

    def __getitem__(self, k):
        # Return element at index k.
        if not 0 <= k <= self._n:
            raise IndexError("Invalid index")
        return self._A[k]       # retrieve from array

    def append(self, obj):
        # Add object to the end of the array.
        if self._n == self.capacity:        # check if there is enough room
            self._resize(2 * self._capacity)        # double the capacity
        self.A[self._n] = obj
        self._n += 1

    def _resize(self, c):       # nonpublic utility
        # Resize internal array to capacity c.
        B = self._make_array(c)     # new (bigger) array

        for k in range(self._n):        # for each existing value
            B[k] = self._A[k]       # offload the values of the initial array into the new array
        self._A = B     # replace the small (older) array with the big (newer) array
        self._capacity = c      # update the capacity of the array to the new bigger one's size

    def _make_array(self, c):       # nonpublic utility
        # Return new array with capacity c.
        return (c * ctypes.py_object)()     # see cytpes documentation        

    def insert(self, k, value):
        # Insert value at index  k, shifting subsequent values rightward.
        # (For simplicity, we assume 0 <= k <= n within this version)
        if self._n == self._capacity:       # check if there is enough room
            self._resize(2 * self._capacity)    # double the capacity
        
        for i in range(self._n, k, -1):     # shiftall elements in A starting with self[A]
            self._A[i] = self._A[i - 1]
        self._A[k] = value      # store newest element
        self._n += 1


    def remove(self, value):
        # Remove first occurence of value (or raise ValueError).
        # We do not consider shrinking the dynmaci array in this version.

        for i in range(self._n):
            if self._A[i] == value:     # If the value passed in the "value" argument equals the value stored at the ith index of set _A
                for j in range(i, self._n - 1):     # shift others to fill the gap
                    self._A[j]=  self._A[j + 1]
                self._A[self._n - 1] = None     # help garbage collection
                self._n -= 1        # we have one less  item
                return      # exit
        raise ValueError("Value not found")     #  only erached if there is no match