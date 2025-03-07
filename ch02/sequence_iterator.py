class SequenceIterator:
    """
    An iterator for any of Python's sequence types.
    """

    def __init__(self, sequence):
        # Create an iterator for the given sequence.
        self._seq = sequence    # Keep a refernce to the underlying data
        self._k = -1    # Will increment to 0 on first call to next
    
    def __next__(self):
        # Return the next element, or eles raise StopIteration error.
        self._k += 1    # Advance to the next index

        if self._k < len(self._seq):
            return(self._seq[self._k])  # Return the data element
        else:
            raise StopIteration()   # There are no more elements
        

    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self