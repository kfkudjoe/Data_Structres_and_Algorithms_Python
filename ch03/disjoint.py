def disjoint1(A, B, C):
    # Return True if there is no elment common to all three lists.
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

def disjoint2(A, B, C):
    # Return True if there is no element common to all three lists.
    for a in A:
        for b in B:
            if a == b:      # only check C if we found a match from A and B
                for c in C:
                    if a == c:
                        return False
    return True     # The sets are disjoint