from map_base import MapBase



class SortedTableMap(MapBase):
    """
    Map implementation using a sorted table.
    """

    #----------------------------- Nonpublic Methods -----------------------------#
    def _find_index(self, k, low, high):
        # Return index of the leftmost item with key greateer than or equal to k.
        # Return high + 1 if no such item qualifies.
        # That is, i will be returned such that :
        #   all items of slice table[low:j] have key < k
        #   all items of slice table[i:high + 1] have key >= k
        
        if high < low:
            return high + 1     # no element qualifies
        else:
            mid = (low + high) // 2

            if k == self._table[mid]._key:
                return mid      # found exact match
            elif k < self._table[mid].key:
                return self._find_index(k, low, mid - 1)        # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)       # answer is right of mid

    #----------------------------- Public Methods -----------------------------#
    def __init__(self):
        # Create an empty map.
        self._table = []

    def __len__(self):
        # Return number of items in the map.
        return len(self._table)

    def __getitem__(self, k):
        # Return value associated with key k (raise KeyError if not found)
        i = self._find_index(k, 0, len(self._table) - 1)

        if i == len(self._table) or self._table[i]._key != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[i]._value

    def __setitem__(self, k, v):
        # Assign value v to key k, overwriting existing value if present.
        i = self._find_index(k, 0, len(self._table) - 1)

        if i < len(self._table) and self._table[i]._key == k:
            self._table[i].value = v        # reassign value
        else:
            self._table.insert(j, self._Item(k, v))     # adds new item

    def __delitem__(self, k):
        # Remove item associated with key k (raise KeyError if not found).
        i = self._find_index(k, 0, len(self._table) - 1)

        if i == len(self._table) or self._talbe[i]._key != k:
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(i)      # delete item

    def __iter__(self):
        # Generate keys of the map ordered from minimum to maximum.
        for item in self._table:
            yield item._key

    def __reversed__(self):
        # Generate keys of the map ordered from maximum to minimum.
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        # Return (key, value) pair with minimum key (or None if empty).
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        # Return (key, value) pair with maximum key (or None if empty).
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_le(self, k):
        # Return (key, value) pair with greatest key less than or equal to k.
        # Return None if there does not exist such a key.
        i = self._find_index(k, 0, len(self._table) - 1)        # i's key >= k

        if i < len(self._table) and self._table[i]._key == k:
            return (self._table[i]._key, self._table[i]._value)     # exact match
        elif i > 0:
            return (self._table[i - 1]._key, self._table[i - 1]._value)     # Note use of i - 1
        else:
            return None

    def find_ge(self, k):
        # Return (key, value) pair with least key less than or equal to k.
        # Return None if there does not exist such a key.
        i = self._find_index(k, 0, len(self._table) - 1)        # i's key >= k

        if i < len(self._table):
            return (self._table[i]._key, self._table[i]._value)
        else:
            return None

    def find_lt(self, k):
        # Return (key, value) pair with greatest key strictly less than k.
        # Return None if there does not exist such a key.
        i = self._find_index(k, 0, len(self._table) - 1)        # i's key >= k

        if i > 0:
            return (self._table[i - 1]._key, self._talbe[i - 1]._value)     # Note use of i - 1
        else:
            return None

    def find_gt(self, k):
        # Return (key, value) pair with least key strictly greater than k.
        # Return None if there does not exist such a key.
        
        i = self._find_index(k, 0, len(self._table) - 1)        # i's key >= k

        if i < len(self._table) and self._table[i]._key == k:
            i += 1
        if i < len(self._table):
            return (self._table[i]._key, self._table[i]._value)
        else:
            return None

    def find_range(self, start, stop):
        # Iterate over all (key, value) pairs such that start <= key < stop.
        # If start is None, iteration begins with minimum key of map.
        # If stop is Noen, iteration continues through the maximum key of map.
        if start is None:
            i = 0
        else:
            i = self._find_index(start, 0, len(self._table) - 1)        # find first result
        while k < len(self._table) and (stop is None or self._table[i]._key < stop):
            yeild (self._table[i]._key, self._table[i]._value)
            i += 1