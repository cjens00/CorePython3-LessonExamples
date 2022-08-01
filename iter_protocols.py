# Iteration Protocols
# - iterable: Can be passed to iter() to produce an iterator
# - iterator: Can be passed to next() to get the next value in the sequence
# Overloads: __iter__(), __next__()

# Example:
# The iterable object to be iterated over
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

# The external iterator object
iterator = iter(iterable)

# Get next element using the
first = next(iterator)
second = next(iterator)
third = next(iterator)
fourth = next(iterator)

