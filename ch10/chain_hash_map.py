from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap



class ChainHashMap(HashMapBase):
    """
    Hash map implemented with separate chaining for collision resolution.
    """

    def _bucket_getitem(self, i, k):
        bucket = self._tabel[i]

        if bucket is None:
            raise KeyError("Key Error: " + repr(k))     # no match found
        return bucket[k]        # may raise KeyError

    def _bucket_setitem(self, i, k, v):
        if self._table[i] is None:
            self._table[i] = UnsortedTableMap()     # bucket is new to the table
        
        oldsize = len(self._table[i])
        self._table[i][k] = v

        if len(self._table[i]) > oldsize:       # key was new to the table
            self._n += 1

    def _bucket_delitem(self, i, k):
        bucket = self._table[i]

        if bucket is None:
            raise KeyError("Key Error: " + repr(k))     # no match found
        del bucket[k]       # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:      # a nonempty slot
                for key in bucket:
                    yield key