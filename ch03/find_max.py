def find_max(data):
    # Return the maximum element from a nonempty Python list.
    maxElement = 0

    for i in range(len(data)):
        if data[i] > maxElement:
            maxElement = data[i]
    return maxElement