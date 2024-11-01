import collections

class Vector:
    """
    Represent a vector in a multidimensional space.
    """

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('Invalid parameter type.')

    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)

    def __getitem__(self, i):
        # Return the ith coordinate of a vector.
        return self._coords[i]

    def __setitem__(self, i, val):
        # Set the ith coordinate of a vector to given value.
        self._coords[i] = val

    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):     # Relies on __len__ method
            raise ValueError('Dimensions must agree.')
        
        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] + other[i]
        
        return result

    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords

    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other    # Rely on existing __eq__ definition

    def __str__(self):
        # Produce string representation of vectors.
        return '<' + str(self._coords)[1:-1] + '>'      # Adapt list representation

    def __neg__(self):
        # Return copy of vector with all coordinates negated
        result = Vector(len(self))      # Start with vector of zeros
        
        for i in range(len(self)):
            result[i] = -self[i]
        return result

    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return self._coords < other._coords

    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return self._coords <= other._coords



if __name__ == "__main__":
    # The following demonstrates the usage of a few methods.
    v = Vector(5)   # Construct 5-dimensional <0, 0, 0, 0, 0>
    v[1] = 23   # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45  # <0, 23, 0, 0, 45> (also via __setitem__)
    
    print(v[4]) # Print 45 (via __getitem__)
    
    u = v + v   # <0, 46, 0, 0, 90> (via __add__)
    
    print(u)    # Print <0, 46, 0, 0, 90>

    total = 0

    for entry in v:
        total += entry