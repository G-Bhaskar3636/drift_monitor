def validate_input(reference, current):
    """
    Validate reference and current datasets.
    """

    if reference is None:
        raise ValueError("Reference data cannot be None.")

    if current is None:
        raise ValueError("Current data cannot be None.")

    if len(reference) == 0:
        raise ValueError("Reference data cannot be empty.")

    if len(current) == 0:
        raise ValueError("Current data cannot be empty.")

    if not hasattr(reference, "__iter__"):
        raise TypeError("Reference data must be iterable.")

    if not hasattr(current, "__iter__"):
        raise TypeError("Current data must be iterable.")

    return True