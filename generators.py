# Generator Functions
# - Iterables defined by functions
# - Allow for the modeling of infinite sequences, e.g., streams
# - Composable into pipelines
# Any function that uses 'yield' one or more times in its definition.
# May also include return statements. Implicit return upon finishing execution.

# Basic conceptual example:
def Generate123():
    # First call to next(generator) begins execution here
    print("")
    # First call ends by yielding (returning) 1 from next(generator)
    yield 1
    # Second call to next() begins here
    # Second call to next() ends here by yielding 2
    yield 2
    # Third call to next() begins here
    # Third call to next() ends here by yielding 3
    yield 3


# Generator objects are iterators
g = Generate123()
print(g)

next(g)
print(g)

next(g)
print(g)

next(g)
print(g)

# Calling next(g) here raises StopIteration exception
