"""
python doctest_example.py
python doctest_example.py -v
python -m doctest -v doctest_example.py
"""

def findall_lod(lst, key, val):
    """Find all matches of key-value pair in list of dicts.

    >>> findall_lod([{'a': 1}, {'a': 1}], 'a', 1)
    [{'a': 1}, {'a': 1}]
    >>> findall_lod([{'a':1}, {'a':2}], 'a', 2)
    [{'a': 2}]
    >>> findall_lod([{'a': 1}, {'a': 2}], 'a', 3)
    []
    >>> findall_lod([{'a': 1}, {'a': 2}], 'a', '1')
    []
    >>> findall_lod([{'a': 1}, {'a': 2}], 'b', 1)
    Traceback (most recent call last):
        ...
    KeyError: 'b'
    """
    return [x for x in lst if x[key] == val]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
