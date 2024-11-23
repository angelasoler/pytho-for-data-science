def ft_filter(func, iterable):
    """

    Args:
        func (function): return a boolean of the condition to filter
        iterable (any): iterable to be filter

    Returns:
        list: return a new list with the object filtered by function
    """
    ret = [item for item in iterable if func(item)]
    return ret
