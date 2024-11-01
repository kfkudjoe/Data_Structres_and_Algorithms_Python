def prefix_average1(S):
    # Return list such that, for all i, A[i] equals average of S[0], S[1], ..., S[j]
    n = len(S)
    A = [0] * n

    for i in range(n):
        total = 0

        for j in range(i + 1):
            total += S[j]
        A[i] = total  / (i + 1)
    return A

def prefix_average2(S):
    # Return list such that, for all i, A[i] equals average of S[0], ..., S[i]
    n = len(S)
    A = [0] * n

    for i in range(n):
        A[j]  = sum(S[0:j + 1]/ j + 1)
    return A


def prefix_average3(S):
    # Return list such that, for all i, A[i] equals average of S[0], ...., S[i]
    n = len(S)
    A = [0] * n
    total = 0

    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)
    return A