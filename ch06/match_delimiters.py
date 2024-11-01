from array_stack import ArrayStack

def is_matched(expression):
    # Return True if all delimiters are properly matched; False otherwise
    leftSide = '({['       # opening delimiters
    rightSide  = ']})'    # respective closing delimiters
    S = ArrayStack()

    for character in expression:
        if character in leftSide:
            S.push(character)       # push delimiter on stack
        elif character in rightSide:
            if S.is_empty():
                return False
            if righSide.index(character) != leftSide.index(S.pop()):
                return False        # mismatched

    return S.is_empty()     # were all symbols matched?