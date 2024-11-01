from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    """
    Our own version of collections.Sequence abstract base class.
    """

    @abstractmethod
    def __len__(self):
        # Return the length of the sequence.
        pass

    @abstractmethod
    def __getitem__(self, j):
        # Return the element index j of the sequence.
        pass

    def __contains__(self, val):
        # Return True if val found in the sequence; False if otherwise
        for i in range(len(self)):
            if self[i] == val:
                return True
            return False

    def index(self, val):
        # Return leftmost index at which val is found (or raise ValueError.)
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("Value not in sequence.")

    def count(self, val):
        # Return the number of elements equal to given value.
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
            return k