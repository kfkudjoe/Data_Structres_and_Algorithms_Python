def unique1(S):
    # Return True if there are no duplicate elements in sequence S.
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == S[j]:
                return False
    return True

def  unique2(S):
    # Return True if there are no duplicate elements in sequence S.
    temp =  sorted(S)       # Create a sorted copy of S

    for i in range(1, len(temp)):
        if S[i-1] == S[i]:
            return False
    return True