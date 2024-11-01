def unique3(S, start, stop):
    # Return True if there are no duplicate elements in slice S[start:stop]
    if stop - start <= 1:       # at most one item
        return True
    elif not unique(S, start, stop - 1):        # first part has duplicate
        return False
    elif not unique(S, start + 1, stop):        # second part has duplicate
        return False
    else:
        return S[start] != S[stop - 1]  # do first and last differ?