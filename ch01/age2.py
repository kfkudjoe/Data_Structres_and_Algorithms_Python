age = -1

while age <= 0:
    try:
        age = int(input("Enter your age in years: "))

        if age <= 0:
            print("Your age must be positive.")
    except ValueError:
        print("That is an invalid age specification.")
    except EOFError:
        print("There was an unexpected error reading input.")
        raise