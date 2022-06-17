def is_even(number):
    if isinstance(number, float):
        raise TypeError("Float is not allowed")
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    return number % 2==0