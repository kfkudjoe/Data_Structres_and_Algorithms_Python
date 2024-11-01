def count(data, target):
    n = 0

    for item in data:
        if item == target:
            n += 1
    return n