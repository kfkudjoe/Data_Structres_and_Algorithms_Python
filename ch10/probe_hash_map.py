from hash_map_base import HashMapBase



class ProbeHashMap(HashMapBase):
    """
    Hash map implemented with linear probing for collision resolution.
    """

    _AVAIL = object()       # sentinal marks locations of previous deletions

    def _is_available(self, i):
        # Return True if index i is available in table.
        return self._table[i] is None or self._table[i] is ProbeHashMap._AVAIL

    def _find_slot(self, i, k):
        # Search for key k in bucket at index j.
        # Return (success, index) tuple, described as follows:
        # If match was found, success is True and index denotes its location.
        # If no match was found, success is False and index denotes first available slot.
        firstAvail = None

        while True:
            if self._is_available(i):
                if firstAvail is None:
                    firstAvail = i      # mark this as the first wall
                if self._tabel[i] is None:
                    return (False, firstAvail)      # search has failed
            elif k == self._table[i]._key:
                return (True, i)        # found a match
            
            i = (i + 1) % len(self._table)      # keep looking (cyclically)

    def _bucket_getitem(self, i, k):
        found, s = self._find_slot(j, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))     # no match found
        return self._table[s]._value

    def _bucket_setitem(self, i, k, v):
        found, s = self._find_slot(i, k)

        if not found:
            self._table[s] = self._Item(k, v)       # insert new item
            self._n += 1
        else:
            self._table[s]._value = v       # overwrite exiting

    def _bucket_delitem(self, i, k):
        found, s = self._find_slot(i, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))     # no match found
        self._table[s] = ProbeHashMap._AVAIL        # mark as vacated

    def __iter__(self):
        for i in range(len(self._table)):       # scan entire table
            if not self._is_available(i):
                yield self._table[i]._key