def revers(S, start, stop):
    # Reverse elements in implicit slice S[start:stop]
    if start < stop - 1:        # If at least two elements, swap first and last
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)     # Narrow the interval and recurse on lower boundaries