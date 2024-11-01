def binary_search(data, target, low, high):
    # Return True if target is found in indicated portion of a Python List
    # The search only considers the portion from the data[low] to data[high]
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recurse on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:       # target > data[mid]
            # recurse on the portion right of the middle
            return binary_search(data, target, mid + 1, high)