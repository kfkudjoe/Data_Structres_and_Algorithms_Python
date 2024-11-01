def insertion_sort(A):
    # Sort list of comparable elements into nondecreasing order.


    for k in range(1, len(A)):      # from 1 to n - 1
        currentElement = A[k]      # current element to be inserted
        i = k       # find correct index j for currentElement

        while i > 0 and A[i - 1] > currentElement:     # element A[i-1] must be after current
            A[i] = A[i-1]
            i -= 1
        A[i] = currentElement      # cur is now in the right place