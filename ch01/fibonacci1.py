def fibonacci():
    a = 0
    b = 1

    while True:
        yield a     # Report value a during this pass
        
        future = a + b
        a = b       # This will be the new value reported
        b = future      # and subsequently this