# Author: Caleb Moura

def greeting():
    """
    This function prints "Hello World" on one line because it is it's only command.
    """
    print("Hello World!")

    # Return the docstring for greeting function.
    return greeting.__doc__

# Call greeting function.
greeting()