from collections import MutableMapping



class MapBase(MutableMapping):
    """
    An abstract base class that includes a nonpublic _Item class.
    """

    #------------------------------ Nested _Item Class ------------------------------#
    class _Item:
        """
        Lig0htweight composite to store key-value pairs as map items.
        """

        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key      # compare items based on their keys
        
        def __ne__(self, other):
            return not (self == other)      # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys