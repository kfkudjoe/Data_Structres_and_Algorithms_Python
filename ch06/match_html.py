from array_stack import ArrayStack

def is_matched_html(raw):
    # Return  True if all HTML tags are properly matched; False otherwise
    Stack = ArrayStack()
    i = raw.find("<")       # find the fist '<' character (if any)

    while i != -1:
        k = raw.find(">", i + 1)    # find the next '>' character

        if k == -1:
            return False   # invalid tag
        
        tag =  raw[i + 1: k]    # strip  away < >

        if not tag.startswith("/"):    # this is opening tag
            Stack.push(tag)
        else:
            if Stack.is_empty():
                return False    # nothing to match with
            if tag[1:] != Stack.pop():
                return False    # mismatched delimiter
        
        i  =  raw.find("<", k + 1)      # find next '<' character (if any)

    return S.is_empty()     # were all opening tags matched?
