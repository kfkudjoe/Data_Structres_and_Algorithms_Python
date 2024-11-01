class Progression:
    """
    Iterator producing a generic progression.
    Default iterator produces the whole numbers: 0, 1, 2, 3, ...
    """

    def __init__(self, start = 0):
        # Initialize current to the first value of the progression
        self._current  = start

    def _advance(self):
        # Update self._current to a new value.
        # This should be overridden by a subclass to customize progression.
        # By convention, if current is set to None, this designates.
        # The end of a finite progression.
        self._current += 1

    def __next__(self):
        # Return the next element, or else raise StopIteration error.
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            
            self._advance()
            return answer

    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self
    
    def print_progression(self, n):
        # Print the next n values of the progression.
        print(' '.join(str(next(self)) for i in range(n)
        ))


class ArithmeticProgression(Progression):
    """
    Iterator producing an arithmetic progression.
    """

    def __init__(self, increment = 1, start = 0):
        # Create a new arithmetic progression.
        # Increment - the fixed constant to add to each term (default 1)
        # Start - the first term of the progression (default 0)
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        # Update the current value by adding the fixed increment.
        self._current += self._increment


class GeometricProgression(Progression):
    """
    Iterator producing a geometric progression.
    """

    def __init__(self, base = 2, start = 1):
        # Create a new geometric progression.
        # Base - the fixed constant multiplied to each term (default is set to 2)
        # Start - the first term of the progression (default is set to 1)
        super().__init__(start)
        self._base = base

    def _advance(self):
        # Update the current value by multiplying it with the base value.
        self._current *= self._base


class FibonacciProgression(Progression):
    """
    Iterator producing a generalized Fibonacci progression.
    """
    def __init__(self, first = 0, second = 1):
        # Create a new Fibonacci progression
        # First - the first term of the progression (default is set to 0)
        # Second - the second term of the progression (default is set to 1)
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        # Update current value by taking sum of previous two.
        self._current = self._prev + self._current
        self._prev = self._current



if __name__ == "__main__":
    print("Default progression: ")
    Progression().print_progression(10)

    print("Arithmetic progression with increment 5: ")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic progression with increment 5 and start 2: ")
    ArithmeticProgression(5, 2).print_progression(10)

    print("Geometric progression with default base: ")
    GeometricProgression().print_progression(10)

    print("Geometric progression with base 3: ")
    GeometricProgression(3).print_progression(10)

    print("Fibonacci progression with default start values: ")
    FibonacciProgression().print_progression(10)

    print("Fibonacci progression with start values 4 and 6:")
    FibonacciProgression(4, 6).print_progression(10)
