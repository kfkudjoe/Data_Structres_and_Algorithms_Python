from array_stack import ArrayStack

def reverse_file(filename):
    # Overwrite given file with its contents line-by-line reversed.
    S = ArrayStack()
    original = open(filename)

    for line in original:
        S.push(line.rstrip('\n'))       # new lines will be re-inserted when writing

    original.close()

    # Overwrite with contents in LIFO order
    output = open(filename, "w")    # reopening file overwrites origial
    
    while not Stack.is_empty():
        ouput.write(S.pop() + "\n")  # re-insert newline characters

    output.close()
    
